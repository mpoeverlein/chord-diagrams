#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Arc, PathPatch
from matplotlib.path import Path


class Chord:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim((-1.1,1.1))
        self.ax.set_ylim((-1.1,1.1))
        self.ax.set_aspect(1)
        plt.axis('off')

    def make_arcs(self, arc_lengths, gap_angle, linewidth=3, colors=None):
        colors = self.get_colors(arc_lengths, colors)
        total_lengths = arc_lengths.sum()
        self.angle_centers = []
        self.arcs = []
        for c, (arc_length, color) in enumerate(zip(arc_lengths, colors)):
            start_angle = arc_lengths[:c].sum() / total_lengths * 360 + gap_angle / 2
            end_angle = arc_lengths[:c+1].sum() / total_lengths * 360 - gap_angle / 2
            self.angle_centers.append(0.5 * (start_angle + end_angle))
            arc = Arc((0, 0), 2, 2, theta1=start_angle, theta2=end_angle, fill=False, lw=linewidth, color=color)
            self.arcs.append(arc)
            self.ax.add_patch(arc)

    def make_labels(self, labels, colors=None, oriented=False):
        self.labels = []
        colors = self.get_colors(labels, colors)
        for label, angle_center, color in zip(labels, self.angle_centers, colors):
            (ha, va, rotation_angle) = self.angle2alignment(angle_center)
            if not oriented:
                rotation_angle = 0
            coords = self.angle2coord(angle_center, r=1.1)
            text = self.ax.text(*coords, label, ha=ha, va=va, color=color, rotation=rotation_angle, fontsize=12)
            self.labels.append(text)

    def make_chords_from_centers_of_arcs(self, interactions, symmetric=True):
        if symmetric:
            interactions = np.triu(interactions)

        for start_index, end_index in np.ndindex(interactions.shape):
            if start_index == end_index: continue

            start_angle = self.angle_centers[start_index]
            end_angle = self.angle_centers[end_index]
            interaction = interactions[start_index, end_index]

            if interaction == 0: continue

            pp1 = PathPatch(
                Path([self.angle2coord(start_angle), (0,0), self.angle2coord(end_angle)],
                     [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
                     fc="none", 
                     transform=self.ax.transData, 
                     lw=self.map_correlation(interaction), 
                     color=self.map_correlation_color(interaction))

            self.ax.add_patch(pp1)

    def make_chord_from_one_unit(self, interactions, unit=0):
        old_interactions = interactions.copy()
        interactions = np.zeros_like(interactions)
        interactions[unit,:] = old_interactions[unit,:]
        self.make_chords_from_centers_of_arcs(interactions, symmetric=False)

        for arc in self.arcs:
            arc.set(alpha=0.1)
        self.arcs[unit].set(alpha=1)

#        for label in self.labels:
#            label.set(alpha=0.1)
#        self.labels[unit].set(alpha=1)
    

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
        colors = colors or 'k'
        if isinstance(colors, str):
            colors = len(property_list) * [colors]

        return colors

    @staticmethod
    def map_correlation(interaction, threshold=0):
        return interaction if abs(interaction) >= threshold else 0       

    @staticmethod
    def map_correlation_color(interaction):
        return 'k'


N = 5
chord = Chord()
chord.make_arcs(np.random.random(N), 5, colors=['b', 'r', 'b', 'r', 'k'])
#chord.make_labels_horizontal(['along text','blong text','clong text','dlong text','elong text'])
#chord.make_labels_adjusted(['along text','blong text','clong text','dlong text','elong text'])
chord.make_labels(['along text','blong text','clong text','dlong text','elong text'], oriented=True)
#chord.make_connections_from_center(np.random.random(size=(N,N)))
chord.make_chord_from_one_unit(np.random.random(size=(N,N)), unit=1)


chord.show()

