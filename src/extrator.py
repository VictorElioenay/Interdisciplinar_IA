import requests
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
                raise ConnectionError
        except ConnectionError as e:
            print(e)
    
    def __filtro(self,content,url):
        conteudoFiltrado = re.sub("<[^>]*>", "", content)
        url = url.replace('https://')
        url = url.replace("/","")
        open('../database/'+url+'.txt', "w").write(conteudoFiltrado)
