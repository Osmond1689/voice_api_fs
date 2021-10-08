from flask import Blueprint,render_template,request
#from werkzeug.local import Local
from voice_api.blueprints.web_api.service_gs import Send_commands
import _thread
from .md5_token import encrypt_md5
from .aes_models import AES_ENCRYPT
from flask import current_app
from voice_api.blueprints.ext import Ext

web_api=Blueprint('web_api',__name__)

return_data={}

def send_command(crm_uuid,extensin_number,customer_number,product_code):
    new_send_commands=Send_commands(crm_uuid,extensin_number,customer_number,product_code)
    new_send_commands.send_call()
    # return_data['data']=new_send_commands.job_status

@web_api.route('/web/ext-add/',methods=['POST'])
def ext_add():
    r_token=request.json.get('token')
    if r_token in encrypt_md5('DIANXIAOheYUYIN@'):
        r_data=request.json.get('data')
        '''
        {
			"token":"97d5fc0bdfc499fc8a008199cab1be53",
			"data":[{
                'domain':domain,
                'group':'default',
                'extnumber':sip_auth_username,
                'password':'123456',
                'callgroup':'default',
                'extname':'osmond'
            }]
		}
        '''
        try:
            Ext.add(r_data)
        except Exception as e:
            current_app.logger.debug("数据库操作失败：%s",e)
            return_data['msg']='Voice abnormal, Please contact the Voice engineer'
            return return_data,500
        else:
            return_data['msg']='Add OK'
            return return_data,200
    else:
        return_data['msg']='Auth Fail'
        return return_data,401

@web_api.route('/web/ext-rm/',methods=['POST'])
def ext_rm():
    r_token=request.json.get('token')
    if r_token in encrypt_md5('DIANXIAOheYUYIN@'):
        r_data=request.json.get('data')
        '''
        {
			"token":"97d5fc0bdfc499fc8a008199cab1be53",
			"data":[{
                'domain':domain,
                'extnumber':sip_auth_username
            }]
		}
        '''
        try:
            Ext.remove(r_data)
        except Exception as e:
            current_app.logger.debug("数据库操作失败：%s",e)
            return_data['msg']='Voice abnormal, Please contact the Voice engineer'
            return return_data,500
        else:
            return_data['msg']='Remove OK'
            return return_data,200
    else:
        return_data['msg']='Auth Fail'
        return return_data,401

@web_api.route('/web/ext-list/',methods=['POST'])
def ext_list():
    r_token=request.json.get('token')
    if r_token in encrypt_md5('DIANXIAOheYUYIN@'):
        r_data=request.json.get('data')
        '''
        {
			"token":"36ad10c7b8ded102658aeb4b241f48cc",
			"data":
            {
            "domain":"172.31.24.240",
            "group":"default"
            }
		}
        '''
        try:
            list=Ext.query(r_data)
        except Exception as e:
            current_app.logger.debug("数据库操作失败：%s",e)
            return_data['msg']='Voice abnormal, Please contact the Voice engineer'
            return return_data,500
        else:
            return_data['msg']='Query OK'
            return_data['data']=list
            return return_data,200
    else:
        return_data['msg']='Auth Fail'
        return return_data,401

@web_api.route('/web/ext-update/',methods=['POST'])
def ext_update():
    r_token=request.json.get('token')
    if r_token in encrypt_md5('DIANXIAOheYUYIN@'):
        r_data=request.json.get('data')
        '''
        {
			"token":"97d5fc0bdfc499fc8a008199cab1be53",
			"data":[{
                'domain':domain,
                'extnumber':sip_auth_username
            }]
		}
        '''
        try:
            Ext.change(r_data)
        except Exception as e:
            current_app.logger.debug("数据库操作失败：%s",e)
            return_data['msg']='Voice abnormal, Please contact the Voice engineer'
            return return_data,500
        else:
            return_data['msg']='Update OK'
            return return_data,200
    else:
        return_data['msg']='Auth Fail'
        return return_data,401

@web_api.route('/web/click-on-call/',methods=['POST'])
def click_on_call():
    r_token=request.json.get('token')
    if r_token in encrypt_md5('DIANXIAOheYUYIN@'):
        r_json=request.json.get('data')
        crm_uuid=r_json.get('crm_uuid')
        extensin_number=r_json.get('extensin_number')
        
        customer_number_encrypt=r_json.get('customer_number')
        if customer_number_encrypt:
            a=AES_ENCRYPT()
            customer_number=(a.decrypt(customer_number_encrypt)).decode('UTF-8')

        product_code=r_json.get('product_code')
        #call_type=r_json.get('call_type')
        #if 1:5t  
        if crm_uuid and extensin_number and customer_number and product_code:
            #异步调用ESL
            try:
                _thread.start_new_thread(send_command,(crm_uuid,extensin_number,customer_number,product_code))
            except Exception as e:
                current_app.logger.debug("连接ESL失败：%s",e)
                return_data['msg']='Voice abnormal, Please contact the Voice engineer'
                return return_data,500
            else:
                current_app.logger.info("接口调用成功:crm_uuid：%s，extensin_number：%s，customer_number： %s，product_code：%s",crm_uuid,extensin_number,customer_number,product_code)
                return_data['msg']='Call OK'
                return return_data,200
            #new_send_commands=Send_commands(crm_uuid,extensin_number,customer_number,product_code)
            #new_send_commands.send_call()
            #return_data['data']=new_send_commands.job_status
        else:
            return_data['msg']='The parameter is wrong'
            return return_data,500
    else:
        return_data['msg']='Auth Fail'
        return return_data,401
    

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