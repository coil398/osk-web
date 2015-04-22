@auth.requires_login()
def index():
    images = db().select(db.image.ALL,orderby=~db.image.upload_on)
    if request.args(0) > 0:
        page=request.args(0,cast=int)
    else:
        page=0
    if page*10+10 > len(images):
        pageEnd = len(images)
    else:
        pageEnd = page*10+10
    return dict(page=page,pageEnd=pageEnd,images=images)

@auth.requires_login()
def upload():
    form = SQLFORM(db.image).process()
    return dict(form=form)

@auth.requires_login()
def show():
    image = db.image(request.args(0,cast=int)) or redirect(URL('index'))
    upload_by = db.auth_user(db.auth_user.id==image.upload_by)['username']
    form = SQLFORM(db.image,image).process(
        next = URL('show',args=request.args))
    return dict(upload_by=upload_by,image=image,form=form)

def download():
    return response.download(request,db)