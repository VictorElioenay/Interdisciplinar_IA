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
matriz_hash = TermoDocumento().contruir_matriz(tokens)
matriz_hash_tf = TermoDocumento().preencher_matriz_tf(matriz_hash)