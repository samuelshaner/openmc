import openmc
from materials import pin_materials, water, moderator, poison_plate
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

cells['SS Sheet Cross SS Core 11']        = openmc.Cell(name='SS Sheet Cross SS Core 11')
cells['SS Sheet Horiz SS Core 11']        = openmc.Cell(name='SS Sheet Horiz SS Core 11')
cells['SS Sheet Verti SS Core 11']        = openmc.Cell(name='SS Sheet Verti SS Core 11')
cells['SS Sheet Cross Mod Core 11']       = openmc.Cell(name='SS Sheet Cross Mod Core 11')
cells['SS Sheet Horiz Mod Core 11']       = openmc.Cell(name='SS Sheet Horiz Mod Core 11')
cells['SS Sheet Verti Mod Core 11']       = openmc.Cell(name='SS Sheet Verti Mod Core 11')
cells['SS Sheet Cross SS Core 12']        = openmc.Cell(name='SS Sheet Cross SS Core 12')
cells['SS Sheet Horiz SS Core 12']        = openmc.Cell(name='SS Sheet Horiz SS Core 12')
cells['SS Sheet Verti SS Core 12']        = openmc.Cell(name='SS Sheet Verti SS Core 12')
cells['SS Sheet Cross Mod Core 12']       = openmc.Cell(name='SS Sheet Cross Mod Core 12')
cells['SS Sheet Horiz Mod Core 12']       = openmc.Cell(name='SS Sheet Horiz Mod Core 12')
cells['SS Sheet Verti Mod Core 12']       = openmc.Cell(name='SS Sheet Verti Mod Core 12')
cells['BAl Sheet Cross BAl Core 13']      = openmc.Cell(name='BAl Sheet Cross BAl Core 13')
cells['BAl Sheet Horiz BAl Core 13']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 13')
cells['BAl Sheet Verti BAl Core 13']      = openmc.Cell(name='BAl Sheet Verti BAl Core 13')
cells['BAl Sheet Cross Mod Core 13']      = openmc.Cell(name='BAl Sheet Cross Mod Core 13')
cells['BAl Sheet Horiz Mod Core 13']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 13')
cells['BAl Sheet Verti Mod Core 13']      = openmc.Cell(name='BAl Sheet Verti Mod Core 13')
cells['BAl Sheet Cross BAl Core 14']      = openmc.Cell(name='BAl Sheet Cross BAl Core 14')
cells['BAl Sheet Horiz BAl Core 14']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 14')
cells['BAl Sheet Verti BAl Core 14']      = openmc.Cell(name='BAl Sheet Verti BAl Core 14')
cells['BAl Sheet Cross Mod Core 14']      = openmc.Cell(name='BAl Sheet Cross Mod Core 14')
cells['BAl Sheet Horiz Mod Core 14']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 14')
cells['BAl Sheet Verti Mod Core 14']      = openmc.Cell(name='BAl Sheet Verti Mod Core 14')
cells['BAl Sheet Cross BAl Core 15']      = openmc.Cell(name='BAl Sheet Cross BAl Core 15')
cells['BAl Sheet Horiz BAl Core 15']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 15')
cells['BAl Sheet Verti BAl Core 15']      = openmc.Cell(name='BAl Sheet Verti BAl Core 15')
cells['BAl Sheet Cross Mod Core 15']      = openmc.Cell(name='BAl Sheet Cross Mod Core 15')
cells['BAl Sheet Horiz Mod Core 15']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 15')
cells['BAl Sheet Verti Mod Core 15']      = openmc.Cell(name='BAl Sheet Verti Mod Core 15')
cells['BAl Sheet Cross BAl Core 16']      = openmc.Cell(name='BAl Sheet Cross BAl Core 16')
cells['BAl Sheet Horiz BAl Core 16']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 16')
cells['BAl Sheet Verti BAl Core 16']      = openmc.Cell(name='BAl Sheet Verti BAl Core 16')
cells['BAl Sheet Cross Mod Core 16']      = openmc.Cell(name='BAl Sheet Cross Mod Core 16')
cells['BAl Sheet Horiz Mod Core 16']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 16')
cells['BAl Sheet Verti Mod Core 16']      = openmc.Cell(name='BAl Sheet Verti Mod Core 16')
cells['BAl Sheet Cross BAl Core 17']      = openmc.Cell(name='BAl Sheet Cross BAl Core 17')
cells['BAl Sheet Horiz BAl Core 17']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 17')
cells['BAl Sheet Verti BAl Core 17']      = openmc.Cell(name='BAl Sheet Verti BAl Core 17')
cells['BAl Sheet Cross Mod Core 17']      = openmc.Cell(name='BAl Sheet Cross Mod Core 17')
cells['BAl Sheet Horiz Mod Core 17']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 17')
cells['BAl Sheet Verti Mod Core 17']      = openmc.Cell(name='BAl Sheet Verti Mod Core 17')
cells['BAl Sheet Cross BAl Core 18']      = openmc.Cell(name='BAl Sheet Cross BAl Core 18')
cells['BAl Sheet Horiz BAl Core 18']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 18')
cells['BAl Sheet Verti BAl Core 18']      = openmc.Cell(name='BAl Sheet Verti BAl Core 18')
cells['BAl Sheet Cross Mod Core 18']      = openmc.Cell(name='BAl Sheet Cross Mod Core 18')
cells['BAl Sheet Horiz Mod Core 18']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 18')
cells['BAl Sheet Verti Mod Core 18']      = openmc.Cell(name='BAl Sheet Verti Mod Core 18')
cells['BAl Sheet Cross BAl Core 19']      = openmc.Cell(name='BAl Sheet Cross BAl Core 19')
cells['BAl Sheet Horiz BAl Core 19']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 19')
cells['BAl Sheet Verti BAl Core 19']      = openmc.Cell(name='BAl Sheet Verti BAl Core 19')
cells['BAl Sheet Cross Mod Core 19']      = openmc.Cell(name='BAl Sheet Cross Mod Core 19')
cells['BAl Sheet Horiz Mod Core 19']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 19')
cells['BAl Sheet Verti Mod Core 19']      = openmc.Cell(name='BAl Sheet Verti Mod Core 19')
cells['BAl Sheet Cross BAl Core 20']      = openmc.Cell(name='BAl Sheet Cross BAl Core 20')
cells['BAl Sheet Horiz BAl Core 20']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 20')
cells['BAl Sheet Verti BAl Core 20']      = openmc.Cell(name='BAl Sheet Verti BAl Core 20')
cells['BAl Sheet Cross Mod Core 20']      = openmc.Cell(name='BAl Sheet Cross Mod Core 20')
cells['BAl Sheet Horiz Mod Core 20']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 20')
cells['BAl Sheet Verti Mod Core 20']      = openmc.Cell(name='BAl Sheet Verti Mod Core 20')
cells['BAl Sheet Cross BAl Core 21']      = openmc.Cell(name='BAl Sheet Cross BAl Core 21')
cells['BAl Sheet Horiz BAl Core 21']      = openmc.Cell(name='BAl Sheet Horiz BAl Core 21')
cells['BAl Sheet Verti BAl Core 21']      = openmc.Cell(name='BAl Sheet Verti BAl Core 21')
cells['BAl Sheet Cross Mod Core 21']      = openmc.Cell(name='BAl Sheet Cross Mod Core 21')
cells['BAl Sheet Horiz Mod Core 21']      = openmc.Cell(name='BAl Sheet Horiz Mod Core 21')
cells['BAl Sheet Verti Mod Core 21']      = openmc.Cell(name='BAl Sheet Verti Mod Core 21')

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
cells['Reflector Core 11']                = openmc.Cell(name='Reflector Core 11')
cells['Reflector Core 12']                = openmc.Cell(name='Reflector Core 12')
cells['Reflector Core 13']                = openmc.Cell(name='Reflector Core 13')
cells['Reflector Core 14']                = openmc.Cell(name='Reflector Core 14')
cells['Reflector Core 15']                = openmc.Cell(name='Reflector Core 15')
cells['Reflector Core 16']                = openmc.Cell(name='Reflector Core 16')
cells['Reflector Core 17']                = openmc.Cell(name='Reflector Core 17')
cells['Reflector Core 18']                = openmc.Cell(name='Reflector Core 18')
cells['Reflector Core 19']                = openmc.Cell(name='Reflector Core 19')
cells['Reflector Core 20']                = openmc.Cell(name='Reflector Core 20')
cells['Reflector Core 21']                = openmc.Cell(name='Reflector Core 21')


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
cells['Fuel Rod Moderator Core 11']       = openmc.Cell(name='Fuel Rod Moderator Core 11')
cells['Fuel Rod Moderator Core 12']       = openmc.Cell(name='Fuel Rod Moderator Core 12')
cells['Fuel Rod Moderator Core 13']       = openmc.Cell(name='Fuel Rod Moderator Core 13')
cells['Fuel Rod Moderator Core 14']       = openmc.Cell(name='Fuel Rod Moderator Core 14')
cells['Fuel Rod Moderator Core 15']       = openmc.Cell(name='Fuel Rod Moderator Core 15')
cells['Fuel Rod Moderator Core 16']       = openmc.Cell(name='Fuel Rod Moderator Core 16')
cells['Fuel Rod Moderator Core 17']       = openmc.Cell(name='Fuel Rod Moderator Core 17')
cells['Fuel Rod Moderator Core 18']       = openmc.Cell(name='Fuel Rod Moderator Core 18')
cells['Fuel Rod Moderator Core 19']       = openmc.Cell(name='Fuel Rod Moderator Core 19')
cells['Fuel Rod Moderator Core 20']       = openmc.Cell(name='Fuel Rod Moderator Core 20')
cells['Fuel Rod Moderator Core 21']       = openmc.Cell(name='Fuel Rod Moderator Core 21')

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
cells['Al Rod Moderator Core 11']         = openmc.Cell(name='Al Rod Moderator Core 11')
cells['Al Rod Moderator Core 12']         = openmc.Cell(name='Al Rod Moderator Core 12')
cells['Al Rod Moderator Core 13']         = openmc.Cell(name='Al Rod Moderator Core 13')
cells['Al Rod Moderator Core 14']         = openmc.Cell(name='Al Rod Moderator Core 14')
cells['Al Rod Moderator Core 15']         = openmc.Cell(name='Al Rod Moderator Core 15')
cells['Al Rod Moderator Core 16']         = openmc.Cell(name='Al Rod Moderator Core 16')
cells['Al Rod Moderator Core 17']         = openmc.Cell(name='Al Rod Moderator Core 17')
cells['Al Rod Moderator Core 18']         = openmc.Cell(name='Al Rod Moderator Core 18')
cells['Al Rod Moderator Core 19']         = openmc.Cell(name='Al Rod Moderator Core 19')
cells['Al Rod Moderator Core 20']         = openmc.Cell(name='Al Rod Moderator Core 20')
cells['Al Rod Moderator Core 21']         = openmc.Cell(name='Al Rod Moderator Core 21')

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
cells['B4C Rod Moderator Core 11']        = openmc.Cell(name='B4C Rod Moderator Core 11')
cells['B4C Rod Moderator Core 12']        = openmc.Cell(name='B4C Rod Moderator Core 12')
cells['B4C Rod Moderator Core 13']        = openmc.Cell(name='B4C Rod Moderator Core 13')
cells['B4C Rod Moderator Core 14']        = openmc.Cell(name='B4C Rod Moderator Core 14')
cells['B4C Rod Moderator Core 15']        = openmc.Cell(name='B4C Rod Moderator Core 15')
cells['B4C Rod Moderator Core 16']        = openmc.Cell(name='B4C Rod Moderator Core 16')
cells['B4C Rod Moderator Core 17']        = openmc.Cell(name='B4C Rod Moderator Core 17')
cells['B4C Rod Moderator Core 18']        = openmc.Cell(name='B4C Rod Moderator Core 18')
cells['B4C Rod Moderator Core 19']        = openmc.Cell(name='B4C Rod Moderator Core 19')
cells['B4C Rod Moderator Core 20']        = openmc.Cell(name='B4C Rod Moderator Core 20')
cells['B4C Rod Moderator Core 21']        = openmc.Cell(name='B4C Rod Moderator Core 21')

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
cells['Core 11']                          = openmc.Cell(name='Core 11')
cells['Core 12']                          = openmc.Cell(name='Core 12')
cells['Core 13']                          = openmc.Cell(name='Core 13')
cells['Core 14']                          = openmc.Cell(name='Core 14')
cells['Core 15']                          = openmc.Cell(name='Core 15')
cells['Core 16']                          = openmc.Cell(name='Core 16')
cells['Core 17']                          = openmc.Cell(name='Core 17')
cells['Core 18']                          = openmc.Cell(name='Core 18')
cells['Core 19']                          = openmc.Cell(name='Core 19')
cells['Core 20']                          = openmc.Cell(name='Core 20')
cells['Core 21']                          = openmc.Cell(name='Core 21')

