import requests
from nltk.tokenize import regexp_tokenize
import nltk
from nltk.stem.snowball import SnowballStemmer
import os
import re

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
        open('../database/'+url+'.txt', "w", errors='ignore').write(conteudoFiltrado)

    def  create_column(self):
        data = os.listdir("../database")
        aux = []
        tokens = {}
        
        for site in data:
            with open("../database/"+site, errors='ignore') as arquivo:     
                aux += regexp_tokenize(arquivo.read(),pattern = "[a-zA-Z]+\w+")

        
        stemmer = SnowballStemmer('portuguese')
        estemas = [stemmer.stem(aux) for aux in aux]
        print(estemas)

        for item in aux:
            if(not(tokens.__contains__(item.lower()))):
                tokens[item.lower()] = 0
         
        return tokens

    def contruir_matriz(self):
        termo_documento = {}
        tokens = self.create_column()
        with open("../links.txt", errors='ignore') as arquivo:
            for link in arquivo:
                termo_documento[link] = tokens
        #print(termo_documento)
