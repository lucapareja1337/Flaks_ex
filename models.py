from app import db

class Tarefa(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    descricao = db.Column(db.String)