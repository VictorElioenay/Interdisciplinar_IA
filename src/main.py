import requests
from extrator import Extrator
import re

with open("../links.txt", "r") as arquivo:
    for url in arquivo:
        Extrator().extrair_de(url)
