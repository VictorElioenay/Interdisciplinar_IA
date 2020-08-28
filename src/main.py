import requests
from extrator import Extrator
import re

# with open("../links.txt", "r") as arquivo:
#     for url in arquivo:
#         url = url.strip('\n')
#         if(Extrator().extrair_de(url)):
#             print("Texto extraido de",url)
Extrator().contruir_matriz()