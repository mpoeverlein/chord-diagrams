import numpy as np
import pandas as pd
import chord
from matplotlib import cm


def map_interaction_function(value):
    return 0 if value == 1 else 1

def map_interaction_color_function(value):
    d = {0: 'black', 0.5: 'red', 1: 'white', 2: 'blue'} 
    return d[value]

df = pd.read_csv('pokemontypes.csv', index_col=0, skiprows=1)
df = df.astype(float)

arc_lengths = np.array([1 for _ in df.columns])
pkmn_types = df.columns
type_colors = ['#aaaa99', '#ff4422', '#3399ff', '#ffcc33', '#77cc55', '#66ccff', '#bb5544', '#aa5599', '#ddbb55', '#8899ff', 
               '#ff5599', '#aabb22', '#bbaa66', '#6666bb', '#7766ee', '#775544', '#aaaabb', '#ee99ee'     
        ]


chord = chord.Chord()
chord.make_arcs(arc_lengths)
#chord.make_labels(pkmn_types, text_colors=type_colors, text_kwargs={'fontsize': 10, 'bbox': props})
chord.make_labels([s.upper() for s in pkmn_types], text_colors='white', background_colors=type_colors)
#chord.make_labels([s.upper() for s in pkmn_types], text_colors=type_colors, background_colors='white', bbox_colors='white')

#chord.make_chords_from_centers_of_arcs(interactions=df.values, map_interaction_function=map_interaction_function, map_interaction_color_function=map_interaction_color_function, direction='forward')
chord.make_chords_both_directions(interactions=df.values, map_interaction_function=map_interaction_function, map_interaction_color_function=map_interaction_color_function)

chord.show()
