import openmc
from materials import pin_materials, water
from surfaces import surfaces

###############################################################################
#                     Create a dictionary of all shared cells
###############################################################################

# Instantiate Cells
cells = {}
cells['Fuel Rod Fuel']                    = openmc.Cell(name='Fuel Rod Fuel')
cells['Fuel Rod Gap']                     = openmc.Cell(name='Fuel Rod Gap')
cells['Fuel Rod Clad']                    = openmc.Cell(name='Fuel Rod Clad')
cells['Al Rod Al']                        = openmc.Cell(name='Al Rod Al')
cells['B4C Rod B4C']                      = openmc.Cell(name='B4C Rod B4C')
cells['B4C Rod Clad']                     = openmc.Cell(name='B4C Rod Clad')

cells['Reflector Core 1']                 = openmc.Cell(name='Reflector Core 1')
cells['Reflector Core 2']                 = openmc.Cell(name='Reflector Core 2')
cells['Reflector Core 3']                 = openmc.Cell(name='Reflector Core 3')
cells['Reflector Core 4']                 = openmc.Cell(name='Reflector Core 4')
cells['Reflector Core 5']                 = openmc.Cell(name='Reflector Core 5')
cells['Reflector Core 6']                 = openmc.Cell(name='Reflector Core 6')
cells['Reflector Core 7']                 = openmc.Cell(name='Reflector Core 7')
cells['Reflector Core 8']                 = openmc.Cell(name='Reflector Core 8')
cells['Reflector Core 9']                 = openmc.Cell(name='Reflector Core 9')
cells['Reflector Core 10']                = openmc.Cell(name='Reflector Core 10')

cells['Fuel Rod Moderator Core 1']        = openmc.Cell(name='Fuel Rod Moderator Core 1')
cells['Fuel Rod Moderator Core 2']        = openmc.Cell(name='Fuel Rod Moderator Core 2')
cells['Fuel Rod Moderator Core 3']        = openmc.Cell(name='Fuel Rod Moderator Core 3')
cells['Fuel Rod Moderator Core 4']        = openmc.Cell(name='Fuel Rod Moderator Core 4')
cells['Fuel Rod Moderator Core 5']        = openmc.Cell(name='Fuel Rod Moderator Core 5')
cells['Fuel Rod Moderator Core 6']        = openmc.Cell(name='Fuel Rod Moderator Core 6')
cells['Fuel Rod Moderator Core 7']        = openmc.Cell(name='Fuel Rod Moderator Core 7')
cells['Fuel Rod Moderator Core 8']        = openmc.Cell(name='Fuel Rod Moderator Core 8')
cells['Fuel Rod Moderator Core 9']        = openmc.Cell(name='Fuel Rod Moderator Core 9')
cells['Fuel Rod Moderator Core 10']       = openmc.Cell(name='Fuel Rod Moderator Core 10')

cells['Al Rod Moderator Core 1']          = openmc.Cell(name='Al Rod Moderator Core 1')
cells['Al Rod Moderator Core 2']          = openmc.Cell(name='Al Rod Moderator Core 2')
cells['Al Rod Moderator Core 3']          = openmc.Cell(name='Al Rod Moderator Core 3')
cells['Al Rod Moderator Core 4']          = openmc.Cell(name='Al Rod Moderator Core 4')
cells['Al Rod Moderator Core 5']          = openmc.Cell(name='Al Rod Moderator Core 5')
cells['Al Rod Moderator Core 6']          = openmc.Cell(name='Al Rod Moderator Core 6')
cells['Al Rod Moderator Core 7']          = openmc.Cell(name='Al Rod Moderator Core 7')
cells['Al Rod Moderator Core 8']          = openmc.Cell(name='Al Rod Moderator Core 8')
cells['Al Rod Moderator Core 9']          = openmc.Cell(name='Al Rod Moderator Core 9')
cells['Al Rod Moderator Core 10']         = openmc.Cell(name='Al Rod Moderator Core 10')

cells['B4C Rod Moderator Core 1']         = openmc.Cell(name='B4C Rod Moderator Core 1')
cells['B4C Rod Moderator Core 2']         = openmc.Cell(name='B4C Rod Moderator Core 2')
cells['B4C Rod Moderator Core 3']         = openmc.Cell(name='B4C Rod Moderator Core 3')
cells['B4C Rod Moderator Core 4']         = openmc.Cell(name='B4C Rod Moderator Core 4')
cells['B4C Rod Moderator Core 5']         = openmc.Cell(name='B4C Rod Moderator Core 5')
cells['B4C Rod Moderator Core 6']         = openmc.Cell(name='B4C Rod Moderator Core 6')
cells['B4C Rod Moderator Core 7']         = openmc.Cell(name='B4C Rod Moderator Core 7')
cells['B4C Rod Moderator Core 8']         = openmc.Cell(name='B4C Rod Moderator Core 8')
cells['B4C Rod Moderator Core 9']         = openmc.Cell(name='B4C Rod Moderator Core 9')
cells['B4C Rod Moderator Core 10']        = openmc.Cell(name='B4C Rod Moderator Core 10')

