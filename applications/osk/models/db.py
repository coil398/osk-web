try:
    db = DAL('gae')
    session.connect(request,response,db)
except:
    db = DAL('sqlite://storage.db')

"""ユーザー認証設定"""
from gluon.tools import *
auth = Auth(db)
auth.define_tables(username=True)
"""auth.settings.actions_disabled.append('register')"""
crud = Crud(db)
"""ユーザー認証設定ここまで"""

"""データベース設定"""
"""記事設定"""
db.define_table('item',
    Field('title'),
    Field('body','text'),
    Field('created_on','datetime', default=request.now),
    Field('created_by','reference auth_user',default=auth.user_id),
    format = '%(title)s')

"""画像うpろだ"""
db.define_table('image',
    Field('title'),
    Field('file','upload'),
    Field('note','text'),
    Field('upload_on','datetime',default=request.now),
    Field('upload_by','reference auth_user',default=auth.user_id),
    format = '%(title)s')

db.item.title.requires = IS_NOT_EMPTY()
"""db.item.body.requires = IS_NOT_EMPTY()"""
db.item.created_by.readable = db.item.created_by.writable = False
db.item.created_on.readable = db.item.created_on.writable = False

db.image.title.requires = IS_NOT_EMPTY()
db.image.file.requires = IS_NOT_EMPTY()
db.image.upload_by.readable = db.image.upload_by.writable = False
db.image.upload_on.readable = db.image.upload_on.writable = False

"""データベース設定ここまで"""
