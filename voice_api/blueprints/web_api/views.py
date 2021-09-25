from . import web_api

@web_api.route('/web/ext-add/',Methods=['POSt'])
def hello():
    return 'Hello WEBAPI'

@web_api.route('/web/ext-del/',Methods=['POSt'])
def hello():
    return 'Hello WEBAPI'

@web_api.route('/web/ext-list/',Methods=['POSt'])
def hello():
    return 'Hello WEBAPI'