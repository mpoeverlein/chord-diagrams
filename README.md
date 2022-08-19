# chord.py

There are multiple ways to represent relationships between two elements in a set of elements. 
In some scenarios, chord diagrams are great way of visualizing those relationships!
In a chord diagram, the elements are represented as arcs along a circle and the relationships as connecting curves.
This repository provides a simple, but powerful way of constructing chord diagrams with the python package matplotlib!

A simple chord diagram with random interactions can be created in the following way:

```
import numpy as np
import matplotlib.pyplot as plt

N = 5 # we will have 5 interacting units
unit_lengths = np.random.random(N) # each of the units has different weights
                                   # larger weight means longer arc
color_list = ['b', 'r', 'b', 'r', 'k']
label_list = ['along text','blong text','clong text','dlong text','elong text']
interactiosn = np.random.random(size=(N,N)) # the interactions are also random

chord = Chord()
chord.make_arcs(unit_lengths, N, colors=color_list, arc_kwargs={'linewidth': 10})
chord.make_labels(label_list, oriented=True,
chord.make_connectios_from_center(interactions, unit=1) # center of arc
```
