from utils.db import db

class Type_document(db.Model):
    __tablename__ = 'type_document'
    id = db.Column(db.Integer, primary_key=True)
    type_document = db.Column(db.String(200), nullable=True)

def __init__(self, type_document):
        self.type_document = type_document

def __repr__(self):
        return f'{self.id} {self.type_document}'
