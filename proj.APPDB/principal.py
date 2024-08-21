from tkinter import *
import importlib.util
import sys
import os

class Principal:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", "20")
        self.janela.pack(padx=10, pady=10)

        self.titulo = Label(self.janela, text="Rotas", font=("Arial black", "25", "bold"))
        self.titulo.pack(pady=5)

        self.botoes = Frame(master)
        self.botoes.pack(padx=5, pady=10)
        self.usuario = Button(self.botoes, text="Usuários", font=self.fontepadrao, width=10, command=self.abrir_cadusuarios)
        self.usuario.pack(side=LEFT, padx=5)
        self.cidades = Button(self.botoes, text="Cidades", font=self.fontepadrao, width=10)
        self.cidades.pack(side=LEFT, padx=5)
        self.clientes = Button(self.botoes, text="Clientes", font=self.fontepadrao, width=10)
        self.clientes.pack(side=LEFT, padx=5)
        self.sair = Button(self.botoes, text="Sair", font=self.fontepadrao, width=10, command=master.quit)
        self.sair.pack(side=LEFT, padx=5)

    def abrir_cadusuarios(self):
        cadusuarios_path = os.path.join(os.path.dirname(__file__), "cadusuarios.py")

        if os.path.exists(cadusuarios_path):
            spec = importlib.util.spec_from_file_location("cadusuarios", cadusuarios_path)
            cadusuarios = importlib.util.module_from_spec(spec)
            sys.modules["cadusuarios"] = cadusuarios
            spec.loader.exec_module(cadusuarios)
        else:
            print(f"Arquivo {cadusuarios_path} não encontrado!")

root = Tk()
app = Principal(root)
root.state("zoomed")
root.mainloop()
