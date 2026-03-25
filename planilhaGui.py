import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox


class InterfaceAquisicao:
    def __init__(self, root, planilhaService):
        self.root = root
        self.servico = planilhaService
        self.root.title("Cadastro de Aquisição v1.1")
        self.root.geometry("500x850")
        self.label_titulo = ctk.CTkLabel (
            self.root,
            text = "Cadastro de Compra",
            font = ctk.CTkFont(size = 20, weight = "bold")
        )
        self.label_titulo.pack(pady = (20,10))

        self.campos_config = [
            ("SCD:", "SCD"),
            ("ID PROTOCOLO:", "ID"),
            ("OS:", "OS"),
            ("Data Previsto (dd/mm/aaaa):", "Data Previsto"),
            ("Item:", "Item"),
            ("Quantidade:", "Qtde"),
            ("Valor Unitário:", "Vlr. Unitário"),
            ("Fornecedor:", "Fornecedor")
        ]

        self.entradas = {}

        #Criação campos
        for label_text, chave in self.campos_config:
            label = ctk.CTkLabel(text = label_text, font = ctk.CTkFont(size = 13))
            label.pack(pady = (10 , 0), anchor = "w", padx = 20)

            entry = ctk.CTkEntry(
                self.frame_campos,
                width=400,
                placeholder_text = f"Digite o {label_text.replace(':', '')}..."
            )
            entry.pack(pady=(0, 10), padx=20)

            self.entradas[chave] = entry

        self.bt_salvar = ctk.CTkButton(
            self.root,
            text="SALVAR NA PLANILHA",
            command=self.executar_envio,
            font=ctk.CTkFont(size=14, weight="bold"),
            height=45,
            fg_color="#27ae60",
            hover_color="#219150"
        )
        self.bt_salvar.pack(pady=30, padx=20, fill="x")

    def executar_envio(self):

        dados_finais = {chave: entry.get() for chave, entry in self.entradas.items()}

        if not dados_finais['SCD'] or not dados_finais['Item']:
            messagebox.showwarning("Aviso", "Preencha ao menos SCD e Item")
            return

        try:
            self.btn_salvar.configure(state="disabled", text="Enviando...")
            self.root.update()

            self.servico.inserir_registro(dados_finais)
            messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")
            self.limpar_tela()
        except Exception as e:
            messagebox.showerror("Erro Crítico", f"Erro ao conectar: {e}")

    def limpar_campos(self):
        for entrada in self.entradas.values():
            entrada.delete(0, 'end')