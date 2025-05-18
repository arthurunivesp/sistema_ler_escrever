from flask import Blueprint, render_template, redirect, url_for, flash, request, send_file
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from src.models.models import Aluno, Nivel, Atividade, Avaliacao
from src.main import db, app
import weasyprint
from io import BytesIO
from datetime import datetime

pdf_bp = Blueprint('pdf', __name__, url_prefix='/pdf')

@pdf_bp.route('/gerar/<int:aluno_id>')
@login_required
def gerar(aluno_id):
    """Gera PDF personalizado para um aluno específico"""
    with app.app_context():
        # Buscar aluno e forçar carregamento dos atributos antes da sessão ser fechada
        aluno = db.session.query(Aluno).options(joinedload(Aluno.nivel)).get(aluno_id)

        if not aluno:
            flash('Aluno não encontrado!', 'danger')
            return redirect(url_for('alunos.listar'))

        if not aluno.nivel:
            flash('O aluno precisa ter um nível definido para gerar atividades!', 'danger')
            return redirect(url_for('alunos.editar', id=aluno_id))

        atividades = db.session.query(Atividade).filter_by(nivel_id=aluno.nivel_id).all()

        if not atividades:
            flash('Não há atividades cadastradas para o nível do aluno!', 'danger')
            return redirect(url_for('atividades.gerar', nivel_id=aluno.nivel_id))

        # **Correção:** Carregar atributos antes de sair da sessão
        aluno_nome = aluno.nome.replace(" ", "_")
        nivel_nome = aluno.nivel.nome

        # Renderizar o template HTML com as atividades
        html = render_template(
            'pdf/atividades.html',
            aluno=aluno,
            atividades=atividades,
            data_geracao=datetime.now().strftime('%d/%m/%Y')
        )

        # Gerar PDF a partir do HTML
        pdf = weasyprint.HTML(string=html).write_pdf()

        # Criar um objeto BytesIO para armazenar o PDF
        pdf_io = BytesIO(pdf)
        pdf_io.seek(0)

        # **Correção:** Garantir que a avaliação seja registrada dentro da sessão ativa
        with db.session.no_autoflush:
            avaliacao = Avaliacao(
                aluno_id=aluno.id,
                resultado=f"PDF gerado com {len(atividades)} atividades",
                observacoes="Geração automática de atividades"
            )
            db.session.add(avaliacao)
            db.session.commit()

    # Retornar o PDF como um arquivo para download
    return send_file(
        pdf_io,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=f'atividades_{aluno_nome}_{datetime.now().strftime("%Y%m%d")}.pdf'
    )

@pdf_bp.route('/visualizar/<int:aluno_id>')
@login_required
def visualizar(aluno_id):
    """Visualiza PDF personalizado para um aluno antes de gerar"""
    with app.app_context():
        aluno = db.session.query(Aluno).options(joinedload(Aluno.nivel)).get(aluno_id)

        if not aluno:
            flash('Aluno não encontrado!', 'danger')
            return redirect(url_for('alunos.listar'))

        if not aluno.nivel:
            flash('O aluno precisa ter um nível definido para visualizar atividades!', 'danger')
            return redirect(url_for('alunos.editar', id=aluno_id))

        atividades = db.session.query(Atividade).filter_by(nivel_id=aluno.nivel_id).all()

        if not atividades:
            flash('Não há atividades cadastradas para o nível do aluno!', 'danger')
            return redirect(url_for('atividades.gerar', nivel_id=aluno.nivel_id))

    return render_template(
        'pdf/preview.html',
        aluno=aluno,
        atividades=atividades,
        data_geracao=datetime.now().strftime('%d/%m/%Y')
    )

@pdf_bp.route('/editar/<int:aluno_id>', methods=['GET', 'POST'])
@login_required
def editar(aluno_id):
    """Permite edição manual do conteúdo do PDF antes da geração"""
    with app.app_context():
        aluno = db.session.query(Aluno).options(joinedload(Aluno.nivel)).get(aluno_id)
        atividades = db.session.query(Atividade).filter_by(nivel_id=aluno.nivel_id).all()

        if not aluno:
            flash('Aluno não encontrado!', 'danger')
            return redirect(url_for('alunos.listar'))

        if not aluno.nivel:
            flash('O aluno precisa ter um nível definido para editar atividades!", "danger')
            return redirect(url_for('alunos.editar', id=aluno_id))

        if request.method == 'POST':
            for atividade in atividades:
                atividade.conteudo = request.form.get(f'atividade_{atividade.id}')
            db.session.commit()
            flash("PDF atualizado com sucesso!", "success")
            return redirect(url_for('pdf.visualizar', aluno_id=aluno_id))

    return render_template('pdf/editar.html', aluno=aluno, atividades=atividades)
