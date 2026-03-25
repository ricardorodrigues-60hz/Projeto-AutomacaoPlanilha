import tkinter as tk
from planilhaService import PlanilhaService
from planilhaGui import InterfaceAquisicao

if __name__ == "__main__":
    #Inicia o serviço de dados
    servico = PlanilhaService('credentials.json', 'Controle de Compras em Kanban')

    #Inicia a interface e passa o serviço para ela
    root = tk.Tk()
    app = InterfaceAquisicao(root, servico)
    root.mainloop()