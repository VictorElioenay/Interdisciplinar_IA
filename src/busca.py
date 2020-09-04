from nltk.tokenize import regexp_tokenize
from nltk.stem.snowball import SnowballStemmer
import math

class Busca(object):
    def __init__(self):
        super().__init__()
    
    def buscar(self,chave_busca,matriz):
        tokens_chave_busca = {}
        norma_matriz = {}
        norma_busca = 0
        escalar_matriz = {}

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

        for token in tokens_chave_busca:
            for url in matriz:
                escalar_matriz[url] = 0
                if(matriz[url].__contains__(token)):
                    escalar_matriz[url] += matriz[url][token] * tokens_chave_busca[token]
                else:
                    print("erro")
                # for token2 in matriz[url]:
    # Aqui
        result_final = [0,0,0,0,0]
        #result_final [posição] = valor 
        result_id = [0,0,0,0,0]
        #result_final [posição] = id hash
        aux_result = [0,0,0,0,0]
        # 0 valor, 1 id hash, 2 valor2, 3 id hash2
        for url in escalar_matriz:
            aux = escalar_matriz[url]/(norma_busca*norma_matriz[url])
            for i in range(5):
                if(aux > result_final[i]):
                    aux_result[0]=result_final[i]
                    aux_result[1]=result_id[i]
                    result_final[i]=aux
                    result_id[i]=url
                    i += 1
                    for i in range(i,5): 
                        aux_result[2]=result_final[i]
                        aux_result[3]=result_id[i]
                        result_final[i]=aux_result[0]
                        result_id[i]=aux_result[1]
                        aux_result[0]=aux_result[2]
                        aux_result[1]=aux_result[3]
                    break
        return result_id

        # resultados = []
        # dic = {}
        # for url in escalar_matriz:
        #     x = escalar_matriz[url]/(norma_busca*norma_matriz[url])
            # item = {url:x}
        
    # def sub(self,resultados,url,item,x):
    #     aux = item
    #     for i in range(resultados.__len__()):
    #         if(resultados[i].values()[0] < x ):
    #             aux = resultados[i].keys()[0]
    #     return {url:x}
    #     resultados.append({aux:x})
    #         r.append( {url : )
    #     pass
