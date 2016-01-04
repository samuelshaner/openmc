import openmc
from materials import materials
from surfaces import surfaces

###############################################################################
#                   Create dictionary of all cells
###############################################################################

cells = {}

# Instantiate Cells
cells['Root']                      = openmc.Cell(cell_id=1 , name='Root')
cells['Core']                      = openmc.Cell(cell_id=2 , name='Core')
cells['Axial Blanket']             = openmc.Cell(cell_id=3 , name='Axial Blanket')
cells['Radial Blanket']            = openmc.Cell(cell_id=4 , name='Radial Blanket')
cells['Internal Blanket']          = openmc.Cell(cell_id=5 , name='Internal Blanket')
cells['Control Rod']               = openmc.Cell(cell_id=6 , name='Control Rod')
cells['Na Filled CRP']             = openmc.Cell(cell_id=7 , name='Na Filled CRP')
cells['Radial Reflector']          = openmc.Cell(cell_id=8 , name='Radial Reflector')
cells['Axial Reflector']           = openmc.Cell(cell_id=9 , name='Axial Reflector')
cells['Empty Matrix']              = openmc.Cell(cell_id=10, name='Empty Matrix')
cells['Internal Blanket Rodded']   = openmc.Cell(cell_id=11, name='Internal Blanket Rodded')
cells['Internal Blanket Unrodded'] = openmc.Cell(cell_id=12, name='Internal Blanket Unrodded')
cells['Internal Blanket Filled']   = openmc.Cell(cell_id=13, name='Internal Blanket Filled')
cells['Core Rodded']               = openmc.Cell(cell_id=14, name='Core Rodded')
cells['Core Unrodded']             = openmc.Cell(cell_id=15, name='Core Unrodded')
cells['Core Filled']               = openmc.Cell(cell_id=16, name='Core Filled')
cells['Axial Blanket Unrodded']    = openmc.Cell(cell_id=17, name='Axial Blanket Unrodded')
cells['Axial Blanket Filled']      = openmc.Cell(cell_id=18, name='Axial Blanket Filled')
cells['Axial Reflector Unrodded']  = openmc.Cell(cell_id=19, name='Axial Reflector Unrodded')
cells['Axial Reflector Filled']    = openmc.Cell(cell_id=20, name='Axial Reflector Filled')

# Use surface half-spaces to define regions
cells['Root']       .region = +surfaces['Core x-min'] & +surfaces['Core y-min'] & +surfaces['Core z-min'] & \
                              -surfaces['Core x-max'] & -surfaces['Core y-max'] & -surfaces['Core z-max']

# Register Materials with Cells
cells['Core'].fill             = materials['Core']
cells['Axial Blanket'].fill    = materials['Axial Blanket']
cells['Radial Blanket'].fill   = materials['Radial & Inner Blanket']
cells['Internal Blanket'].fill = materials['Radial & Inner Blanket']
cells['Control Rod'].fill      = materials['Control Rod']
cells['Na Filled CRP'].fill    = materials['Na Filled CRP']
cells['Radial Reflector'].fill = materials['Radial Reflector']
cells['Axial Reflector'].fill  = materials['Axial Reflector']
cells['Empty Matrix'].fill     = materials['Empty Matrix']
