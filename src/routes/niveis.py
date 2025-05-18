from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from src.models.models import Nivel
from src.main import db, app  # ✅ Importação de `app` para garantir `app.app_context()`

niveis_bp = Blueprint('niveis', __name__, url_prefix='/niveis')

@niveis_bp.route('/')
@login_required
def listar():
    with app.app_context():  # ✅ Garante que a consulta ao banco ocorra dentro do contexto do Flask
        niveis = Nivel.query.all()
    return render_template('niveis/listar.html', niveis=niveis)

@niveis_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        
        if not nome:
            flash('Nome é obrigatório!', 'danger')
            return render_template('niveis/novo.html')
        
        with app.app_context():
            nivel = Nivel(
                nome=nome,
                descricao=descricao
            )

            db.session.add(nivel)
            db.session.commit()
        
        flash('Nível cadastrado com sucesso!', 'success')
        return redirect(url_for('niveis.listar'))
    
    return render_template('niveis/novo.html')

@niveis_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    with app.app_context():
        nivel = Nivel.query.get_or_404(id)
    
    if request.method == 'POST':
        nivel.nome = request.form.get('nome')
        nivel.descricao = request.form.get('descricao')

        with app.app_context():
            db.session.commit()
        
        flash('Nível atualizado com sucesso!', 'success')
        return redirect(url_for('niveis.listar'))
    
    return render_template('niveis/editar.html', nivel=nivel)

@niveis_bp.route('/excluir/<int:id>')
@login_required
def excluir(id):
    with app.app_context():
        nivel = Nivel.query.get_or_404(id)

        # Verificar se há alunos associados a este nível
        if nivel.alunos:
            flash('Não é possível excluir um nível que possui alunos associados!', 'danger')
            return redirect(url_for('niveis.listar'))

        db.session.delete(nivel)
        db.session.commit()
    
    flash('Nível excluído com sucesso!', 'success')
    return redirect(url_for('niveis.listar'))
