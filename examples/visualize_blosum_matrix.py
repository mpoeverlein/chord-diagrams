import chord
import numpy as np
import pandas as pd

#df = pd.read_csv('blosum62.txt', comment='#', sep=' ')
df = pd.read_csv('blosum62.txt', comment='#', delim_whitespace=True)
df = df.drop(labels=['*'], axis=0)
df = df.drop(labels=['*'], axis=1)

def map_interaction(interaction):
    return abs(interaction) * 0.2

def map_interaction_color(interaction):
    return 'b' if interaction > 0 else 'r'


colors = 'k'
labels = df.columns
arc_kwargs = {'linewidth': 1}
text_kwargs = {'fontsize': 10, 'alpha': 1, 'weight': 'medium'}
chord = chord.Chord()
chord.make_arcs(np.ones_like(df.columns), gap_angle=0.1, colors=colors, arc_kwargs=arc_kwargs)
chord.make_labels(labels, oriented=False, centered=True, text_kwargs=text_kwargs)
chord.make_chords_from_centers_of_arcs(df.values, map_interaction_function=map_interaction, map_interaction_color_function=map_interaction_color)
#chord.make_chord_from_one_unit(np.random.random(size=(N,N)), unit=1)


chord.show()
