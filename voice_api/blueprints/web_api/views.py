from flask import Blueprint,render_template

web_api=Blueprint('web_api',__name__)

@web_api.route('/web/ext-add/',methods=['POST'])
def ext_add():
    ext={
        'domain':'',
        'group':'',
        'extnumber':'',
        'password':'',
        'callgroup':''
    }
    return render_template('ext.xml',ext=ext)

# @web_api.route('/web/ext-del/',Methods=['POSt'])
# def hello():
#     return 'Hello WEBAPI'

# @web_api.route('/web/ext-list/',Methods=['POSt'])
# def hello():
#     return 'Hello WEBAPI'