cells['Core 1']                           = openmc.Cell(name='Core 1')
cells['Core 2']                           = openmc.Cell(name='Core 2')
cells['Core 3']                           = openmc.Cell(name='Core 3')
cells['Core 4']                           = openmc.Cell(name='Core 4')
cells['Core 5']                           = openmc.Cell(name='Core 5')
cells['Core 6']                           = openmc.Cell(name='Core 6')
cells['Core 7']                           = openmc.Cell(name='Core 7')
cells['Core 8']                           = openmc.Cell(name='Core 8')
cells['Core 9']                           = openmc.Cell(name='Core 9')
cells['Core 10']                          = openmc.Cell(name='Core 10')

# Use surface half-spaces to define regions
cells['Fuel Rod Fuel'].region              = -surfaces['Fuel OR']
cells['Fuel Rod Gap'].region               = +surfaces['Fuel OR'] & -surfaces['Fuel Clad IR']
cells['Fuel Rod Clad'].region              = +surfaces['Fuel Clad IR'] & -surfaces['Fuel Clad OR']
cells['Al Rod Al'].region                  = -surfaces['Threaded Al R']
cells['B4C Rod B4C'].region                = -surfaces['B4C Clad IR']
cells['B4C Rod Clad'].region               = +surfaces['B4C Clad IR'] & -surfaces['B4C Clad OR']


cells['Fuel Rod Moderator Core 1'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 2'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 3'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 4'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 5'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 6'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 7'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 8'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 9'].region  = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 10'].region = +surfaces['Fuel Clad OR']

cells['Al Rod Moderator Core 1'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 2'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 3'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 4'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 5'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 6'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 7'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 8'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 9'].region    = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 10'].region   = +surfaces['Threaded Al R']

cells['B4C Rod Moderator Core 1'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 2'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 3'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 4'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 5'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 6'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 7'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 8'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 9'].region   = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 10'].region  = +surfaces['B4C Clad OR']

cells['Core 1'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 2'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 3'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 4'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 5'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 6'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 7'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 8'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 9'].region                      = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 10'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']

# Register Materials with Cells
cells['Fuel Rod Fuel'].fill              = pin_materials['Fuel']
cells['Fuel Rod Gap'].fill               = pin_materials['Gap']
cells['Fuel Rod Clad'].fill              = pin_materials['SS']
cells['Al Rod Al'].fill                  = pin_materials['Al']
cells['B4C Rod B4C'].fill                = pin_materials['B4C']
cells['B4C Rod Clad'].fill               = pin_materials['SS']

cells['Fuel Rod Moderator Core 1'].fill  = water[1]
cells['Fuel Rod Moderator Core 2'].fill  = water[2]
cells['Fuel Rod Moderator Core 3'].fill  = water[3]
cells['Fuel Rod Moderator Core 4'].fill  = water[4]
cells['Fuel Rod Moderator Core 5'].fill  = water[5]
cells['Fuel Rod Moderator Core 6'].fill  = water[6]
cells['Fuel Rod Moderator Core 7'].fill  = water[7]
cells['Fuel Rod Moderator Core 8'].fill  = water[8]
cells['Fuel Rod Moderator Core 9'].fill  = water[9]
cells['Fuel Rod Moderator Core 10'].fill = water[10]

cells['Al Rod Moderator Core 1'].fill   = water[1]
cells['Al Rod Moderator Core 2'].fill   = water[2]
cells['Al Rod Moderator Core 3'].fill   = water[3]
cells['Al Rod Moderator Core 4'].fill   = water[4]
cells['Al Rod Moderator Core 5'].fill   = water[5]
cells['Al Rod Moderator Core 6'].fill   = water[6]
cells['Al Rod Moderator Core 7'].fill   = water[7]
cells['Al Rod Moderator Core 8'].fill   = water[8]
cells['Al Rod Moderator Core 9'].fill   = water[9]
cells['Al Rod Moderator Core 10'].fill  = water[10]

cells['B4C Rod Moderator Core 1'].fill  = water[1]
cells['B4C Rod Moderator Core 2'].fill  = water[2]
cells['B4C Rod Moderator Core 3'].fill  = water[3]
cells['B4C Rod Moderator Core 4'].fill  = water[4]
cells['B4C Rod Moderator Core 5'].fill  = water[5]
cells['B4C Rod Moderator Core 6'].fill  = water[6]
cells['B4C Rod Moderator Core 7'].fill  = water[7]
cells['B4C Rod Moderator Core 8'].fill  = water[8]
cells['B4C Rod Moderator Core 9'].fill  = water[9]
cells['B4C Rod Moderator Core 10'].fill = water[10]

cells['Reflector Core 1'].fill          = water[1]
cells['Reflector Core 2'].fill          = water[2]
cells['Reflector Core 3'].fill          = water[3]
cells['Reflector Core 4'].fill          = water[4]
cells['Reflector Core 5'].fill          = water[5]
cells['Reflector Core 6'].fill          = water[6]
cells['Reflector Core 7'].fill          = water[7]
cells['Reflector Core 8'].fill          = water[8]
cells['Reflector Core 9'].fill          = water[9]
cells['Reflector Core 10'].fill         = water[10]
