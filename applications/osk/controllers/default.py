# -*- coding: utf-8 -*-
# try something like
def index(): 
    pages = db().select(db.page.id,db.page.title,db.page.created_on,orderby=~db.page.created_on)
    return dict(pages=pages)

def user():
    return dict(form=auth())