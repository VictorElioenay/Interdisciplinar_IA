import requests
from extrator import Extrator
from termoDocumento import TermoDocumento
from busca import Busca
import re

class Controller(object):
    def __init__(self):
        super().__init__()
        self.matriz = None

    def gerarBase(self,path):
        # with open(path, "r") as arquivo:
        #     for url in arquivo:
        #         url = url.strip('\n')
        #         if(Extrator().extrair_de(url)):
        #             print("Texto extraido de",url)
        
        tokens = Extrator().extrair_tokens()
        data = TermoDocumento().contruir_matriz(tokens)
        self.matriz = TermoDocumento().preencher_matriz_tf(data['matriz'])
        TermoDocumento().redefinir_matriz(self.matriz, tokens, data['n_documentos'])

    def buscar(self,chave_busca): 
        return Busca().buscar(chave_busca,self.matriz)
        
