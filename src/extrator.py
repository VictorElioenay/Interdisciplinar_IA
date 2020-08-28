import requests
from nltk.tokenize import regexp_tokenize
import os
import re
import math

class Extrator(object):

    def __init__(self):
        super().__init__()

    def extrair_de(self,url):
        try:
            resposta = requests.get(url)
            if resposta.status_code == 200:
                self.__filtro(resposta.text,url)
            else:
                raise requests.RequestException
        except requests.RequestException as e:
            print('Erro!!')
            return False
        return True
    
    def __filtro(self,content,url):
        conteudoFiltrado = re.sub("<style[^~]*>[^+]*</style>|<script[^~]*>[^~]*</script>|<[^>]*>", "", content)
        url = url.replace("https://","")
        url = url.replace("/","")
        open('../database/'+url+'.txt', "w").write(conteudoFiltrado)

    def  extrair_tokens(self):
        data = os.listdir("../database")
        aux = []
        tokens = {}
        
        for site in data:
            with open("../database/"+site) as arquivo:     
                aux += regexp_tokenize(arquivo.read(),pattern = "[a-zA-Z]+\w+")
              
        #Radicalização Faltando
    
        for item in aux:
            if(not(tokens.__contains__(item.lower()))):
                tokens[item.lower()] = 0
         
        return tokens

    def contruir_matriz(self):
        termo_documento = {}
        tokens = self.extrair_tokens()
        with open("../links.txt") as arquivo:
            for url in arquivo:
                termo_documento[url] = tokens
        
        self.preencher_matriz_tf(termo_documento)
    
    def preencher_matriz_tf(self,termo_documento):
        for link in termo_documento:
            url = link
            url = url.replace("https://","")
            url = url.replace("/","")
            url = url.strip('\n')
            aux_lower = []
            with open("../database/"+url+'.txt') as arquivo:     
                aux = regexp_tokenize(arquivo.read(),pattern = "[a-zA-Z]+\w+")
                
                for item in aux:
                    aux_lower.append(item.lower())
                    
                for token in termo_documento[link]:
                    termo_documento[link][token] = aux_lower.count(token)
              
    def redefinir_matriz(self,termo_documento):
        V_idf = []
        count = 0
        for url in termo_documento:
            for token in termo_documento[url]:
                if(termo_documento[url][token] != 0 ):
                    count+=1
                break
                V_idf.append()

        # { 
        #    http://dfsdfsdid.com : {  'talvez' : 10, 'mais ': 3  } ,
        #    http://eitah.com : {  'talvez' : 10, 'mais ': 3  }
        # }