routers = dict(
    BASE = dict(
        default_application = 'osk',
        default_controller = 'home',
        default_function = 'index'))

routes_in = (
  ('/$c/$f', '/init/$c/$f'),
)

routes_out = (
  ('/init/$c/$f', '/$c/$f'),
)