# Use surface half-spaces to define regions
cells['Fuel Rod Fuel'].region              = -surfaces['Fuel OR']
cells['Fuel Rod Gap'].region               = +surfaces['Fuel OR'] & -surfaces['Fuel Clad IR']
cells['Fuel Rod Clad'].region              = +surfaces['Fuel Clad IR'] & -surfaces['Fuel Clad OR']
cells['Al Rod Al'].region                  = -surfaces['Threaded Al R']
cells['B4C Rod B4C'].region                = -surfaces['B4C Clad IR']
cells['B4C Rod Clad'].region               = +surfaces['B4C Clad IR'] & -surfaces['B4C Clad OR']

cells['SS Sheet Cross SS Core 11'].region  = (+surfaces['SS Sheet x-min'] & -surfaces['SS Sheet x-max']) | \
                                             (+surfaces['SS Sheet y-min'] & -surfaces['SS Sheet y-max'])
cells['SS Sheet Horiz SS Core 11'].region  = (+surfaces['SS Sheet y-min'] & -surfaces['SS Sheet y-max'])
cells['SS Sheet Verti SS Core 11'].region  = (+surfaces['SS Sheet x-min'] & -surfaces['SS Sheet x-max'])
cells['SS Sheet Cross Mod Core 11'].region = ~cells['SS Sheet Cross SS Core 11'].region
cells['SS Sheet Horiz Mod Core 11'].region = ~cells['SS Sheet Horiz SS Core 11'].region
cells['SS Sheet Verti Mod Core 11'].region = ~cells['SS Sheet Verti SS Core 11'].region
cells['SS Sheet Cross SS Core 12'].region  = (+surfaces['SS Sheet x-min'] & -surfaces['SS Sheet x-max']) | \
                                             (+surfaces['SS Sheet y-min'] & -surfaces['SS Sheet y-max'])
