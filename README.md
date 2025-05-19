# sistema_ler_escrever
Sistema de alfabetização para alunos do 6º ano

# Sistema Ler & Escrever

## 📚 Sobre o projeto
O **Sistema Ler & Escrever** é uma plataforma inovadora voltada para a **alfabetização de alunos do 6º ano**, ajudando-os a desenvolver habilidades de leitura e escrita de forma interativa e pedagógica.  

A aplicação utiliza uma metodologia baseada em atividades progressivas, que permitem aos alunos avançarem de nível conforme seu aprendizado. O sistema também oferece suporte para professores acompanharem o desempenho dos alunos.  

---

## 🎯 Objetivos
✅ **Alfabetizar alunos** de forma intuitiva e acessível.  
✅ **Ensinar leitura e escrita** por meio de atividades práticas.  
✅ **Acompanhar a evolução dos alunos** com um sistema de níveis.  
✅ **Motivar os estudantes** com insígnias e recompensas educacionais.  

---

## ⚙️ Tecnologias utilizadas
📌 **Python** - Linguagem principal do projeto.  
📌 **Flask** - Framework para construção da API e interface web.  
📌 **SQLite** - Banco de dados leve e eficiente para armazenar alunos e atividades.  
📌 **HTML, CSS e JavaScript** - Interface interativa para alunos e professores.  

---

## 🚀 Como instalar e rodar o sistema

### **1️⃣ Instalar e ativar o ambiente virtual (`venv`)**
Antes de iniciar o sistema, **é recomendado criar um ambiente virtual para gerenciar as dependências**:

```bash
# Criar o ambiente virtual (apenas necessário na primeira vez)
python -m venv venv  

# Ativar o ambiente virtual no Windows
venv\Scripts\activate  

# Ativar o ambiente virtual no macOS/Linux
source venv/bin/activate  


Instalar as dependências
Agora, instale todas as dependências do projeto com:
pip install -r requirements.txt

3️⃣ Configurar e instalar o banco de dados
O sistema utiliza SQLite como banco de dados. Para garantir que ele está configurado corretamente, siga estes passos:

📌 Criar a estrutura do banco de dados:
python src/setup_db.py

📌 Verificar se o banco foi criado corretamente:
sqlite3 .tables  # Listar todas as tabelas existentes no banco

📌 Se necessário, insira os níveis manualmente:
sqlite3 
INSERT INTO nivel (id, nome, descricao, insignia) VALUES (1, 'Explorador das Letras', 'Início da alfabetização', '🔤');
INSERT INTO nivel (id, nome, descricao, insignia) VALUES (2, 'Caçador de Palavras', 'Formação de palavras', '🔍');
INSERT INTO nivel (id, nome, descricao, insignia) VALUES (3, 'Mestre das Frases', 'Criação de frases', '✏️');
INSERT INTO nivel (id, nome, descricao, insignia) VALUES (4, 'Aventureiro da Leitura', 'Interpretação de textos', '📖');
INSERT INTO nivel (id, nome, descricao, insignia) VALUES (5, 'Guardião das Histórias', 'Leitura avançada', '🌟');

4️⃣ Rodar a aplicação
Agora que tudo está configurado, execute o sistema com:
python src/main.py

📌 Acesse a interface pelo navegador em: 🔗 http://127.0.0.1:5000

🎓 Metodologia pedagógica
O sistema é baseado em níveis de aprendizado, onde os alunos começam com atividades básicas e vão avançando à medida que desenvolvem suas habilidades.

✅ Cada nível representa um estágio da alfabetização:

Explorador das Letras - Introdução à leitura e identificação de letras.

Caçador de Palavras - Formação de palavras e reconhecimento de sons.

Mestre das Frases - Construção de frases simples e coerentes.

Aventureiro da Leitura - Interpretação de textos curtos e desafios de leitura.

Guardião das Histórias - Habilidades avançadas de leitura e produção textual.

✅ A aprendizagem é motivada através de insígnias, concedidas conforme os alunos atingem novos níveis!

💡 Conclusão
O Sistema Ler & Escrever é uma ferramenta poderosa para alfabetizar alunos, ajudando-os a ler, escrever e interpretar textos de forma lúdica e eficiente.

📌 Vamos transformar o aprendizado em uma jornada incrível! 🚀📚✨