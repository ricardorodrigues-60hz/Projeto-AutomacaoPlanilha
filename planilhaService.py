import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials


class PlanilhaService:
    def __init__(self, arquivo_json, nome_planilha):
        self.arquivo_json = 'credentials.json'
        self.escopos = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]
        self.SAMPLE_SPREADSHEET_ID = '1cz9WI5ocxhhD7ujOqNCjPhCFXD0X97kFTbP_kE9shXg'
        self.SAMPLE_RANGE_NAME = 'A2:N100'
        self.creds = ServiceAccountCredentials.from_json_keyfile_name(filename = arquivo_json, scopes=self.escopos)
        self.cliente = gspread.authorize(self.creds)
        self.aba = self.cliente.open('Controle de Compras em Kanban').sheet1


    def inserir_registro(self, dados):

        linha = [
            dados.get('SCD'),
            dados.get('ID'),
            dados.get('OS'),
            '',
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

        self.aba.append_row(linha, value_input_option='USER_ENTERED')



