import openmc
from cells import cells

###############################################################################
#                     Create dictionary with all universes
###############################################################################

universes = {}

# Instantiate Universe
universes['Root']           = openmc.Universe(universe_id=0, name='Root')
universes['Core']           = openmc.Universe(universe_id=1, name='Core')
universes['Axial Blanket']  = openmc.Universe(universe_id=2, name='Axial Blanket')
universes['Radial Blanket'] = openmc.Universe(universe_id=3, name='Radial Blanket')
universes['Control Rod']    = openmc.Universe(universe_id=4, name='Control Rod')
universes['Na Filled CRP']  = openmc.Universe(universe_id=5, name='Na Filled CRP')
universes['Core Upper']     = openmc.Universe(universe_id=6, name='Core Upper')
universes['Core Lower']     = openmc.Universe(universe_id=7, name='Core Lower')
universes['Blanket Upper']  = openmc.Universe(universe_id=8, name='Blanket Upper')
universes['Blanket Lower']  = openmc.Universe(universe_id=9, name='Blanket Lower')

# Register Cells with Universes
universes['Root']          .add_cell(cells['Root'])
universes['Core']          .add_cell(cells['Core'])
universes['Axial Blanket'] .add_cell(cells['Axial Blanket'])
universes['Radial Blanket'].add_cell(cells['Radial Blanket'])
universes['Control Rod']   .add_cell(cells['Control Rod'])
universes['Na Filled CRP'] .add_cell(cells['Na Filled CRP'])
universes['Core Upper']    .add_cell(cells['Core Upper'])
universes['Core Lower']    .add_cell(cells['Core Lower'])
universes['Blanket Upper'] .add_cell(cells['Blanket Upper'])
universes['Blanket Lower'] .add_cell(cells['Blanket Lower'])
