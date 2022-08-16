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
        print(total_lengths)
        self.angle_centers = []
        for c, (arc_length, color) in enumerate(zip(arc_lengths, colors)):
            start_angle = arc_lengths[:c].sum() / total_lengths * 360 + gap_angle
            end_angle = arc_lengths[:c+1].sum() / total_lengths * 360
            print(start_angle, end_angle)
            self.angle_centers.append(0.5 * (start_angle + end_angle))
            self.ax.add_patch(Arc((0, 0), 2, 2, theta1=start_angle, theta2=end_angle, fill=False, lw=linewidth, color=color))

        print(arc_lengths/total_lengths)
        print(self.angle_centers)

    def make_labels_horizontal(self, labels, colors=None):
        colors = self.get_colors(labels, colors)
        for label, angle_center, color in zip(labels, self.angle_centers, colors):
            (ha, va, rotation_angle) = self.angle2alignment(angle_center)
            self.ax.text(*self.angle2coord(angle_center, r=1.1), label, fontsize=12, ha=ha, va=va, color=color)

    def make_labels_adjusted(self, labels, colors=None):
        colors = self.get_colors(labels, colors)
        for label, angle_center, color in zip(labels, self.angle_centers, colors):
            (ha, va, rotation_angle) = self.angle2alignment(angle_center)
            self.ax.text(*self.angle2coord(angle_center, r=1.1), label, fontsize=12, ha=ha, va=va, color=color, rotation=rotation_angle)

    def make_connections_from_center(self, interactions):
        for start_index, end_index in np.ndindex(interactions.shape):
            if start_index == end_index: continue

            start_angle = self.angle_centers[start_index]
            end_angle = self.angle_centers[end_index]

            interaction = interactions[start_index, end_index]

            pp1 = PathPatch(
                Path([self.angle2coord(start_angle), (0,0), self.angle2coord(end_angle)],
                     [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
                fc="none", transform=self.ax.transData, lw=self.map_correlation(interaction), color=self.map_correlation_color(interaction))

            self.ax.add_patch(pp1)
    

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
        if colors is None:
            colors = 'k'
        if isinstance(colors, str):
            colors = len(property_list) * [colors]

        return colors

    @staticmethod
    def map_correlation(interaction, threshold=0.5):
        return interaction if abs(interaction) >= threshold else 0       

    @staticmethod
    def map_correlation_color(interaction):
        return 'k'


N = 5
chord = Chord()
chord.make_arcs(np.random.random(N), 5, colors=['b', 'r', 'b', 'r', 'k'])
chord.make_labels_horizontal(['long text','long text','clong text','dlong text','elong text'])
#chord.make_labels_adjusted(['long text','long text','clong text','dlong text','elong text'])
chord.make_connections_from_center(np.random.random(size=(N,N)))


chord.show()


# pp1 = PathPatch(
#     Path([angle2coord(subunit_angle1), (0,0), angle2coord(subunit_angle2)],
#          [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
#     fc="none", transform=ax.transData, lw=map_correlation(cvalue, threshold=threshold), color=map_correlation_color(cvalue)) 
#
# ax.add_patch(pp1)
