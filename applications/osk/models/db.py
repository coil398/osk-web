try:
    db = DAL('gae')
    session.connect(request,response,db)
except:
    db = DAL('sqlite://storage.db')

"""ユーザー認証設定"""
from gluon.tools import *
auth = Auth(db)
auth.define_tables()
crud = Crud(db)

"""ユーザー認証設定ここまで"""

"""データベース設定"""
db.define_table('page',
   Field('title'),
   Field('body','text'),
   Field('created_on','datetime', default=request.now),
   Field('created_by','reference auth_user',default=auth.user_id),
   format = '%(title)s')

db.page.title.requires = IS_NOT_EMPTY()
"""db.page.body.requires = IS_NOT_EMPTY()"""
db.page.created_by.readable = db.page.created_by.writable = False
db.page.created_on.readable = db.page.created_on.writable = False

"""データベース設定ここまで"""
