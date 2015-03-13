# controllers/blog.py
def new():
    form = SQLFORM(db.entry)
    if form.accepts(request.vars,session):
        redirect(URL(r=request,f='index'))
    return dict(form=form)

def index():
		rows = db(db.entry.id>0).select(orderby=~db.entry.created_at)
		return dict(rows=rows)
