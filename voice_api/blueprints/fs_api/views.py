from flask import Blueprint,render_template,request,make_response

fs_api=Blueprint('fs_api',__name__,template_folder='templates')

@fs_api.route('/api/auth-ext',methods=['POST'])
def auth_ext():
    r=request.form
    #print(r)
    sip_auth_username=r.get('sip_auth_username')
    domain=r.get('domain')
    #查询数据库返回xml
    ext={
        'domain':domain,
        'group':'default',
        'extnumber':sip_auth_username,
        'password':'123456',
        'callgroup':'default'
    }
    response=make_response(render_template('ext.xml',ext=ext))
    response.headers['Content-Type'] = 'application/xml'
    return response

# @fs_api.route('/fsapi/hello',Methods=['POST'])
# def hello():
#     return 'Hello FSAPI'

# @fs_api.route('/fsapi/hello',Methods=['POST'])
# def hello():
#     return 'Hello FSAPI'

# @fs_api.route('/fsapi/hello',Methods=['POST'])
# def hello():
#     return 'Hello FSAPI'