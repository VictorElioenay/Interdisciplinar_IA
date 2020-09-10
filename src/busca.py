from nltk.tokenize import regexp_tokenize
from nltk.stem.snowball import SnowballStemmer
import math

#Feito por Luiz Gustavo Chinelato Setten, Pedro Henrique Borges Prado, Victor Elioenay Santos Narciso, Yuri PSS Da Silva
class Busca(object):
    def __init__(self):
        super().__init__()
    
    def buscar(self,chave_busca,matriz):
        tokens_chave_busca = {}
        norma_matriz = {}
        norma_busca = 0
        escalar_matriz = {}
        resultados = []

        chave_busca = regexp_tokenize(chave_busca,pattern = "[a-zA-Z]+\w+")
        stemmer = SnowballStemmer('portuguese')
        estemas = [stemmer.stem(chave_busca) for chave_busca in chave_busca]

        for token in estemas:
            if not(tokens_chave_busca.__contains__(token)):
                tokens_chave_busca[token] = estemas.count(token)

        for token in tokens_chave_busca:
            norma_busca += tokens_chave_busca[token]**2
        norma_busca = math.sqrt(norma_busca)

        for url in matriz:
            auxiliar = 0
            for token in matriz[url]:
                auxiliar += matriz[url][token]**2
            norma_matriz[url] = math.sqrt(auxiliar)

        for url in matriz:
            escalar_matriz[url] = 0
            for token in tokens_chave_busca:
                if(matriz[url].__contains__(token)):
                    escalar_matriz[url] += matriz[url][token] * tokens_chave_busca[token]
                else:
                    print("erro")
    
        for url in escalar_matriz:
            x = escalar_matriz[url]/(norma_busca*norma_matriz[url])
            item = {url:x}
            for i in range(resultados.__len__()):
                if( list(resultados[i].values())[0] < list(item.values())[0] ):
                    aux = resultados[i]
                    resultados[i] = item
                    item = aux
            resultados.append(item)
        
        return resultados