cells['SS Sheet Horiz SS Core 12'].region  = (+surfaces['SS Sheet y-min'] & -surfaces['SS Sheet y-max'])
cells['SS Sheet Verti SS Core 12'].region  = (+surfaces['SS Sheet x-min'] & -surfaces['SS Sheet x-max'])
cells['SS Sheet Cross Mod Core 12'].region = ~cells['SS Sheet Cross SS Core 12'].region
cells['SS Sheet Horiz Mod Core 12'].region = ~cells['SS Sheet Horiz SS Core 12'].region
cells['SS Sheet Verti Mod Core 12'].region = ~cells['SS Sheet Verti SS Core 12'].region
cells['BAl Sheet Cross BAl Core 13'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 13'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 13'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 13'].region = ~cells['BAl Sheet Cross BAl Core 13'].region
cells['BAl Sheet Horiz Mod Core 13'].region = ~cells['BAl Sheet Horiz BAl Core 13'].region
cells['BAl Sheet Verti Mod Core 13'].region = ~cells['BAl Sheet Verti BAl Core 13'].region
cells['BAl Sheet Cross BAl Core 14'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 14'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 14'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 14'].region = ~cells['BAl Sheet Cross BAl Core 14'].region
cells['BAl Sheet Horiz Mod Core 14'].region = ~cells['BAl Sheet Horiz BAl Core 14'].region
cells['BAl Sheet Verti Mod Core 14'].region = ~cells['BAl Sheet Verti BAl Core 14'].region
cells['BAl Sheet Cross BAl Core 15'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 15'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 15'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 15'].region = ~cells['BAl Sheet Cross BAl Core 15'].region
cells['BAl Sheet Horiz Mod Core 15'].region = ~cells['BAl Sheet Horiz BAl Core 15'].region
cells['BAl Sheet Verti Mod Core 15'].region = ~cells['BAl Sheet Verti BAl Core 15'].region
cells['BAl Sheet Cross BAl Core 16'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 16'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 16'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 16'].region = ~cells['BAl Sheet Cross BAl Core 16'].region
cells['BAl Sheet Horiz Mod Core 16'].region = ~cells['BAl Sheet Horiz BAl Core 16'].region
cells['BAl Sheet Verti Mod Core 16'].region = ~cells['BAl Sheet Verti BAl Core 16'].region
cells['BAl Sheet Cross BAl Core 17'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 17'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 17'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 17'].region = ~cells['BAl Sheet Cross BAl Core 17'].region
cells['BAl Sheet Horiz Mod Core 17'].region = ~cells['BAl Sheet Horiz BAl Core 17'].region
cells['BAl Sheet Verti Mod Core 17'].region = ~cells['BAl Sheet Verti BAl Core 17'].region
cells['BAl Sheet Cross BAl Core 18'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 18'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 18'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 18'].region = ~cells['BAl Sheet Cross BAl Core 18'].region
cells['BAl Sheet Horiz Mod Core 18'].region = ~cells['BAl Sheet Horiz BAl Core 18'].region
cells['BAl Sheet Verti Mod Core 18'].region = ~cells['BAl Sheet Verti BAl Core 18'].region
cells['BAl Sheet Cross BAl Core 19'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 19'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 19'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 19'].region = ~cells['BAl Sheet Cross BAl Core 19'].region
cells['BAl Sheet Horiz Mod Core 19'].region = ~cells['BAl Sheet Horiz BAl Core 19'].region
cells['BAl Sheet Verti Mod Core 19'].region = ~cells['BAl Sheet Verti BAl Core 19'].region
cells['BAl Sheet Cross BAl Core 20'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 20'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 20'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 20'].region = ~cells['BAl Sheet Cross BAl Core 20'].region
cells['BAl Sheet Horiz Mod Core 20'].region = ~cells['BAl Sheet Horiz BAl Core 20'].region
cells['BAl Sheet Verti Mod Core 20'].region = ~cells['BAl Sheet Verti BAl Core 20'].region
cells['BAl Sheet Cross BAl Core 21'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max']) | \
                                               (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Horiz BAl Core 21'].region  = (+surfaces['BAl Sheet y-min'] & -surfaces['BAl Sheet y-max'])
cells['BAl Sheet Verti BAl Core 21'].region  = (+surfaces['BAl Sheet x-min'] & -surfaces['BAl Sheet x-max'])
cells['BAl Sheet Cross Mod Core 21'].region = ~cells['BAl Sheet Cross BAl Core 21'].region
cells['BAl Sheet Horiz Mod Core 21'].region = ~cells['BAl Sheet Horiz BAl Core 21'].region
cells['BAl Sheet Verti Mod Core 21'].region = ~cells['BAl Sheet Verti BAl Core 21'].region


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
cells['Fuel Rod Moderator Core 11'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 12'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 13'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 14'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 15'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 16'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 17'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 18'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 19'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 20'].region = +surfaces['Fuel Clad OR']
cells['Fuel Rod Moderator Core 21'].region = +surfaces['Fuel Clad OR']

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
cells['Al Rod Moderator Core 11'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 12'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 13'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 14'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 15'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 16'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 17'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 18'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 19'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 20'].region   = +surfaces['Threaded Al R']
cells['Al Rod Moderator Core 21'].region   = +surfaces['Threaded Al R']

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
cells['B4C Rod Moderator Core 11'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 12'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 13'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 14'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 15'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 16'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 17'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 18'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 19'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 20'].region  = +surfaces['B4C Clad OR']
cells['B4C Rod Moderator Core 21'].region  = +surfaces['B4C Clad OR']

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
cells['Core 11'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 12'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 13'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 14'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 15'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 16'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 17'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 18'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 19'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 20'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 20'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 21'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
                                              -surfaces['Core x-max'] & -surfaces['Core y-max']
cells['Core 21'].region                     = +surfaces['Core x-min'] & +surfaces['Core y-min'] & \
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
cells['Fuel Rod Moderator Core 10'].fill = moderator[10]
cells['Fuel Rod Moderator Core 11'].fill = moderator[11]
cells['Fuel Rod Moderator Core 12'].fill = moderator[12]
cells['Fuel Rod Moderator Core 13'].fill = moderator[13]
cells['Fuel Rod Moderator Core 14'].fill = moderator[14]
cells['Fuel Rod Moderator Core 15'].fill = moderator[15]
cells['Fuel Rod Moderator Core 16'].fill = moderator[16]
cells['Fuel Rod Moderator Core 17'].fill = moderator[17]
cells['Fuel Rod Moderator Core 18'].fill = moderator[18]
cells['Fuel Rod Moderator Core 19'].fill = moderator[19]
cells['Fuel Rod Moderator Core 20'].fill = moderator[20]
cells['Fuel Rod Moderator Core 21'].fill = moderator[21]

cells['Al Rod Moderator Core 1'].fill   = water[1]
cells['Al Rod Moderator Core 2'].fill   = water[2]
cells['Al Rod Moderator Core 3'].fill   = water[3]
cells['Al Rod Moderator Core 4'].fill   = water[4]
cells['Al Rod Moderator Core 5'].fill   = water[5]
cells['Al Rod Moderator Core 6'].fill   = water[6]
cells['Al Rod Moderator Core 7'].fill   = water[7]
cells['Al Rod Moderator Core 8'].fill   = water[8]
cells['Al Rod Moderator Core 9'].fill   = water[9]
cells['Al Rod Moderator Core 10'].fill  = moderator[10]
cells['Al Rod Moderator Core 11'].fill  = moderator[11]
cells['Al Rod Moderator Core 12'].fill  = moderator[12]
cells['Al Rod Moderator Core 13'].fill  = moderator[13]
cells['Al Rod Moderator Core 14'].fill  = moderator[14]
cells['Al Rod Moderator Core 15'].fill  = moderator[15]
cells['Al Rod Moderator Core 16'].fill  = moderator[16]
cells['Al Rod Moderator Core 17'].fill  = moderator[17]
cells['Al Rod Moderator Core 18'].fill  = moderator[18]
cells['Al Rod Moderator Core 19'].fill  = moderator[19]
cells['Al Rod Moderator Core 20'].fill  = moderator[20]
cells['Al Rod Moderator Core 21'].fill  = moderator[21]

cells['B4C Rod Moderator Core 1'].fill  = water[1]
cells['B4C Rod Moderator Core 2'].fill  = water[2]
cells['B4C Rod Moderator Core 3'].fill  = water[3]
cells['B4C Rod Moderator Core 4'].fill  = water[4]
cells['B4C Rod Moderator Core 5'].fill  = water[5]
cells['B4C Rod Moderator Core 6'].fill  = water[6]
cells['B4C Rod Moderator Core 7'].fill  = water[7]
cells['B4C Rod Moderator Core 8'].fill  = water[8]
cells['B4C Rod Moderator Core 9'].fill  = water[9]
cells['B4C Rod Moderator Core 10'].fill = moderator[10]
cells['B4C Rod Moderator Core 11'].fill = moderator[11]
cells['B4C Rod Moderator Core 12'].fill = moderator[12]
cells['B4C Rod Moderator Core 13'].fill = moderator[13]
cells['B4C Rod Moderator Core 14'].fill = moderator[14]
cells['B4C Rod Moderator Core 15'].fill = moderator[15]
cells['B4C Rod Moderator Core 16'].fill = moderator[16]
cells['B4C Rod Moderator Core 17'].fill = moderator[17]
cells['B4C Rod Moderator Core 18'].fill = moderator[18]
cells['B4C Rod Moderator Core 19'].fill = moderator[19]
cells['B4C Rod Moderator Core 20'].fill = moderator[20]
cells['B4C Rod Moderator Core 21'].fill = moderator[21]

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
cells['Reflector Core 11'].fill         = water[11]
cells['Reflector Core 12'].fill         = water[12]
cells['Reflector Core 13'].fill         = water[13]
cells['Reflector Core 14'].fill         = water[14]
cells['Reflector Core 15'].fill         = water[15]
cells['Reflector Core 16'].fill         = water[16]
cells['Reflector Core 17'].fill         = water[17]
cells['Reflector Core 18'].fill         = water[18]
cells['Reflector Core 19'].fill         = water[19]
cells['Reflector Core 20'].fill         = water[20]
cells['Reflector Core 21'].fill         = water[21]

cells['SS Sheet Cross SS Core 11'].fill       = pin_materials['SS']
cells['SS Sheet Horiz SS Core 11'].fill       = pin_materials['SS']
cells['SS Sheet Verti SS Core 11'].fill       = pin_materials['SS']
cells['SS Sheet Cross Mod Core 11'].fill      = water[11]
cells['SS Sheet Horiz Mod Core 11'].fill      = water[11]
cells['SS Sheet Verti Mod Core 11'].fill      = water[11]
cells['SS Sheet Cross SS Core 12'].fill       = pin_materials['SS']
cells['SS Sheet Horiz SS Core 12'].fill       = pin_materials['SS']
cells['SS Sheet Verti SS Core 12'].fill       = pin_materials['SS']
cells['SS Sheet Cross Mod Core 12'].fill      = water[12]
cells['SS Sheet Horiz Mod Core 12'].fill      = water[12]
cells['SS Sheet Verti Mod Core 12'].fill      = water[12]
cells['BAl Sheet Cross BAl Core 13'].fill     = poison_plate[13]
cells['BAl Sheet Horiz BAl Core 13'].fill     = poison_plate[13]
cells['BAl Sheet Verti BAl Core 13'].fill     = poison_plate[13]
cells['BAl Sheet Cross Mod Core 13'].fill     = water[13]
cells['BAl Sheet Horiz Mod Core 13'].fill     = water[13]
cells['BAl Sheet Verti Mod Core 13'].fill     = water[13]
cells['BAl Sheet Cross BAl Core 14'].fill     = poison_plate[14]
cells['BAl Sheet Horiz BAl Core 14'].fill     = poison_plate[14]
cells['BAl Sheet Verti BAl Core 14'].fill     = poison_plate[14]
cells['BAl Sheet Cross Mod Core 14'].fill     = water[14]
cells['BAl Sheet Horiz Mod Core 14'].fill     = water[14]
cells['BAl Sheet Verti Mod Core 14'].fill     = water[14]
cells['BAl Sheet Cross BAl Core 15'].fill     = poison_plate[15]
cells['BAl Sheet Horiz BAl Core 15'].fill     = poison_plate[15]
cells['BAl Sheet Verti BAl Core 15'].fill     = poison_plate[15]
cells['BAl Sheet Cross Mod Core 15'].fill     = water[15]
cells['BAl Sheet Horiz Mod Core 15'].fill     = water[15]
cells['BAl Sheet Verti Mod Core 15'].fill     = water[15]
cells['BAl Sheet Cross BAl Core 16'].fill     = poison_plate[16]
cells['BAl Sheet Horiz BAl Core 16'].fill     = poison_plate[16]
cells['BAl Sheet Verti BAl Core 16'].fill     = poison_plate[16]
cells['BAl Sheet Cross Mod Core 16'].fill     = water[16]
cells['BAl Sheet Horiz Mod Core 16'].fill     = water[16]
cells['BAl Sheet Verti Mod Core 16'].fill     = water[16]
cells['BAl Sheet Cross BAl Core 17'].fill     = poison_plate[17]
cells['BAl Sheet Horiz BAl Core 17'].fill     = poison_plate[17]
cells['BAl Sheet Verti BAl Core 17'].fill     = poison_plate[17]
cells['BAl Sheet Cross Mod Core 17'].fill     = water[17]
cells['BAl Sheet Horiz Mod Core 17'].fill     = water[17]
cells['BAl Sheet Verti Mod Core 17'].fill     = water[17]
cells['BAl Sheet Cross BAl Core 18'].fill     = poison_plate[18]
cells['BAl Sheet Horiz BAl Core 18'].fill     = poison_plate[18]
cells['BAl Sheet Verti BAl Core 18'].fill     = poison_plate[18]
cells['BAl Sheet Cross Mod Core 18'].fill     = water[18]
cells['BAl Sheet Horiz Mod Core 18'].fill     = water[18]
cells['BAl Sheet Verti Mod Core 18'].fill     = water[18]
cells['BAl Sheet Cross BAl Core 19'].fill     = poison_plate[19]
cells['BAl Sheet Horiz BAl Core 19'].fill     = poison_plate[19]
cells['BAl Sheet Verti BAl Core 19'].fill     = poison_plate[19]
cells['BAl Sheet Cross Mod Core 19'].fill     = water[19]
cells['BAl Sheet Horiz Mod Core 19'].fill     = water[19]
cells['BAl Sheet Verti Mod Core 19'].fill     = water[19]
cells['BAl Sheet Cross BAl Core 20'].fill     = poison_plate[20]
cells['BAl Sheet Horiz BAl Core 20'].fill     = poison_plate[20]
cells['BAl Sheet Verti BAl Core 20'].fill     = poison_plate[20]
cells['BAl Sheet Cross Mod Core 20'].fill     = water[20]
cells['BAl Sheet Horiz Mod Core 20'].fill     = water[20]
cells['BAl Sheet Verti Mod Core 20'].fill     = water[20]
cells['BAl Sheet Cross BAl Core 21'].fill     = poison_plate[21]
cells['BAl Sheet Horiz BAl Core 21'].fill     = poison_plate[21]
cells['BAl Sheet Verti BAl Core 21'].fill     = poison_plate[21]
cells['BAl Sheet Cross Mod Core 21'].fill     = water[21]
cells['BAl Sheet Horiz Mod Core 21'].fill     = water[21]
cells['BAl Sheet Verti Mod Core 21'].fill     = water[21]
