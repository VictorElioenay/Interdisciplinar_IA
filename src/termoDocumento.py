from nltk.tokenize import regexp_tokenize

class TermoDocumento(object):
    def __init__(self):
        super().__init__()

    def contruir_matriz(self,tokens):
        termo_documento = {}
        with open("../links.txt") as arquivo:
            for url in arquivo:
                termo_documento[url] = tokens
        
        return termo_documento
    
    def preencher_matriz_tf(self,termo_documento):
        for link in termo_documento:
            url = link.strip('\n')
            url = url.replace("/","").replace("https:","")
            with open("../database/"+url+'.txt') as arquivo:     
                aux = regexp_tokenize(arquivo.read().lower(),pattern = "[a-zA-Z]+\w+")
                
                for token in termo_documento[link]:
                    termo_documento[link][token] = aux.count(token)
        
        return termo_documento

    def redefinir_matriz(self,termo_documento,tokens):
        v_idf = {}
        count = 0
        for token in tokens:
            for url in termo_documento:
                    if(termo_documento[url][token] != 0 ):
                        count+=1
            v_idf[token] = count
            count = 0