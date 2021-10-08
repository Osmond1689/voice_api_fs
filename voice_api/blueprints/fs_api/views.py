from flask import Blueprint,render_template,request,make_response
from voice_api.blueprints.ext import Ext

fs_api=Blueprint('fs_api',__name__,template_folder='templates')

@fs_api.route('/api/auth-ext',methods=['POST'])
def auth_ext():
    r=request.form
    #print(r)
    sip_auth_username=r.get('user')
    domain=r.get('domain')
    if r.get('Event-Calling-Function')== 'switch_load_network_lists':
        response=make_response(render_template('404.xml'))
        response.headers['Content-Type'] = 'application/xml'
        return response
    elif r.get('Event-Calling-Function')=='config_sofia':
        response=make_response(render_template('404.xml'))
        response.headers['Content-Type'] = 'application/xml'
        return response
    else:
        #查询数据库返回xml
        try:
            ext=Ext.query({'domain':domain,'extnumber':sip_auth_username})
        except AttributeError:
            response=make_response(render_template('404.xml'))
            response.headers['Content-Type'] = 'application/xml'
            return response
        if ext['extnumber'] in ['1000','1001']:
            response=make_response(render_template('404.xml'))
            response.headers['Content-Type'] = 'application/xml'
            return response
        else:
            response=make_response(render_template('ext.xml',ext=ext))
            response.headers['Content-Type'] = 'application/xml'
            return response

@fs_api.route('/api/queue-info',methods=['POST'])
def queue_info():
    r=request
    queues=[{'name':'1003'},{'name':'1004'}]
    if r.values.get('key_value')=='callcenter.conf':
        response=make_response(render_template('callcenter.conf.xml',queues=queues))
        response.headers['Content-Type'] = 'application/xml'
        return response
    else:
        response=make_response(render_template('404.xml'))
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