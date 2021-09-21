from . import web_api

@web_api.route('/webapi/hello',Methods=['GET','POSt'])
def hello():
    return 'Hello WEBAPI'