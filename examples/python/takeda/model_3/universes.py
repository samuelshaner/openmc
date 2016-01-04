import openmc
from cells import cells

###############################################################################
#                     Create dictionary with all universes
###############################################################################

universes = {}

# Instantiate Universe
universes['Root']                      = openmc.Universe(universe_id=0 , name='Root')
universes['Core']                      = openmc.Universe(universe_id=1 , name='Core')
universes['Axial Blanket']             = openmc.Universe(universe_id=2 , name='Axial Blanket')
universes['Radial Blanket']            = openmc.Universe(universe_id=3 , name='Radial Blanket')
universes['Internal Blanket']          = openmc.Universe(universe_id=4 , name='Internal Blanket')
universes['Control Rod']               = openmc.Universe(universe_id=5 , name='Control Rod')
universes['Na Filled CRP']             = openmc.Universe(universe_id=6 , name='Na Filled CRP')
universes['Radial Reflector']          = openmc.Universe(universe_id=7 , name='Radial Reflector')
universes['Axial Reflector']           = openmc.Universe(universe_id=8 , name='Axial Reflector')
universes['Empty Matrix']              = openmc.Universe(universe_id=9 , name='Empty Matrix')
universes['Internal Blanket Rodded']   = openmc.Universe(universe_id=10, name='Internal Blanket Rodded')
universes['Internal Blanket Unrodded'] = openmc.Universe(universe_id=11, name='Internal Blanket Unrodded')
universes['Internal Blanket Filled']   = openmc.Universe(universe_id=12, name='Internal Blanket Filled')
universes['Core Rodded']               = openmc.Universe(universe_id=13, name='Core Rodded')
universes['Core Unrodded']             = openmc.Universe(universe_id=14, name='Core Unrodded')
universes['Core Filled']               = openmc.Universe(universe_id=15, name='Core Filled')
universes['Axial Blanket Unrodded']    = openmc.Universe(universe_id=16, name='Axial Blanket Unrodded')
universes['Axial Blanket Filled']      = openmc.Universe(universe_id=17, name='Axial Blanket Filled')
universes['Axial Reflector Unrodded']  = openmc.Universe(universe_id=18, name='Axial Reflector Unrodded')
universes['Axial Reflector Filled']    = openmc.Universe(universe_id=19, name='Axial Reflector Filled')

# Register Cells with Universes
universes['Root']                     .add_cell(cells['Root'])
universes['Core']                     .add_cell(cells['Core'])
universes['Axial Blanket']            .add_cell(cells['Axial Blanket'])
universes['Radial Blanket']           .add_cell(cells['Radial Blanket'])
universes['Internal Blanket']         .add_cell(cells['Internal Blanket'])
universes['Control Rod']              .add_cell(cells['Control Rod'])
universes['Na Filled CRP']            .add_cell(cells['Na Filled CRP'])
universes['Radial Reflector']         .add_cell(cells['Radial Reflector'])
universes['Axial Reflector']          .add_cell(cells['Axial Reflector'])
universes['Empty Matrix']             .add_cell(cells['Empty Matrix'])
universes['Internal Blanket Rodded']  .add_cell(cells['Internal Blanket Rodded'])
universes['Internal Blanket Unrodded'].add_cell(cells['Internal Blanket Unrodded'])
universes['Internal Blanket Filled']  .add_cell(cells['Internal Blanket Filled'])
universes['Core Rodded']              .add_cell(cells['Core Rodded'])
universes['Core Unrodded']            .add_cell(cells['Core Unrodded'])
universes['Core Filled']              .add_cell(cells['Core Filled'])
universes['Axial Blanket Unrodded']   .add_cell(cells['Axial Blanket Unrodded'])
universes['Axial Blanket Filled']     .add_cell(cells['Axial Blanket Filled'])
universes['Axial Reflector Unrodded'] .add_cell(cells['Axial Reflector Unrodded'])
universes['Axial Reflector Filled']   .add_cell(cells['Axial Reflector Filled'])
