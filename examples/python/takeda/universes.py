import openmc
from cells import cells

###############################################################################
#                     Create dictionary with all universes
###############################################################################

universes = {}

# Instantiate Universe
universes['Root'] = openmc.Universe(universe_id=0, name='Root')
