# -*- coding: utf-8 -*-
# try something like
def index(): 
    items = db().select(db.item.ALL,orderby=~db.item.created_on)
    if request.args(0) > 0:
        page = request.args(0,cast=int)
    else:
        page = 0
    if page*10+10 > len(items):
        pageEnd = len(items)
    return dict(page=page,pageEnd=pageEnd,items=items)

def user():
    return dict(form=auth())