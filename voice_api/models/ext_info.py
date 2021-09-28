from . import db

class Ext_info(db.Model):
    __tablename__="ext_info"

    id = db.Column(db.Integer,primary_key=True)
    extnumber= db.Column(db.String(10))
    domain = db.Column(db.String(30))
    group= db.Column(db.String(30))
    password= db.Column(db.String(30))
    callgroup= db.Column(db.String(30))
