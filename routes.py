routers = dict(
    BASE = dict(
        default_application = 'osk',
        default_controller = 'default',
        default_function = 'index'))

routes_in = (
  ('/$c/$f', '/osk/$c/$f'),
)

routes_out = (
  ('/osk/$c/$f', '/$c/$f'),
)