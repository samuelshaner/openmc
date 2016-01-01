import openmc
from materials import materials
from surfaces import surfaces

###############################################################################
#                   Create dictionary of all cells
###############################################################################

cells = {}

# Instantiate Cells
cells['Core']        = openmc.Cell(cell_id=1, name='Core')
cells['Control Rod'] = openmc.Cell(cell_id=2, name='Control Rod')
cells['Void']        = openmc.Cell(cell_id=2, name='Void')
cells['Reflector']   = openmc.Cell(cell_id=3, name='Reflector')

# Use surface half-spaces to define regions
cells['Core']       .region = +surfaces['Core x-min'] & +surfaces['Core y-min'] & +surfaces['Core z-min'] & \
                              -surfaces['Core x-max'] & -surfaces['Core y-max'] & -surfaces['Core z-max']
cells['Control Rod'].region = +surfaces['Core x-max'] & -surfaces['Void x-max'] & +surfaces['Core y-min'] & \
                              -surfaces['Void y-max'] & +surfaces['Core z-min'] & -surfaces['Core z-max']
cells['Void']       .region =  +surfaces['Core x-max'] & -surfaces['Void x-max'] & +surfaces['Core y-min'] & \
                              -surfaces['Void y-max'] & +surfaces['Core z-min'] & -surfaces['Core z-max']
cells['Reflector']  .region = ~cells['Core'].region & ~(+surfaces['Core x-max'] & -surfaces['Void x-max'] & +surfaces['Core y-min'] & \
                              -surfaces['Void y-max'] & +surfaces['Core z-min'] & -surfaces['Core z-max']) & \
                              +surfaces['Core x-min'] & +surfaces['Core y-min'] & +surfaces['Core z-min'] & \
                              -surfaces['Core x-max'] & -surfaces['Core y-max'] & -surfaces['Core z-max']

# Register Materials with Cells
cells['Core'].fill = materials['Core']
cells['Void'].fill = materials['Void']
cells['Control Rod'].fill = materials['Control Rod']
cells['Reflector'].fill = materials['Reflector']
