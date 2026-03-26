Controle de Aquisições - Google Sheets
Interface em Python para automação de lançamentos no Google Sheets, integrada com tabelas pré-formatadas e menus suspensos.

🚀 Funcionalidades
Interface gráfica simples para inserção de dados.

Cálculo automático de status (Atrasado/Crítico).

Preenchimento inteligente de linhas em tabelas existentes.

Conexão segura via API do Google Cloud.

🛠️ Requisitos
Python 3.x

Bibliotecas: gspread, oauth2client, pandas, tkinter

📂 Estrutura do Projeto
main.py: Ponto de entrada que inicializa a aplicação.

interface_gui.py: Contém a classe da interface visual (Tkinter).

planilha_service.py: Contém a lógica de comunicação com o Google Sheets.

credentials.json: Arquivo de autenticação da API (não incluso por segurança).

⚙️ Configuração
Coloque o arquivo credentials.json na pasta raiz do projeto.

Certifique-se de que a planilha "Controle de Compras em Kanban" esteja compartilhada com o e-mail do cliente presente no JSON.

No terminal, instale as dependências:

Plaintext
pip install gspread oauth2client
📖 Como usar
Execute o arquivo principal:

Plaintext
python main.py
Preencha os campos na janela que será aberta.

Clique em "Salvar" e os dados serão inseridos na primeira linha disponível da planilha.

⚠️ Notas Técnicas
O sistema identifica a próxima linha livre baseada na Coluna A (SCD).

A Coluna F (Situação) é ignorada pelo script para preservar os menus suspensos originais da planilha.

Datas devem ser inseridas no formato DD/MM/AAAA.
