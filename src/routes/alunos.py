from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from src.models.models import Aluno, Nivel
from src.main import db, app  # ✅ Importação de `app` para garantir `app.app_context()`

alunos_bp = Blueprint('alunos', __name__, url_prefix='/alunos')

@alunos_bp.route('/')
@login_required
def listar():
    with app.app_context():  # ✅ Garante que a consulta ao banco ocorra dentro do contexto do Flask
        alunos = db.session.query(Aluno).options(joinedload(Aluno.nivel)).all()  # ✅ Carrega `nivel` junto com `Aluno`
    return render_template('alunos/listar.html', alunos=alunos)

@alunos_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    with app.app_context():
        niveis = db.session.query(Nivel).all()
    
    if request.method == 'POST':
        nome = request.form.get('nome')
        idade = request.form.get('idade')
        turma = request.form.get('turma')
        nivel_id = request.form.get('nivel_id')
        observacoes = request.form.get('observacoes')
        
        if not nome:
            flash('Nome é obrigatório!', 'danger')
            return render_template('alunos/novo.html', niveis=niveis)
        
        with app.app_context():
            aluno = Aluno(
                nome=nome,
                idade=idade,
                turma=turma,
                nivel_id=nivel_id,
                observacoes=observacoes
            )
            db.session.add(aluno)
            db.session.commit()
        
        flash('Aluno cadastrado com sucesso!', 'success')
        return redirect(url_for('alunos.listar'))
    
    return render_template('alunos/novo.html', niveis=niveis)

@alunos_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    with app.app_context():
        aluno = db.session.query(Aluno).options(joinedload(Aluno.nivel)).get(id)
        niveis = db.session.query(Nivel).all()
    
    if not aluno:
        flash('Aluno não encontrado!', 'danger')
        return redirect(url_for('alunos.listar'))

    if request.method == 'POST':
        aluno.nome = request.form.get('nome')
        aluno.idade = request.form.get('idade')
        aluno.turma = request.form.get('turma')
        aluno.nivel_id = request.form.get('nivel_id')
        aluno.observacoes = request.form.get('observacoes')

        with app.app_context():
            db.session.commit()
        
        flash('Aluno atualizado com sucesso!', 'success')
        return redirect(url_for('alunos.listar'))
    
    return render_template('alunos/editar.html', aluno=aluno, niveis=niveis)

@alunos_bp.route('/excluir/<int:id>')
@login_required
def excluir(id):
    with app.app_context():
        aluno = db.session.get(Aluno, id)

        if not aluno:
            flash('Aluno não encontrado!', 'danger')
            return redirect(url_for('alunos.listar'))

        db.session.delete(aluno)
        db.session.commit()
    
    flash('Aluno excluído com sucesso!', 'success')
    return redirect(url_for('alunos.listar'))

