from utils.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from .type_document import Type_document

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    number_ID = db.Column(db.String(200), nullable=True)
    name = db.Column(db.String(200), nullable=True)
    last_name = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(200), nullable=True)
    phone = db.Column(db.String(200), nullable=True)

    type_id = db.Column(db.Integer, ForeignKey('type_document.id'), index=True)
    type_document = relationship(Type_document, foreign_keys=[type_id])

def __init__(self, number_ID, name, last_name, email, phone, type_document):
        self.number_ID = number_ID
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.type_document = type_document

def __repr__(self):
        return f'{self.id} {self.name}'
