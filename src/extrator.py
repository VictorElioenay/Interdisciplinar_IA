import requests
from nltk.tokenize import regexp_tokenize
import nltk
from nltk.stem.snowball import SnowballStemmer
import os
import re
import math
import io

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
        # conteudoFiltrado=conteudoFiltrado.encode("UTF-8").decode('UTF-8')
        open('../database/'+url+'.txt', "w").write(conteudoFiltrado.encode('ascii','ignore').decode('ascii','ignore'))

    def extrair_tokens(self):
        data = os.listdir("../database")
        aux = []
        tokens = {}
        
        for site in data:
            with open("../database/"+site) as arquivo:     
                aux += regexp_tokenize(arquivo.read().lower(),pattern = "[a-zA-Z]+\w+")
              
        stemmer = SnowballStemmer('portuguese')
        estemas = [stemmer.stem(aux) for aux in aux]
        
        for item in estemas:
            if(not(tokens.__contains__(item))):
                tokens[item] = 0

        #print(tokens) 
        return tokens