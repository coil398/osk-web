try:
    db = DAL('gae')
    session.connect(request,response,db)
except:
    db = DAL('sqlite://storage.db')
