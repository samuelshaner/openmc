import openmc

###############################################################################
#                 Create dictionary of common surfaces
###############################################################################

surfaces = {}

# Instantiate ZCylinder surfaces
surfaces['Fuel x-max'] = openmc.XPlane(surface_id=1 , x0=15.0, name='Fuel x-max')
surfaces['Fuel y-max'] = openmc.YPlane(surface_id=2 , y0=15.0, name='Fuel y-max')
surfaces['Fuel z-max'] = openmc.ZPlane(surface_id=3 , z0=15.0, name='Fuel z-max')

surfaces['Core x-min'] = openmc.XPlane(surface_id=4 , x0= 0.0, name='Core x-min')
surfaces['Core y-min'] = openmc.YPlane(surface_id=5 , y0= 0.0, name='Core y-min')
surfaces['Core z-min'] = openmc.ZPlane(surface_id=6 , z0= 0.0, name='Core z-min')
surfaces['Core x-max'] = openmc.XPlane(surface_id=7 , x0=25.0, name='Core x-max')
surfaces['Core y-max'] = openmc.YPlane(surface_id=8 , y0=25.0, name='Core y-max')
surfaces['Core z-max'] = openmc.ZPlane(surface_id=9 , z0=25.0, name='Core z-max')

surfaces['Void x-max'] = openmc.XPlane(surface_id=10, x0=20.0, name='Void x-max')
surfaces['Void y-max'] = openmc.YPlane(surface_id=11, y0= 5.0, name='Void y-max')

surfaces['Core x-min'].boundary_type = 'reflective'
surfaces['Core y-min'].boundary_type = 'reflective'
surfaces['Core z-min'].boundary_type = 'reflective'
surfaces['Core x-max'].boundary_type = 'vacuum'
surfaces['Core y-max'].boundary_type = 'vacuum'
surfaces['Core z-max'].boundary_type = 'vacuum'
