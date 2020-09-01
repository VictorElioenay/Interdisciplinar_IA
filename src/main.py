import requests
from extrator import Extrator
from termoDocumento import TermoDocumento
import re

# with open("../links.txt", "r") as arquivo:
#     for url in arquivo:
#         url = url.strip('\n')
#         if(Extrator().extrair_de(url)):
#             print("Texto extraido de",url)

tokens = Extrator().extrair_tokens()
hashh = TermoDocumento().contruir_matriz(tokens)
matriz_hash = TermoDocumento().preencher_matriz_tf(hashh['matriz'])
TermoDocumento().redefinir_matriz(matriz_hash, tokens, hashh['n_documentos'])

# for url in matriz_hash:
#     for tokens in matriz_hash[url]:
#         print(url)
#         print(matriz_hash[url])
#         break
#     break
#     # print('\n')