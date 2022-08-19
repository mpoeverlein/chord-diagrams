#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, PathPatch
from matplotlib.path import Path


def map_interaction(interaction, threshold=0):
    return interaction if abs(interaction) >= threshold else 0       

def map_interaction_color(interaction):
    return 'k'


class Chord:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim((-1.1,1.1))
        self.ax.set_ylim((-1.1,1.1))
        self.ax.set_aspect(1)
        plt.axis('off')

    def make_arcs(self, arc_lengths, gap_angle=5, colors='k',
        arc_kwargs={'fill': False, 'linewidth': 1}):

        colors = self.get_colors(arc_lengths, colors)
        total_lengths = arc_lengths.sum()
        self.angle_centers = []
        self.arcs = []
        for c, (arc_length, color) in enumerate(zip(arc_lengths, colors)):
            start_angle = arc_lengths[:c].sum() / total_lengths * 360 + gap_angle / 2
            end_angle = arc_lengths[:c+1].sum() / total_lengths * 360 - gap_angle / 2
            self.angle_centers.append(0.5 * (start_angle + end_angle))
            arc = Arc((0, 0), 2, 2, theta1=start_angle, theta2=end_angle, 
                      color=color, **arc_kwargs)
            self.arcs.append(arc)
            self.ax.add_patch(arc)

    def make_labels(self, labels, colors='k', oriented=False, centered=False,
        text_kwargs={'fontsize': 12}):

        self.labels = []
        colors = self.get_colors(labels, colors)
        for label, angle_center, color in zip(labels, self.angle_centers, colors):
            (ha, va, rotation_angle) = self.angle2alignment(angle_center)
            rotation_angle = rotation_angle if oriented else 0
            if centered:
                ha, va = 'center', 'center'
            coords = self.angle2coord(angle_center, r=1.1)
            text = self.ax.text(*coords, label, ha=ha, va=va, color=color, rotation=rotation_angle, **text_kwargs)
            self.labels.append(text)

    def make_chords_from_centers_of_arcs(self, interactions, 
        map_interaction_function=map_interaction, 
        map_interaction_color_function=map_interaction_color, 
        direction='forward',
        path_kwargs={'fc': 'none'}):

        if direction in ['forward', 'symmetric']:
            interactions = np.triu(interactions)
        else:
            interactions = np.tril(interactions)

        for start_index, end_index in np.ndindex(interactions.shape):
            if start_index == end_index: 
                continue
            interaction = interactions[start_index, end_index]
            if interaction == 0: 
                continue
            start_angle = self.angle_centers[start_index]
            end_angle = self.angle_centers[end_index]

            pp1 = PathPatch(
                Path([self.angle2coord(start_angle), (0,0), self.angle2coord(end_angle)],
                     [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
                     transform=self.ax.transData, 
                     lw=map_interaction_function(interaction), 
                     color=map_interaction_color_function(interaction),
                     **path_kwargs)

            self.ax.add_patch(pp1)

    def make_chord_from_one_unit(self, interactions, unit=0, highlight_arc=True, highlight_label=False):
        # we select row of interactions by setting all other elements of the array to zero and then pass it on
        old_interactions = interactions.copy()
        interactions = np.zeros_like(interactions)
        interactions[unit,:] = old_interactions[unit,:]
        interactions[:,unit] = old_interactions[:,unit]

        self.make_chords_from_centers_of_arcs(interactions, direction='forward')

        if highlight_arc:
            for arc in self.arcs:
                arc.set(alpha=0.1)
            self.arcs[unit].set(alpha=1)

        if highlight_label:
            for label in self.labels:
                label.set(alpha=0.1)
            self.labels[unit].set(alpha=1)
    
    def show(self):
        plt.show()

    @staticmethod
    def angle2coord(angle, r=1):
        ''' given an angle in degrees and a radius, return the complex number r * e ^ (i*angle)'''
        phi = np.pi * angle / 180
        c = r * np.exp(1j*phi)
        return (c.real, c.imag)
    
    @staticmethod
    def angle2alignment(angle):
        if angle < 90: return ('left', 'bottom', angle)
        elif angle < 180: return ('right', 'bottom', angle+180)
        elif angle < 270: return ('right', 'top', angle+180)
        else: return ('left', 'top', angle)

    @staticmethod
    def get_colors(property_list, colors):
        if isinstance(colors, str):
            colors = len(property_list) * [colors]

        return colors


if __name__ == '__main__':
    N = 5
    chord = Chord()
    chord.make_arcs(np.random.random(N), 5, colors=['b', 'r', 'b', 'r', 'k'], arc_kwargs={'linewidth': 10})
    #chord.make_labels_horizontal(['along text','blong text','clong text','dlong text','elong text'])
    #chord.make_labels_adjusted(['along text','blong text','clong text','dlong text','elong text'])
    chord.make_labels(['along text','blong text','clong text','dlong text','elong text'], oriented=True, text_kwargs={'fontsize': 14, 'alpha': 0.1, 'weight': 'extra bold'})
    #chord.make_connections_from_center(np.random.random(size=(N,N)))
    chord.make_chord_from_one_unit(np.random.random(size=(N,N)), unit=1)
    
    
    chord.show()
    
