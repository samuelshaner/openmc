import openmc

###############################################################################
#                 Create dictionary of common surfaces
###############################################################################

surfaces = {}

# Instantiate ZCylinder surfaces
surfaces['Core x-max'] = openmc.XPlane(surface_id=1 , x0=15.0, name='Core x-max')
surfaces['Core y-max'] = openmc.YPlane(surface_id=2 , y0=15.0, name='Core y-max')
surfaces['Core z-max'] = openmc.ZPlane(surface_id=3 , z0=15.0, name='Core z-max')

surfaces['Root x-min'] = openmc.XPlane(surface_id=4 , x0= 0.0, name='Root x-min')
surfaces['Root y-min'] = openmc.YPlane(surface_id=5 , y0= 0.0, name='Root y-min')
surfaces['Root z-min'] = openmc.ZPlane(surface_id=6 , z0= 0.0, name='Root z-min')
surfaces['Root x-max'] = openmc.XPlane(surface_id=7 , x0=25.0, name='Root x-max')
surfaces['Root y-max'] = openmc.YPlane(surface_id=8 , y0=25.0, name='Root y-max')
surfaces['Root z-max'] = openmc.ZPlane(surface_id=9 , z0=25.0, name='Root z-max')

surfaces['Void x-max'] = openmc.XPlane(surface_id=10, x0=20.0, name='Void x-max')
surfaces['Void y-max'] = openmc.YPlane(surface_id=11, y0= 5.0, name='Void y-max')

surfaces['Root x-min'].boundary_type = 'reflective'
surfaces['Root y-min'].boundary_type = 'reflective'
surfaces['Root z-min'].boundary_type = 'reflective'
surfaces['Root x-max'].boundary_type = 'vacuum'
surfaces['Root y-max'].boundary_type = 'vacuum'
surfaces['Root z-max'].boundary_type = 'vacuum'
