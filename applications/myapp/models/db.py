# models/dp.py

if request.env.web2py_runtime_gae:
    db = DAL('gae')

else:
    db = DAL('sqlite://storage.sqlite')

db.define_table('entry',
                Field('title','string',length=255,
                      notnull = True),
                Field('body','text'),
                Field('created_at','datetime',
                      default=request.now),
                Field('updated_at','datetime',
                      update=request.now,default=request.now))
