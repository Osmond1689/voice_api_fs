from . import db
'''
 queue    | character varying(255) |           |          | 
 agent    | character varying(255) |           |          | 
 state    | character varying(255) |           |          | 
 level    | integer                |           | not null | 1
 position | integer                |           | not null | 1
'''
class Tiers(db.Model):
    __tablename__ = 'tiers'
    queue    =db.Column(db.String(255))
    agent    =db.Column(db.String(255))
    state    =db.Column(db.String(255))
    level    =db.Column(db.Integer,nullable=False,default=1)
    position =db.Column(db.Integer,nullable=False,default=1)

    
