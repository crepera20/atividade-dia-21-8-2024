from tkinter import *

class usuarios:
    def __init__(self, master=None):
        self.janela = Frame(master)
        self.fontepadrao = ("Arial", "20")
        self.janela.pack(padx=10, pady=10)

        self.titulo = Label(self.janela, text="Informe os dados", font=("Arial black", "25", "bold"))
        self.titulo.pack(pady=5)

        self.idUsuario = Frame(master)
        self.idUsuario.pack(padx=10, pady=10)
        self.idLabel = Label(self.idUsuario, text="idUsuario: ", font=self.fontepadrao)
        self.idLabel.pack(side=LEFT)
        self.id_entry = Entry(self.idUsuario, width=13, font=self.fontepadrao)
        self.id_entry.pack(side=LEFT)
        self.botaobuscar = Button(self.idUsuario, text="Buscar", font=self.fontepadrao, width=12, command=self.verificarusuarios)
        self.botaobuscar.pack(side=LEFT)

        self.nome = Frame(master)
        self.nome.pack(padx=10, pady=10)
        self.nomeLabel = Label(self.nome, text="Nome:", font=self.fontepadrao)
        self.nomeLabel.pack(side=LEFT)
        self.nome_entry = Entry(self.nome, width=30, font=self.fontepadrao)
        self.nome_entry.pack(side=LEFT)

        self.telefone = Frame(master)
        self.telefone.pack(padx=10, pady=10)
        self.telefoneLabel = Label(self.telefone, text="Telefone:", font=self.fontepadrao)
        self.telefoneLabel.pack(side=LEFT)
        self.telefone_entry = Entry(self.telefone, width=28, font=self.fontepadrao)
        self.telefone_entry.pack(side=LEFT)

        self.email = Frame(master)
        self.email.pack(padx=10, pady=10)
        self.emailLabel = Label(self.email, text="E-mail:", font=self.fontepadrao)
        self.emailLabel.pack(side=LEFT)
        self.email_entry = Entry(self.email, width=30, font=self.fontepadrao)
        self.email_entry.pack(side=LEFT)

        self.Usuario = Frame(master)
        self.Usuario.pack(padx=10, pady=10)
        self.usuarioLabel = Label(self.Usuario, text="Usuario:", font=self.fontepadrao)
        self.usuarioLabel.pack(side=LEFT)
        self.usuario_entry = Entry(self.Usuario, width=29, font=self.fontepadrao)
        self.usuario_entry.pack(side=LEFT)

        self.janela3 = Frame(master)
        self.janela3["padx"] = 20
        self.janela3.pack(padx=10, pady=10)
        self.senhaLabel = Label(self.janela3, text="Senha:", font=self.fontepadrao)
        self.senhaLabel.pack(side=LEFT)
        self.senha = Entry(self.janela3)
        self.senha["width"] = 30
        self.senha["font"] = self.fontepadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)

        self.botoes = Frame(master)
        self.botoes.pack(padx=5, pady=10)
        self.inserir = Button(self.botoes, text="Inserir", font=self.fontepadrao, width=10)
        self.inserir.pack(side=LEFT, padx=5)
        self.alterar = Button(self.botoes, text="Alterar", font=self.fontepadrao, width=10)
        self.alterar.pack(side=LEFT, padx=5)
        self.excluir = Button(self.botoes, text="Excluir", font=self.fontepadrao, width=10)
        self.excluir.pack(side=LEFT, padx=5)

        self.msg = Label(self.janela, text="", font=self.fontepadrao)
        self.msg.pack(pady=5)

    def verificarusuarios(self):
        usuario = self.id_entry.get()
        if usuario == "me mama":
            self.msg["text"] = "Usuario encontrado"
        else:
            self.msg["text"] = "Usuario não encontrado"

root = Tk()
app = usuarios(root)
root.state("zoomed")
root.mainloop()