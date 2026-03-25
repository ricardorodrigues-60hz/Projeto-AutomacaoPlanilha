import gspread
from google.oauth2.service_account import Credentials


class PlanilhaService:
    def __init__(self, arquivo_json, nome_planilha):
        self.escopos = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        self.creds = Credentials.from_service_account_file(arquivo_json, scopes=self.escopos)
        self.cliente = gspread.authorize(self.creds)
        self.aba = self.cliente.open(nome_planilha).sheet1

    def inserir_registro(self, dados):

        linha = [
            dados.get('scd'), dados.get('id'), dados.get('os'), dados.get('previsto'),
            "Sistema Python", dados.get('Item'), dados.get('qtde'),
            dados.get('valor_uni'), "", dados.get('fornecedor'),
            "", dados.get('obs')
        ]

        self.aba.append_row(linha, value_input_option='USER_ENTERED')


if __name__ == "__main__":
    print("--- INICIANDO TESTE DE CONEXÃO ISOLADO ---")
    try:
        # 1. Tenta conectar
        # Certifique-se de que o nome da planilha está IDÊNTICO ao do Google Drive
        servico = PlanilhaService('credentials.json', 'Controle de Compras em Kanban')
        print("✅ Conexão com a API estabelecida.")

        # 2. Tenta inserir um dado de teste
        dados_teste = {
            'scd': 'TESTE', 'id': '999', 'os': '000',
            'previsto': '20/12/2026', 'item': 'Item de Teste Python',
            'qtde': '1', 'valor_uni': '10.00', 'fornecedor': 'Teste SA',
            'obs': 'Teste de integração'
        }

        print("Enviando dados...")
        servico.inserir_registro(dados_teste)
        print("✅ Dados gravados na planilha com sucesso!")

    except FileNotFoundError:
        print("❌ Erro: O arquivo 'credentials.json' não foi encontrado na pasta.")
    except Exception as e:
        print(f"⚠️ Nota: Ocorreu algo inesperado, mas verifique sua planilha.")
        print(f"Detalhe técnico: {e}")