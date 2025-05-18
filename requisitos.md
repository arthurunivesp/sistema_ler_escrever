# Requisitos do Sistema Web de Alfabetização e Adaptação Curricular

## Visão Geral
Sistema web para geração de materiais de alfabetização e adaptação curricular para alunos do 6º ano que não sabem ler e escrever. O sistema permitirá cadastrar alunos, definir seus níveis de conhecimento e gerar métodos personalizados em PDF para avaliação e acompanhamento do progresso.

## Requisitos Funcionais

### 1. Cadastro de Alunos
- Cadastrar informações básicas dos alunos (nome, idade, turma, etc.)
- Armazenar histórico de avaliações e progresso
- Permitir edição e exclusão de cadastros
- Visualizar lista de alunos cadastrados

### 2. Definição de Níveis de Conhecimento
- Cadastrar diferentes níveis de alfabetização (pré-silábico, silábico, silábico-alfabético, alfabético)
- Definir características específicas de cada nível
- Associar alunos aos níveis correspondentes
- Permitir atualização do nível conforme progresso do aluno

### 3. Geração de Métodos Personalizados
- Criar atividades adaptadas ao nível de cada aluno
- Gerar conteúdos específicos para alfabetização (reconhecimento de letras, formação de sílabas, palavras, frases)
- Personalizar atividades com base no histórico e progresso do aluno
- Oferecer variedade de métodos pedagógicos (fônico, silábico, global, etc.)

### 4. Exportação para PDF
- Gerar documentos PDF com atividades personalizadas
- Incluir cabeçalho com informações do aluno e nível
- Formatar adequadamente para impressão
- Permitir seleção de conteúdos específicos para inclusão no PDF

### 5. Acompanhamento de Progresso
- Registrar resultados das atividades realizadas
- Visualizar evolução do aluno ao longo do tempo
- Gerar relatórios de desempenho
- Sugerir próximos passos no processo de alfabetização

## Requisitos Não Funcionais

### 1. Usabilidade
- Interface intuitiva para professores sem conhecimentos técnicos avançados
- Design responsivo para acesso em diferentes dispositivos
- Fluxo de trabalho simplificado para geração rápida de materiais

### 2. Desempenho
- Geração rápida de documentos PDF
- Carregamento eficiente das páginas do sistema
- Capacidade para gerenciar múltiplos usuários simultaneamente

### 3. Segurança
- Proteção dos dados dos alunos
- Controle de acesso por autenticação
- Backup regular dos dados cadastrados

### 4. Tecnologia
- Sistema web acessível via navegador
- Banco de dados para armazenamento das informações
- Framework Flask para desenvolvimento backend
- Biblioteca WeasyPrint para geração de PDFs

## Fluxo Principal do Sistema
1. Professor acessa o sistema e faz login
2. Cadastra um novo aluno ou seleciona um aluno existente
3. Define ou atualiza o nível de conhecimento do aluno
4. Seleciona o tipo de método/atividade a ser gerado
5. Sistema gera automaticamente o conteúdo personalizado
6. Professor visualiza prévia do material
7. Sistema exporta o material em formato PDF
8. Professor imprime o material para uso com o aluno
9. Após aplicação, professor registra resultados e progresso
10. Sistema atualiza o histórico do aluno e sugere próximos passos
