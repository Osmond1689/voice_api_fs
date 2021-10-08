from . import db
from contextlib import contextmanager

class Ext_info(db.Model):
    __tablename__="ext_info"

    id = db.Column(db.Integer,primary_key=True)
    extnumber= db.Column(db.String(10))
    extname= db.Column(db.String(10))
    domain = db.Column(db.String(30))
    group= db.Column(db.String(30))
    password= db.Column(db.String(30))
    callgroup= db.Column(db.String(30))
    
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()  # 事务
        except Exception as e:
            self.session.rollback()  # 回滚
            raise e
    def to_json(self):
        return {
            'id': self.id,
            'extnumber': self.extnumber,
            'extname': self.extname,
            'group':self.group
        }
    def to_auth_json(self):
        return{
            'domain':self.domain,
            'group':self.group,
            'extnumber':self.extnumber,
            'password':self.password,
            'callgroup':self.callgroup,
            'extname':self.extname
        }
    
