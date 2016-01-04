import openmc
from materials import materials
from surfaces import surfaces

###############################################################################
#                   Create dictionary of all cells
###############################################################################

cells = {}

# Instantiate Cells
cells['Root']           = openmc.Cell(cell_id=1 , name='Root')
cells['Core']           = openmc.Cell(cell_id=2 , name='Core')
cells['Axial Blanket']  = openmc.Cell(cell_id=3 , name='Axial Blanket')
cells['Radial Blanket'] = openmc.Cell(cell_id=4 , name='Radial Blanket')
cells['Control Rod']    = openmc.Cell(cell_id=5 , name='Control Rod')
cells['Na Filled CRP']  = openmc.Cell(cell_id=6 , name='Na Filled CRP')
cells['Core Upper']     = openmc.Cell(cell_id=7 , name='Core Upper')
cells['Core Lower']     = openmc.Cell(cell_id=8 , name='Core Lower')
cells['Blanket Upper']  = openmc.Cell(cell_id=9 , name='Blanket Upper')
cells['Blanket Lower']  = openmc.Cell(cell_id=10, name='Blanket Lower')

# Use surface half-spaces to define regions
cells['Root']       .region = +surfaces['Core x-min'] & +surfaces['Core y-min'] & +surfaces['Core z-min'] & \
                              -surfaces['Core x-max'] & -surfaces['Core y-max'] & -surfaces['Core z-max']

# Register Materials with Cells
cells['Core'].fill           = materials['Core']
cells['Axial Blanket'].fill  = materials['Axial Blanket']
cells['Radial Blanket'].fill = materials['Radial & Inner Blanket']
cells['Control Rod'].fill    = materials['Control Rod']
cells['Na Filled CRP'].fill  = materials['Na Filled CRP']
