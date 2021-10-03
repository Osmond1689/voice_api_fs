import ESL

con=ESL.ESLconnection('172.17.0.1','8021','ClueCon')

if con.connected():
    cmd='originate'
    arg='user/1000 &echo'
    job_uuid='123'

    bgapi=con.bgapi(cmd,arg,job_uuid)
    con.disconnect()