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
    else:
        pageEnd = page*10+10
    return dict(page=page,pageEnd=pageEnd,items=items)

def user():
    return dict(form=auth())

@auth.requires_login()
def create():
    form = SQLFORM(db.item).process()
    return dict(form=form)

@auth.requires_login()
def edit():
    this_page = db.item(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.item,this_page).process(
        next = URL('index'))
    return dict(form=form)

@auth.requires_membership('administrator')
def manageItem():
    grid = SQLFORM.smartgrid(db.item,linked_tables=['post'])
    return dict(grid=grid)

@auth.requires_membership('administrator')
def manageUser():
    grid = SQLFORM.smartgrid(db.auth_user,linked_tables=['post'])
    return dict(grid=grid)

@auth.requires_membership('administrator')
def manageMembership():
    grid = SQLFORM.smartgrid(db.auth_membership,linked_tables=['post'])
    return dict(grid=grid)

