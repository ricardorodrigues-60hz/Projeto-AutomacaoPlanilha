import customtkinter as ctk
from tkinter import messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class InterfaceAquisicao:
    def __init__(self, root, planilhaService):
        self.root = root
        self.servico = planilhaService
        self.root.title("Cadastro de Aquisição v1.1")
        self.root.geometry("500x750")
        self.label_titulo = ctk.CTkLabel (
            self.root,
            text = "Cadastro de Compra",
            font = ctk.CTkFont(size = 22, weight = "bold")
        )
        self.label_titulo.pack(pady = (30,20))
        self.main_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.main_frame.pack(fill="both", expand=True, padx=40)

        self.campos_config = [
            ("SCD:", "SCD"),
            ("ID PROTOCOLO:", "ID"),
            ("OS:", "OS"),
            ("Data Previsto (dd/mm/aaaa):", "Data Previsto"),
            ("Solicitante:", "Solicitante"),
            ("Item:", "Item"),
            ("Quantidade:", "Qtde"),
            ("Valor Unitário:", "Vlr. Unitário"),
            ("Fornecedor:", "Fornecedor")
        ]

        self.entradas = {}

        #Criação campos
        for label_text, chave in self.campos_config:
            label = ctk.CTkLabel(self.main_frame, text = label_text, font = ctk.CTkFont(size = 13))
            label.pack(pady = (2 , 0), anchor = "w")

            entry = ctk.CTkEntry(
                self.main_frame,
                width=400,
                height=30,
                placeholder_text = f"Informe o {label_text.replace(':', '')}..."
            )
            entry.pack(pady=(0, 5), fill = "x")

            self.entradas[chave] = entry

        self.bt_salvar = ctk.CTkButton(
            self.root,
            text = "SALVAR NA PLANILHA",
            command = self.executar_envio,  # Chama a função abaixo
            font = ctk.CTkFont(size=15, weight="bold"),
            height = 50,
            fg_color = "#27ae60",
            hover_color = "#219150"
        )
        self.bt_salvar.pack(side="bottom", pady=20, padx=40, fill="x")

    def executar_envio(self):
        """Coleta os dados da interface e envia para o serviço da planilha."""

        # 1. Coleta os dados de todos os campos Entry
        dados_finais = {chave: entrada.get() for chave, entrada in self.entradas.items()}

        # 2. Validação simples: SCD e Item não podem estar vazios
        if not dados_finais.get('SCD') or not dados_finais.get('Item'):
            messagebox.showwarning("Aviso", "Por favor, preencha os campos SCD e Item!")
            return

        try:
            # 3. Feedback Visual: Desabilita o botão para evitar cliques duplos
            self.bt_salvar.configure(state="disabled", text="Enviando...")
            self.root.update()  # Força a interface a mostrar a mudança de texto

            # 4. Envia os dados para o motor (PlanilhaService)
            self.servico.inserir_registro(dados_finais)

            # 5. Sucesso!
            messagebox.showinfo("Sucesso", "Dados registrados com sucesso na planilha!")
            self.limpar_campos()

        except Exception as e:
            # 6. Trata erros (Ex: Internet caiu ou Planilha renomeada)
            messagebox.showerror("Erro de Rede", f"Não foi possível salvar os dados:\n{e}")

        finally:
            # 7. Restaura o botão independente de ter dado erro ou sucesso
            self.bt_salvar.configure(state="normal", text="SALVAR NA PLANILHA")

    def limpar_campos(self):
        """Limpa o texto de todas as caixas de entrada."""
        for entrada in self.entradas.values():
            entrada.delete(0, 'end')


