from nltk.tokenize import regexp_tokenize
from nltk.stem.snowball import SnowballStemmer
import math

class TermoDocumento(object):
    def __init__(self):
        super().__init__()

    def contruir_matriz(self,tokens):
        termo_documento = {}
        count = 0
        with open("../links.txt") as arquivo:
            for url in arquivo:
                termo_documento[url] = tokens
                count+=1
        
        return { "matriz" : termo_documento, "n_documentos" : count}
    
    def preencher_matriz_tf(self,termo_documento):
        for link in termo_documento:
            url = link.strip('\n')
            url = url.replace("/","").replace("https:","")
            with open("../database/"+url+'.txt') as arquivo:     
                aux = regexp_tokenize(arquivo.read().lower(),pattern = "[a-zA-Z]+\w+")
                
                stemmer = SnowballStemmer('portuguese')
                estemas = [stemmer.stem(aux) for aux in aux]
                
                for token in termo_documento[link]:
                    termo_documento[link][token] = estemas.count(token)
               
        return termo_documento

    def redefinir_matriz(self,termo_documento,tokens,n_documentos):
        v_idf = {}
        count = 0
        total_sites = n_documentos

        for token in tokens:
            for url in termo_documento:
                if(termo_documento[url][token] != 0 ):
                    count+=1
            if(count != 0):   
                v_idf[token] = math.log(total_sites/count,10)
            else:
                print(token)
            count = 0

        for token in tokens:
            for url in termo_documento:
                feq = termo_documento[url][token]
                if(feq != 0):
                    tf = 1 + math.log(feq,10)
                else:
                    tf = 0
                termo_documento[url][token] = tf * v_idf[token]