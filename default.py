def index():
    response.menu = []
    return dict()

def subject():
    response.menu = []
    return dict()

def alphabetically():
    response.menu = []
    return dict()

def keywords():
    response.menu = []
    return dict()

def libdbs():
    grids = []
    messages = []
    messages.append('Grid')
    libGrid = SQLFORM.grid(db.libdb, fields=(db.libdb.title,db.libdb.subject,db.libdb.description,db.libdb.url), create=False,editable=False,deletable=False,paginate=20,searchable=True, maxtextlength=1000, exportclasses=dict(tsv=False, xml=False, html=False, json=False, tsv_with_hidden_cols=False, csv_with_hidden_cols=False), details=False,csv=False, links = [lambda row: A('View ', _href=row.url, _target="_blank", _style="display:block;color:#fff;border-radius:3px;background-color:#337ab7;text-align:center;")])
    grids.append(libGrid)
    return dict(grid=libGrid, messages=messages)

@auth.requires_membership('Library-Admins')
def admin():
    response.menu = []
    lib = []
    libStr = ",".join(lib)
    libID = db.libdb.insert(subject=request.vars.subject, title=request.vars.title,description=request.vars.description,url=request.vars.url)
    return dict()


@auth.requires_membership('Library-Admins')
def adminlibdbs():
    grids = []
    messages = []
    messages.append('Grid')
    libGrid = SQLFORM.grid(db.libdb, fields=(db.libdb.title,db.libdb.subject,db.libdb.description,db.libdb.url), create=False,editable=True,deletable=True,paginate=20,searchable=True, maxtextlength=1000, exportclasses=dict(tsv=False, xml=False, html=False, json=False, tsv_with_hidden_cols=False, csv_with_hidden_cols=False), details=False,csv=False, links = [lambda row: A('View ', _href=row.url, _target="_blank", _style="display:block;color:#fff;border-radius:3px;background-color:#337ab7;text-align:center;")])
    grids.append(libGrid)
    return dict(grid=libGrid, messages=messages)



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
