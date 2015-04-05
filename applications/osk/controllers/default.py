# -*- coding: utf-8 -*-
# try something like
def index(): 
    if 
    items = db().select(db.item.ALL,orderby=~db.item.created_on)
    return dict(items=items)

def user():
    return dict(form=auth())