import tkinter as tk
from tkinter import messagebox


class InterfaceAquisicao:
    def __init__(self, root, servico_planilha):
        self.root = root
        self.servico = servico_planilha
        self.root.title("Cadastro de Aquisição v1.0")
        self.root.geometry("450x600")

        # Configuração de Labels e Campos de Entrada
        self.campos_info = [
            ("SCD:", "scd"), ("ID Item:", "id"), ("OS:", "os"),
            ("Data Previsto (dd/mm/aaaa):", "previsto"), ("Nome do Item:", "item"),
            ("Quantidade:", "qtde"), ("Valor Unitário:", "valor_uni"),
            ("Fornecedor:", "fornecedor"), ("Observações:", "obs")
        ]

        self.entradas = {}

        # Criar os campos dinamicamente
        for label_text, chave in self.campos_info:
            tk.Label(self.root, text=label_text, font=("Arial", 10, "bold")).pack(pady=2)
            entry = tk.Entry(self.root, width=45)
            entry.pack(pady=2)
            self.entradas[chave] = entry

        # Botão de Ação
        self.btn_salvar = tk.Button(
            self.root, text="SALVAR NA PLANILHA", font=("Arial", 12, "bold"),
            bg="#27ae60", fg="white", command=self.executar_envio, pady=10
        )
        self.btn_salvar.pack(pady=25)

    def executar_envio(self):
        # Coleta dados dos inputs
        dados_finais = {chave: entry.get() for chave, entry in self.entradas.items()}

        if not dados_finais['item'] or not dados_finais['previsto']:
            messagebox.showwarning("Atenção", "Preencha ao menos o Item e a Data!")
            return

        try:
            self.servico.inserir_registro(dados_finais)
            messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")
            self.limpar_tela()
        except Exception as e:
            messagebox.showerror("Erro Crítico", f"Erro ao conectar: {e}")

    def limpar_tela(self):
        for entry in self.entradas.values():
            entry.delete(0, tk.END)

if __name__ == "__main__":
    # Criamos uma classe "Mock" (de mentira) para simular o serviço da planilha
    class MockService:
        def inserir_registro(self, dados):
            print(f"Simulando envio para o Google: {dados}")

    root = tk.Tk()
    # Passamos o serviço de mentira para a interface
    app = InterfaceAquisicao(root, MockService())
    root.mainloop()