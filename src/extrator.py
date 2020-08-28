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
        url = url.replace("/","").replace("https:","")
        open('../database/'+url+'.txt', "w").write(conteudoFiltrado)

    def extrair_tokens(self):
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