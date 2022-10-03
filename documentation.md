# Class Chord
## __init__
takes no arguments, creates the base of the figure using [matplotlib.pyplot.subplots](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html)

## make_arcs
adds arcs to figure.
### Parameters
- arc_lengths: list/np.ndarray of arc lengths
- gap_angle: gap angle between individual arcs in degrees (default: 5)
- colors: list of colors used for each arc. if `colors` is of type str, it is interpreted as a single color used for all arcs
- arc_kwargs: dict of arguments that are supplied to [matplotlib.patches.Arc](https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Arc.html)

## make_labels
adds labels for arcs to figure.
### Parameters
- labels: list of labels to use for arcs. 
- colors: list of colors used for each arc. if `colors` is of type str, it is interpreted as a single color used for all arcs
- oriented: bool, describes if label is rotated to be vertical to the tangential of the corresponding arc
- centered: bool, describes if label alignment is aligned (both vertically and horizontally)
- text_kwargs: dict of arguments that are supplied to [matplotlib.axes.Axes.text](https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html)

## make_chords_from_centers_of_arcs
connect arcs with each other using chords
### Parameters
- interactions: 2d np.ndarray describing interactions
- map_interaction_function: function mapping interaction to linewidth of chord (default: map_interaction)
- map_interaction_color_function: function mapping interaction to color of chord (default: map_interaction_color)
- direction: 'forward', 'backward', or 'symmetric', describes if chord A-B describes interaction A->B or B->A. ('symmetric' uses A->B)
- path_kwargs: dict of arguments that are supplied to [matplotlib.path.Path](https://matplotlib.org/stable/api/path_api.html#matplotlib.path.Path)

## make_chord_from_one_unit
Chords starting from only one arc are considered. 
### Parameters
- interactions: 2d np.ndarray describing **all** interactions
- unit: index of the arc from which chords will originate (default: 0)
- highlight_arc: bool, all other arcs are set to have opacity of 0.1 (default: True)
- highlight_label: bool, all other labels are set to have opacity of 0.1 (default: False)

## angle2coord
given an angle in degrees and a radius, return the complex number `r * e ^ (i*angle)`
### Parameters
- angle: int/float
- radius: int/float (default: 1)

## angle2alignment
needed to align label to arc

## get_colors
turn color string into color list
### Parameters
- property_list: list of labels/arc lengths
- colors: list of colors used for each label/arc or str of one color

## show
simply calls [plt.show](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html)
