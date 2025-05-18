from src.main import db
from flask_login import UserMixin
from datetime import datetime

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha_hash = db.Column(db.String(200), nullable=False)
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Usuario {self.nome}>'

class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer)
    turma = db.Column(db.String(50))
    data_cadastro = db.Column(db.DateTime, default=datetime.utcnow)
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.id'))
    observacoes = db.Column(db.Text)
    
    # Relacionamentos
    nivel = db.relationship('Nivel', backref='alunos')
    avaliacoes = db.relationship('Avaliacao', backref='aluno', lazy=True)
    
    def __repr__(self):
        return f'<Aluno {self.nome}>'

class Nivel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    
    # Relacionamentos
    atividades = db.relationship('Atividade', backref='nivel', lazy=True)
    
    def __repr__(self):
        return f'<Nivel {self.nome}>'

class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text)
    tipo = db.Column(db.String(50))  # reconhecimento_letras, silabas, palavras, frases, etc.
    conteudo = db.Column(db.Text, nullable=False)
    nivel_id = db.Column(db.Integer, db.ForeignKey('nivel.id'))
    
    def __repr__(self):
        return f'<Atividade {self.titulo}>'

class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'))
    data = db.Column(db.DateTime, default=datetime.utcnow)
    resultado = db.Column(db.Text)
    observacoes = db.Column(db.Text)
    
    def __repr__(self):
        return f'<Avaliacao {self.id} - Aluno {self.aluno_id}>'
