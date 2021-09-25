from . import fs_api


@fs_api.route('/api/click',Methods=['GET','POSt'])
def hello():
    return 'Hello FSAPI'

@fs_api.route('/fsapi/hello',Methods=['GET','POSt'])
def hello():
    return 'Hello FSAPI'

@fs_api.route('/fsapi/hello',Methods=['GET','POSt'])
def hello():
    return 'Hello FSAPI'

@fs_api.route('/fsapi/hello',Methods=['GET','POSt'])
def hello():
    return 'Hello FSAPI'