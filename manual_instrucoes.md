# Manual de Instruções - Sistema de Alfabetização e Adaptação Curricular

## Visão Geral

Este sistema web foi desenvolvido para auxiliar professores na geração de materiais de alfabetização e adaptação curricular para alunos do 6º ano que não sabem ler e escrever. O sistema permite cadastrar alunos, definir seus níveis de conhecimento e gerar métodos personalizados em PDF para avaliação e acompanhamento do progresso.

## Requisitos do Sistema

- Python 3.8 ou superior
- Flask e suas dependências
- WeasyPrint para geração de PDFs
- Navegador web moderno (Chrome, Firefox, Edge, etc.)

## Instalação

1. Certifique-se de ter o Python instalado em seu computador
2. Descompacte o arquivo do projeto em uma pasta de sua preferência
3. Abra um terminal na pasta do projeto
4. Ative o ambiente virtual:
   ```
   source venv/bin/activate  # No Linux/Mac
   venv\Scripts\activate     # No Windows
   ```
5. Instale as dependências (caso necessário):
   ```
   pip install -r requirements.txt
   ```
6. Inicialize o banco de dados:
   ```
   flask --app src.main init-db
   ```
7. Execute o aplicativo:
   ```
   python src/main.py
   ```
8. Acesse o sistema em seu navegador: http://localhost:5000

## Primeiros Passos

1. **Registre-se no sistema**:
   - Acesse a página inicial e clique em "Registrar"
   - Preencha seus dados e crie uma conta

2. **Cadastre níveis de conhecimento**:
   - Acesse o menu "Níveis"
   - Clique em "Novo Nível"
   - Recomendamos criar pelo menos os seguintes níveis:
     - Pré-silábico
     - Silábico
     - Silábico-alfabético
     - Alfabético

3. **Gere atividades para cada nível**:
   - Na lista de níveis, clique em "Gerar Atividades" para cada nível cadastrado
   - O sistema criará automaticamente atividades adequadas para cada nível

4. **Cadastre alunos**:
   - Acesse o menu "Alunos"
   - Clique em "Novo Aluno"
   - Preencha os dados do aluno, incluindo o nível de conhecimento

5. **Gere PDFs personalizados**:
   - Na lista de alunos, clique em "Visualizar PDF" para ver uma prévia
   - Clique em "Gerar PDF" para baixar o documento com as atividades personalizadas

## Funcionalidades Principais

### Cadastro de Alunos
- Permite registrar informações básicas dos alunos
- Associa cada aluno a um nível de conhecimento
- Armazena histórico de avaliações e progresso

### Definição de Níveis
- Cadastro de diferentes níveis de alfabetização
- Personalização das características de cada nível
- Associação de alunos aos níveis correspondentes

### Geração de Métodos
- Criação automática de atividades adaptadas ao nível de cada aluno
- Personalização de conteúdos específicos para alfabetização
- Variedade de métodos pedagógicos

### Exportação para PDF
- Geração de documentos PDF com atividades personalizadas
- Formatação adequada para impressão
- Cabeçalho com informações do aluno e nível

### Acompanhamento de Progresso
- Registro de resultados das atividades realizadas
- Visualização da evolução do aluno ao longo do tempo

## Dicas de Uso

- **Personalize as atividades**: Você pode editar as atividades geradas automaticamente para adaptá-las às necessidades específicas de cada aluno.
- **Atualize o nível do aluno**: À medida que o aluno progride, atualize seu nível para que as atividades geradas sejam adequadas ao seu desenvolvimento.
- **Crie novas atividades**: Além das atividades geradas automaticamente, você pode criar novas atividades personalizadas para cada nível.

## Suporte

Para dúvidas ou problemas, consulte a documentação técnica incluída no projeto ou entre em contato com o desenvolvedor.
