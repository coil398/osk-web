@auth.requires_login()
def index():
    images = db().select(db.image.ALL,orderby=~db.image.upload_on)
    return dict(images=images)

@auth.requires_login()
def upload():
    form = SQLFORM(db.image).process(next=URL('index'))
    return dict(form=form)

@auth.requires_login()
def show():
    image = db.image(request.args(0,cast=int)) or redirect(URL('index'))
    form = SQLFORM(db.image,image).process(
        next = URL('show',args=request.args))
    return dict(image=image,form=form)

def download():
    return response.download(request,db)