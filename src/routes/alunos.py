from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from src.models.models import Aluno, Nivel
from src.main import db, app  # ✅ Importação de `app` para garantir `app.app_context()`

alunos_bp = Blueprint('alunos', __name__, url_prefix='/alunos')

@alunos_bp.route('/')
@login_required
def listar():
    """Lista todos os alunos cadastrados"""
    with app.app_context():
        alunos = db.session.query(Aluno).options(joinedload(Aluno.nivel)).all()
    return render_template('alunos/listar.html', alunos=alunos)

@alunos_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    """Cria um novo aluno no sistema"""
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
    """Edita as informações de um aluno"""
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
    """Exclui um aluno do sistema"""
    with app.app_context():
        aluno = db.session.get(Aluno, id)

        if not aluno:
            flash('Aluno não encontrado!', 'danger')
            return redirect(url_for('alunos.listar'))

        db.session.delete(aluno)
        db.session.commit()

    flash('Aluno excluído com sucesso!', 'success')
    return redirect(url_for('alunos.listar'))

@alunos_bp.route('/subir_nivel/<int:aluno_id>')
@login_required
def subir_nivel(aluno_id):
    """Permite que o aluno suba de nível corretamente e atualiza a insígnia"""
    with app.app_context():
        aluno = db.session.query(Aluno).get(aluno_id)

        if not aluno:
            flash("Aluno não encontrado!", "danger")
            return redirect(url_for('alunos.listar'))

        # ✅ Verifica o nível atual do aluno
        nivel_atual = db.session.query(Nivel).filter(Nivel.id == aluno.nivel_id).first()

        if not nivel_atual:
            flash("Erro: O nível atual do aluno não foi encontrado!", "danger")
            return redirect(url_for('alunos.listar'))

        # ✅ Busca o próximo nível corretamente
        proximo_nivel = db.session.query(Nivel).filter(Nivel.id > aluno.nivel_id).order_by(Nivel.id).first()

        if proximo_nivel:  # ✅ Se existe um próximo nível, atualiza
            aluno.nivel_id = proximo_nivel.id  # ✅ Atualiza nível
            aluno.insignia = proximo_nivel.insignia  # ✅ Atualiza insígnia correspondente
            db.session.commit()
            flash(f"Aluno {aluno.nome} avançou para {proximo_nivel.nome} e ganhou a insígnia {proximo_nivel.insignia}! 🏅", "success")
        else:
            flash("O aluno já está no nível máximo!", "warning")

    return redirect(url_for('alunos.listar'))

@alunos_bp.route('/alterar_nivel/<int:aluno_id>', methods=['POST'])
@login_required
def alterar_nivel(aluno_id):
    """Permite a edição manual do nível do aluno"""
    with app.app_context():
        aluno = db.session.query(Aluno).get(aluno_id)

        if not aluno:
            flash("Aluno não encontrado!", "danger")
            return redirect(url_for('alunos.listar'))

        novo_nivel_id = request.form.get("nivel_id")

        if novo_nivel_id:
            aluno.nivel_id = int(novo_nivel_id)
            db.session.commit()
            flash(f"Nível do aluno {aluno.nome} atualizado para {aluno.nivel.nome}!", "success")
        else:
            flash("Erro ao alterar nível!", "danger")

    return redirect(url_for('alunos.listar'))
