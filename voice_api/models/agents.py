from . import db
from contextlib import contextmanager
'''
       Column        |          Type           | Collation | Nullable | Default 
----------------------+-------------------------+-----------+----------+---------
 name                 | character varying(255)  |           |          | 
 instance_id          | character varying(255)  |           |          | 
 uuid                 | character varying(255)  |           |          | 
 type                 | character varying(255)  |           |          | 
 contact              | character varying(1024) |           |          | 
 status               | character varying(255)  |           |          | 
 state                | character varying(255)  |           |          | 
 max_no_answer        | integer                 |           | not null | 0
 wrap_up_time         | integer                 |           | not null | 0
 reject_delay_time    | integer                 |           | not null | 0
 busy_delay_time      | integer                 |           | not null | 0
 no_answer_delay_time | integer                 |           | not null | 0
 last_bridge_start    | integer                 |           | not null | 0
 last_bridge_end      | integer                 |           | not null | 0
 last_offered_call    | integer                 |           | not null | 0
 last_status_change   | integer                 |           | not null | 0
 no_answer_count      | integer                 |           | not null | 0
 calls_answered       | integer                 |           | not null | 0
 talk_time            | integer                 |           | not null | 0
 ready_time           | integer                 |           | not null | 0
 external_calls_count | integer                 |           | not null | 0
'''

class Agents(db.Model):
    __tablename__='agents'
    name                 =db.Column(db.String(255))  #1001@default
    instance_id          =db.Column(db.String(255))  #single_box
    uuid                 =db.Column(db.String(255)) 
    type                 =db.Column(db.String(255))  #callback
    contact              =db.Column(db.String(1024)) #user/1001
    status               =db.Column(db.String(255))  #Logged out
    state                =db.Column(db.String(255))  #Waiting
    max_no_answer        =db.Column(db.Integer,nullable=False,default=5)  #最大无应答 就会将座席改成On Break
    wrap_up_time         =db.Column(db.Integer,nullable=False,default=15) #整理时间
    reject_delay_time    =db.Column(db.Integer,nullable=False,default=30) #拒绝时间 
    busy_delay_time      =db.Column(db.Integer,nullable=False,default=0)  
    no_answer_delay_time =db.Column(db.Integer,nullable=False,default=0)
    last_bridge_start    =db.Column(db.Integer,nullable=False,default=0)
    last_bridge_end      =db.Column(db.Integer,nullable=False,default=0)
    last_offered_call    =db.Column(db.Integer,nullable=False,default=0)
    last_status_change   =db.Column(db.Integer,nullable=False,default=0)
    no_answer_count      =db.Column(db.Integer,nullable=False,default=0)
    calls_answered       =db.Column(db.Integer,nullable=False,default=0)
    talk_time            =db.Column(db.Integer,nullable=False,default=0)
    ready_time           =db.Column(db.Integer,nullable=False,default=0)
    external_calls_count =db.Column(db.Integer,nullable=False,default=0)

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()  # 事务
        except Exception as e:
            self.session.rollback()  # 回滚
            raise e