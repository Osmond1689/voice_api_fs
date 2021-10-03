import greenswitch

class Send_commands():
    job_status=''
    def __init__(self,crm_uuid,extensin_number,customer_number,product_code,domain='172.31.24.240') -> None:
        self.crm_uuid=crm_uuid
        self.extensin_number=extensin_number
        self.customer_number=customer_number
        self.product_code=product_code
        self.domain=domain
    def send_call(self):
        cmd='bgapi originate {{crm_uuid={},product_code={},call_type=click-on-call,leg_type=a}}user/{}@{} {} XML default'
        new_cmd=cmd.format(self.crm_uuid,self.product_code,self.extensin_number,self.domain,self.customer_number)
        host='172.17.0.1'
        port=8021
        password='ClueCon'

        fs=greenswitch.InboundESL(host,port,password)
        
        try:
            fs.connect()
        except Exception as e:
            self.job_status=e
        else:
            bgapi_reponse=fs.send(new_cmd)
            self.job_status=bgapi_reponse.data
            fs.stop()


if __name__ == '__main__':
    host='172.17.0.1'
    port=8021
    password='ClueCon'
    cmd='bgapi originate user/1000 &echo'

    fs=greenswitch.InboundESL(host,port,password)
    
    try:
        fs.connect()
    except Exception as e:
        print(e)
    else:
        bgapi_reponse=fs.send(cmd)
        print(bgapi_reponse.data)
        fs.stop()

