from tkinter import *
from tkinter.filedialog import askopenfilename
from controller import Controller
import webbrowser

def callback(url):
    webbrowser.open_new(url)

class Application:
    def __init__(self, master=None):
        self.master = master
        self.controller = Controller()

        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Buscador Gluglu")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()



        self.buscar = Button(self.segundoContainer)
        self.buscar["text"] = "Carregar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar["command"] = self.inserirDB
        self.buscar.pack()

        self.databaseLabel = Label(self.segundoContainer, text="", font=self.fontePadrao)
        self.databaseLabel.pack(side=LEFT)

        self.chaveBuscaLabel = Label(self.terceiroContainer, text="Busca", font=self.fontePadrao)
        self.chaveBuscaLabel.pack(side=LEFT)

        self.chaveBusca = Entry(self.terceiroContainer)
        self.chaveBusca["width"] = 30
        self.chaveBusca["font"] = self.fontePadrao
        self.chaveBusca.pack(side=LEFT)

        self.buscar = Button(self.quartoContainer)
        self.buscar["text"] = "Buscar"
        self.buscar["font"] = ("Calibri", "8")
        self.buscar["width"] = 12
        self.buscar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

        self.link1 = Label(root, text="", fg="blue", cursor="hand2")
        self.link1.pack()

        self.link2 = Label(root, text="", fg="blue", cursor="hand2")
        self.link2.pack()

        self.link3 = Label(root, text="", fg="blue", cursor="hand2")
        self.link3.pack()

        self.link4 = Label(root, text="", fg="blue", cursor="hand2")
        self.link4.pack()

        self.link5 = Label(root, text="", fg="blue", cursor="hand2")
        self.link5.pack()

    def inserirDB(self):
        filename = askopenfilename()
        self.buscar["text"] = "Aguarde"
        self.controller.gerarBase(str(filename))
        self.databaseLabel["text"] = str(filename)
        self.buscar["command"] = self.buscador
        self.buscar["text"] = "Buscar"

    #Método realizar a busca
    def buscador(self):
        chaveBusca = self.chaveBusca.get()
        database = self.databaseLabel["text"]

        self.link1["text"] = "" 
        self.link2["text"] = ""
        self.link3["text"] = ""
        self.link4["text"] = ""
        self.link5["text"] = ""

        if chaveBusca == "" or database == "":
            self.mensagem["text"] = "A chave de busca e/ou a base de dados não pode ser nulas"

        else:
            self.mensagem["text"] = ""
            resultados = self.controller.buscar(chaveBusca)

            try:
                for i in range(5):
                    resultados[i] = resultados[i].replace("\n", "")
            except:
                if(resultados[0] == 0):
                    self.mensagem["text"] = "Nenhum site encontrado"

            # link1 = Label(root, text="1°: " + resultados[0], fg="blue", cursor="hand2")
            self.link1["text"] = "1°: " + resultados[0]
            self.link1.bind("<Button-1>", lambda e: callback(resultados[0]))

            self.link2["text"] = "2°: " + resultados[1]
            self.link2.bind("<Button-1>", lambda e: callback(resultados[1]))

            self.link3["text"] = "3°: " + resultados[2]
            self.link3.bind("<Button-1>", lambda e: callback(resultados[2]))

            self.link4["text"] = "4°: " + resultados[3]
            self.link4.bind("<Button-1>", lambda e: callback(resultados[3]))

            self.link5["text"] = "5°: " + resultados[4] + "\n"
            self.link5.bind("<Button-1>", lambda e: callback(resultados[4]))

root = Tk(className="Buscador")
Application(master=root)
root.mainloop()

