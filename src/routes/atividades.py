from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload  # ✅ Adicionado `joinedload` para evitar `DetachedInstanceError`
from src.models.models import Atividade, Nivel
from src.main import db, app

atividades_bp = Blueprint('atividades', __name__, url_prefix='/atividades')

@atividades_bp.route('/')
@login_required
def listar():
    with app.app_context():
        atividades = db.session.query(Atividade).options(joinedload(Atividade.nivel)).all()  # ✅ Corrigido `DetachedInstanceError`
    return render_template('atividades/listar.html', atividades=atividades)

@atividades_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo():
    with app.app_context():
        niveis = Nivel.query.all()
    
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        tipo = request.form.get('tipo')
        conteudo = request.form.get('conteudo')
        nivel_id = request.form.get('nivel_id')
        
        if not titulo or not conteudo or not nivel_id:
            flash('Título, conteúdo e nível são obrigatórios!', 'danger')
            return render_template('atividades/novo.html', niveis=niveis)
        
        with app.app_context():
            atividade = Atividade(
                titulo=titulo,
                descricao=descricao,
                tipo=tipo,
                conteudo=conteudo,
                nivel_id=nivel_id
            )
            db.session.add(atividade)
            db.session.commit()
        
        flash('Atividade cadastrada com sucesso!', 'success')
        return redirect(url_for('atividades.listar'))
    
    return render_template('atividades/novo.html', niveis=niveis)

@atividades_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    with app.app_context():
        atividade = db.session.query(Atividade).options(joinedload(Atividade.nivel)).get(id)  # ✅ Corrigido `DetachedInstanceError`
        niveis = Nivel.query.all()
    
    if request.method == 'POST':
        atividade.titulo = request.form.get('titulo')
        atividade.descricao = request.form.get('descricao')
        atividade.tipo = request.form.get('tipo')
        atividade.conteudo = request.form.get('conteudo')
        atividade.nivel_id = request.form.get('nivel_id')

        with app.app_context():
            db.session.commit()
        
        flash('Atividade atualizada com sucesso!', 'success')
        return redirect(url_for('atividades.listar'))
    
    return render_template('atividades/editar.html', atividade=atividade, niveis=niveis)

@atividades_bp.route('/excluir/<int:id>')
@login_required
def excluir(id):
    with app.app_context():
        atividade = Atividade.query.get_or_404(id)
        db.session.delete(atividade)
        db.session.commit()
    
    flash('Atividade excluída com sucesso!', 'success')
    return redirect(url_for('atividades.listar'))

@atividades_bp.route('/gerar/<int:nivel_id>')
@login_required
def gerar(nivel_id):
    """Gera atividades personalizadas para um determinado nível"""
    with app.app_context():
        nivel = Nivel.query.get_or_404(nivel_id)

        atividades_por_nivel = {
            1: [  # Nível Pré-silábico
                {'titulo': 'Reconhecimento de Letras', 'descricao': 'Atividade para reconhecimento das letras do alfabeto', 'tipo': 'reconhecimento_letras', 'conteudo': 'Apresentação das vogais A, E, I, O, U com imagens associativas.'},
                {'titulo': 'Identificação de Formas', 'descricao': 'Atividade para identificar formas das letras', 'tipo': 'formas', 'conteudo': 'Contorno pontilhado das vogais para o aluno traçar.'}
            ],
            2: [  # Nível Silábico
                {'titulo': 'Formação de Sílabas', 'descricao': 'Atividade para formação de sílabas simples', 'tipo': 'silabas', 'conteudo': 'Combinação de consoantes B, C, D, F com vogais.'},
                {'titulo': 'Leitura de Sílabas', 'descricao': 'Atividade para leitura de sílabas', 'tipo': 'leitura_silabas', 'conteudo': 'Lista de sílabas simples para leitura e identificação.'}
            ],
            3: [  # Nível Silábico-Alfabético
                {'titulo': 'Formação de Palavras Simples', 'descricao': 'Atividade para formação de palavras simples', 'tipo': 'palavras_simples', 'conteudo': 'Junção de sílabas para formar palavras como BOLA, CASA, PATO.'},
                {'titulo': 'Leitura de Palavras', 'descricao': 'Atividade para leitura de palavras simples', 'tipo': 'leitura_palavras', 'conteudo': 'Lista de palavras simples com imagens correspondentes.'}
            ],
            4: [  # Nível Alfabético
                {'titulo': 'Formação de Frases', 'descricao': 'Atividade para formação de frases simples', 'tipo': 'frases', 'conteudo': 'Organização de palavras para formar frases curtas e coerentes.'},
                {'titulo': 'Leitura de Pequenos Textos', 'descricao': 'Atividade para leitura de textos curtos', 'tipo': 'textos', 'conteudo': 'Pequenos textos de 3-4 linhas com vocabulário simples.'}
            ]
        }

        if nivel.id in atividades_por_nivel:
            for ativ_data in atividades_por_nivel[nivel.id]:
                atividade_existente = Atividade.query.filter_by(titulo=ativ_data['titulo'], nivel_id=nivel.id).first()
                if not atividade_existente:
                    db.session.add(Atividade(**ativ_data, nivel_id=nivel.id))  # ✅ Melhorado para simplificação
            
            db.session.commit()
            flash(f'Atividades geradas com sucesso para o nível {nivel.nome}!', 'success')
        else:
            flash(f'Não há atividades predefinidas para o nível {nivel.nome}.', 'warning')

    return redirect(url_for('atividades.listar'))
