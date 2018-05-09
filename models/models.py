#encoding:utf-8

from models import db

class FlaskTable(db.Model):
    __tablename__ = 'fadfsd'
    id = db.Column(db.Integer(),primary_key=True)
    dafef = db.Column(db.DATETIME())

# class OneTable(db.Model):
#     __bind_key__ = 'db_one'
#     __tablename__ = 'fadfsd'
#     id = db.Column(db.Integer(),primary_key=True)
#     dafef = db.Column(db.DATETIME())
#
# class TwoTable(db.Model):
#     __bind_key__ = 'db_two'
#     __tablename__ = 'fadfsd'
#     id = db.Column(db.Integer(),primary_key=True)
#     dafef = db.Column(db.DATETIME())