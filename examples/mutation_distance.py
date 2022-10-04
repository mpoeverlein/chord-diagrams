import numpy as np
import pandas as pd
import chord
from matplotlib import cm

cmap = cm.get_cmap('Greys', 4)

def map_interaction(interaction, threshold=3):
    #return 0.2*interaction if interaction >= threshold else 0
    #return 0.5 * interaction if interaction == 1 else 0
    return interaction

def map_interaction_color(interaction):
    #return 'b' if interaction > 1 else 'r'
    return cmap(3-interaction)
    #return 'k'

df = pd.read_csv('mutation_distances.csv', index_col=0)
for col in df.columns:
    if col == 'K': continue
    df[col].values[:] = 0
#print(df)

colors = 'k'
labels = df.columns
arc_kwargs = {'linewidth': 1}
text_kwargs = {'fontsize': 10, 'alpha': 1, 'weight': 'medium'}
chord = chord.Chord()
chord.make_arcs(np.ones_like(df.columns), gap_angle=1, colors=colors, arc_kwargs=arc_kwargs)
chord.make_labels(labels, oriented=False, centered=True, text_kwargs=text_kwargs)
chord.make_chords_from_centers_of_arcs(df.values, map_interaction_function=map_interaction, map_interaction_color_function=map_interaction_color, direction='backward')
#chord.make_chords_with_proportions(df.values, map_interaction_function=map_interaction, map_interaction_color_function=map_interaction_color)
#chord.make_chord_from_one_unit(np.random.random(size=(N,N)), unit=1)


chord.show()
