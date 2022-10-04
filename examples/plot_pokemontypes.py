import numpy as np
import pandas as pd
import chord
from matplotlib import cm

df = pd.read_csv('pokemontypes.csv', index_col=0, skiprows=1)
df = df.astype(float)


#factor_one = (~(df.notnull())).astype('int')
#print(factor_one)
#df += factor_one

print(df)

arc_lengths = np.array([1 for _ in df.columns])
pkmn_types = df.columns

chord = chord.Chord()
chord.make_arcs(arc_lengths)
chord.make_labels(pkmn_types)

chord.show()
