from voice_api.models.ext_info import Ext_info
from voice_api.models import db
from flask import current_app
class Ext():
    '''
    ext={
            'domain':domain,
            'group':'default',
            'extnumber':sip_auth_username,
            'password':'123456',
            'callgroup':'default',
            'extname':'osmond'
        }
    '''
    @staticmethod
    def add(ext_info_list):#分机信息map组成列表
        add_list=[]
        for i in ext_info_list:
            if not i.get('domain'):
                i['domain']=current_app.config['LOCAL_IPV4']
            if not i.get('group'):
                i['group']='default'
            if not i.get('callgroup'):
                i['callgroup']='default'
            if not i.get('extname'):
                i['extname']=i['extnumber']

            add_list.append(Ext_info(domain=i['domain'],group=i['group'],extnumber=i['extnumber'],password=i['password'],callgroup=i['callgroup'],extname=i['extname']))
            current_app.logger.info("分机添加接口调用成功:%s:%s@%s",i['extname'],i['extnumber'],i['domain'])
        with Ext_info.auto_commit(db):
            db.session.add_all(add_list)

    @staticmethod
    def remove(ext_info_list):#分机号,doamin组成的map 列表
        with Ext_info.auto_commit(db):
            for i in ext_info_list:
                if not i.get('domain'):
                    i['domain']=current_app.config['LOCAL_IPV4']
                a=Ext_info.query.filter(Ext_info.domain==i['domain'],Ext_info.extnumber==i['extnumber']).first()
                db.session.delete(a)
        
    @staticmethod
    def change(ext_info_list):#分机号,doamin组成的map 列表
        with Ext_info.auto_commit(db):
            for i in ext_info_list:
                if not i.get('domain'):
                    i['domain']=current_app.config['LOCAL_IPV4']
                if not i.get('group'):
                    i['group']='default'
                if not i.get('callgroup'):
                    i['callgroup']='default'
                #密码和分机名必传，可以传原值
                Ext_info.query.filter(Ext_info.domain==i['domain'],Ext_info.extnumber==i['extnumber']).update({'group':i['group'],'password':i['password'],'callgroup':i['callgroup'],'extname':i['extname']})
                
    @staticmethod
    def query(ext_info):#分机号,doamin,group,extname组成的map
        if not ext_info.get('domain'):
            ext_info.domain=current_app.config['LOCAL_IPV4']
        if not ext_info.get('group'):
            query_result=Ext_info.query.filter(Ext_info.domain==ext_info['domain'],Ext_info.extnumber==ext_info['extnumber']).first()
            return query_result.to_auth_json()
        if not ext_info.get('extnumber'):
            query_result=Ext_info.query.filter().all()
            query_result_list=[]
            for i in query_result:
                query_result_list.append(i.to_json())
            return query_result_list
        else:
            query_result=Ext_info.query.filter(Ext_info.domain==ext_info['domain'],Ext_info.group==ext_info['group'],Ext_info.extnumber==ext_info['extnumber'],Ext_info.extname==ext_info['extname']).first()
            return query_result.to_json()