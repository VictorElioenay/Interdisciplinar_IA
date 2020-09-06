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

        self.labelLinks = []

    def inserirDB(self):
        filename = askopenfilename()
        self.buscar["text"] = "Aguarde"
        self.controller.gerarBase(str(filename))
        self.databaseLabel["text"] = str(filename)
        self.buscar["command"] = self.buscador
        self.buscar["text"] = "Buscar"
        
        self.clearLabelLinks()
       
    #Método realizar a busca
    def buscador(self):
        chaveBusca = self.chaveBusca.get()
        database = self.databaseLabel["text"]

        self.clearLabelLinks()

        if chaveBusca == "" or database == "":
            self.mensagem["text"] = "A chave de busca e/ou a base de dados não pode ser nulas"

        else:
            self.mensagem["text"] = ""
            resultados = self.controller.buscar(chaveBusca)
            resultados_links = []
            
            if(list(resultados[0].values())[0] == 0):
                self.mensagem["text"] = "Nenhum site encontrado"
            else:
                for i in resultados:
                    resultados_links.append(i.popitem()[0])
                
                for i in range(5):
                    self.labelLinks.append(Label(root, text=str(i+1)+"º: "+resultados_links[i], fg="blue", cursor="hand2"))
                    self.labelLinks[i].pack()
                
                self.labelLinks[0].bind('<Button-1>',lambda e : callback(resultados_links[0]) )
                self.labelLinks[1].bind('<Button-1>',lambda e : callback(resultados_links[1]) )
                self.labelLinks[2].bind('<Button-1>',lambda e : callback(resultados_links[2]) )
                self.labelLinks[3].bind('<Button-1>',lambda e : callback(resultados_links[3]) )
                self.labelLinks[4].bind('<Button-1>',lambda e : callback(resultados_links[4]) )
                    
    def clearLabelLinks(self):
        for i in self.labelLinks:
            i.destroy()
        self.labelLinks.clear()

root = Tk(className="Buscador")
Application(master=root)
root.mainloop()

