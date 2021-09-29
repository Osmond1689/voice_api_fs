from flask import Blueprint,render_template,request
from werkzeug.local import Local

web_api=Blueprint('web_api',__name__)

return_json=Local()
return_json.data={'msg':'','data':[]}

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

@web_api.route('/web/click-on-call/',methods=['POST'])
def click_on_call():
    r_json=request.json.get('data')
    crmuuid=r_json.get('crmuuid')
    extensin_number=r_json.get('extensin_number')
    customer_number=r_json.get('customer_number')
    product_code=r_json.get('product_code')
    call_type=r_json.get('call_type')
    if crmuuid and extensin_number and customer_number and product_code and call_type:
        pass#调用ESL
    else:
        return_json.data['msg']='The parameter is wrong'
        return return_json.data
    return_json.data['msg']='Call OK'
    return return_json.data

@web_api.route('/web/queue-out-call/',methods=['POST'])
def queue_out_call():
    '''
    队列名称
    客户列表
    并发数量
    接听策略
    '''
    pass

@web_api.route('/web/out-queue-add/',methods=['POST'])
def out_queue_add():
    pass

@web_api.route('/web/out-queue-del/',methods=['POST'])
def out_queue_del():
    pass

@web_api.route('/web/out-queue-list/',methods=['POST'])
def out_queue_list():
    pass
# @web_api.route('/web/ext-del/',Methods=['POSt'])
# def hello():
#     return 'Hello WEBAPI'

# @web_api.route('/web/ext-list/',Methods=['POSt'])
# def hello():
#     return 'Hello WEBAPI'