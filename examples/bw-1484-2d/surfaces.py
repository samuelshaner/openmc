import openmc

###############################################################################
#                       Create the OpenMC Surfaces
###############################################################################

# Instantiate ZCylinder surfaces
surfaces = {}
surfaces['Fuel OR']       = openmc.ZCylinder(x0=0, y0=0, R=0.515, name='Fuel OR')
surfaces['Fuel Clad IR']  = openmc.ZCylinder(x0=0, y0=0, R=0.522, name='Fuel Clad IR')
surfaces['Fuel Clad OR']  = openmc.ZCylinder(x0=0, y0=0, R=0.603, name='Fuel Clad OR')
surfaces['B4C Clad IR']   = openmc.ZCylinder(x0=0, y0=0, R=0.4675, name='B4C Clad IR')
surfaces['B4C Clad OR']   = openmc.ZCylinder(x0=0, y0=0, R=0.5565, name='B4C Clad OR')
surfaces['Threaded Al R'] = openmc.ZCylinder(x0=0, y0=0, R=0.635, name='Threaded Al R')

# Instantiate boundary surface
surfaces['Core x-min']       = openmc.XPlane(surface_id=2, x0=-1.636*39, name='Core x-min')
surfaces['Core x-max']       = openmc.XPlane(surface_id=3, x0= 1.636*39, name='Core x-max')
surfaces['Core y-min']       = openmc.YPlane(surface_id=4, y0=-1.636*39, name='Core y-min')
surfaces['Core y-max']       = openmc.YPlane(surface_id=5, y0= 1.636*39, name='Core y-max')

surfaces['Core x-min'].boundary_type       = 'vacuum'
surfaces['Core x-max'].boundary_type       = 'vacuum'
surfaces['Core y-min'].boundary_type       = 'vacuum'
surfaces['Core y-max'].boundary_type       = 'vacuum'
