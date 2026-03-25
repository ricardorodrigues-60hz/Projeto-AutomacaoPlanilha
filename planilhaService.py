import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime


class PlanilhaService:
    def __init__(self, arquivo_json, nome_planilha):

        self.escopo = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        self.creds = ServiceAccountCredentials.from_json_keyfile_name(filename = arquivo_json, scopes=self.escopo)
        self.cliente = gspread.authorize(self.creds)
        self.aba = self.cliente.open('Controle de Compras em Kanban').sheet1


    def inserir_registro(self, dados):

        hoje = datetime.today().strftime('%d/%m/%Y')

        valores_coluna_a = self.aba.col_values(1)
        proxima_linha = len(valores_coluna_a) + 1

        campos = [
            dados.get('SCD'),
            dados.get('ID'),
            dados.get('OS'),
            hoje,
            dados.get('Data Previsto'),
            '',
            dados.get('Solicitante'),
            dados.get('Item'),
            dados.get('Qtde'),
            dados.get('Vlr. Unitário'),
            '',
            dados.get('Fornecedor'),
            ''
        ]
        range_para_preencher = f"A{proxima_linha}:N{proxima_linha}"

        self.aba.update(range_para_preencher, [campos], value_input_option='USER_ENTERED')



