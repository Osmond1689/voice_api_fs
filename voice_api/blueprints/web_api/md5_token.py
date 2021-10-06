import hashlib
import time,datetime

def encrypt_md5(old_str):
    utc_now=datetime.datetime.utcnow()
    utc_old_now=(utc_now-datetime.timedelta(minutes=1))

    utc_now_time_array = time.strptime(utc_now.strftime("%Y-%m-%d %H:%M:00"), "%Y-%m-%d %H:%M:00")
    utc_old_now_time_array = time.strptime(utc_old_now.strftime("%Y-%m-%d %H:%M:00"), "%Y-%m-%d %H:%M:00")
    time_stamp = str(time.mktime(utc_now_time_array))
    old_time_stamp = str(time.mktime(utc_old_now_time_array))
    
    #print(time_stamp,old_time_stamp)
    new_str=old_str+time_stamp
    new_str_old=old_str+old_time_stamp
    h1=hashlib.md5()
    h2=hashlib.md5()
    h1.update(new_str.encode(encoding='utf-8'))
    h2.update(new_str_old.encode(encoding='utf-8'))
    md5_list=[]
    md5_list.append(h1.hexdigest())
    md5_list.append(h2.hexdigest())
    #调试使用，打印token
    print(md5_list)
    return md5_list

if __name__=='__main__':
    a=encrypt_md5('123')
    print(a)
