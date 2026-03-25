import customtkinter as ctk
from planilhaService import PlanilhaService
from planilhaGui import InterfaceAquisicao

if __name__ == "__main__":
    servico = PlanilhaService('credentials.json', 'Controle de Compras em Kanban')
    root = ctk.CTk()
    app = InterfaceAquisicao(root, servico)
    root.mainloop()