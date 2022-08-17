#!/usr/bin/env python3

import numpy as np
import chord

N = 6
colors = ['k', 'grey', 'blue', 'orange', 'k', 'green']
arc_kwargs = {'linewidth': 1}
text_kwargs = {'fontsize': 10, 'alpha': 1, 'weight': 'medium'}
chord = chord.Chord()
chord.make_arcs(np.random.random(N), gap_angle=5, colors=colors, arc_kwargs=arc_kwargs)
chord.make_labels(['along text','blong text','clong text','dlong text','elong text'], oriented=True, text_kwargs=text_kwargs)
chord.make_chords_from_centers_of_arcs(np.random.random(size=(N,N)))
#chord.make_chord_from_one_unit(np.random.random(size=(N,N)), unit=1)


chord.show()


