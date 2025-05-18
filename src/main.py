import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))  # NÃO ALTERE ESTA LINHA!

from flask import Flask, render_template, redirect, url_for, flash, request, session, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
import weasyprint
from io import BytesIO
from jinja2 import Environment

# Inicializando a aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta_do_sistema_alfabetizacao'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/gigie/Documents/alfabetizacao.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando banco de dados e autenticação
db = SQLAlchemy()
db.init_app(app)  # ✅ Correção: Garante que o banco seja inicializado corretamente com o Flask

login_manager = LoginManager()
login_manager.init_app(app)  # ✅ Correção: Inicializa o sistema de login com a aplicação
login_manager.login_view = 'auth.login'  # Define a rota de login corretamente

@login_manager.user_loader
def load_user(user_id):
    from src.models.models import Usuario
    with app.app_context():
        return db.session.get(Usuario, int(user_id))

# Registrar filtro personalizado para Jinja2
def nl2br(value):
    """Converte quebras de linha em `<br>` para exibição correta no PDF"""
    return value.replace("\n", "<br>") if value else ""

app.jinja_env.filters["nl2br"] = nl2br  # ✅ Corrigido erro do filtro `nl2br` no PDF

# Importar rotas e modelos após a inicialização do app
from src.routes.auth import auth_bp
from src.routes.alunos import alunos_bp
from src.routes.niveis import niveis_bp
from src.routes.atividades import atividades_bp
from src.routes.pdf import pdf_bp

# Registrar blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(alunos_bp)
app.register_blueprint(niveis_bp)
app.register_blueprint(atividades_bp)
app.register_blueprint(pdf_bp)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Inicializar banco de dados via CLI
@app.cli.command('init-db')
def init_db():
    with app.app_context():
        db.create_all()
        print('Banco de dados inicializado.')

# Rodar a aplicação
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

