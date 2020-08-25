import requests
import re

arquivo = open("./links.txt", "r")

def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == 200:
        with open(endereco, 'w') as novo_arquivo:
                novo_arquivo.write(resposta.url + resposta.text)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        print(resposta)
        print("Deu ruim em baixar: " + url)

## Aqui a gente baixa os arquivos
with open("./links.txt", "r") as file:
    count = 0
    for line in file:
        count += 1
        line = line.replace("\n", "")
        line = line.replace("\u7530", "")
        baixar_arquivo(line, './downloads/'+ str(count) +'.txt')

## Filtro de tags ***Temos problemas com a função do webhost***
file2 = open('./downloads/1.txt', "r")
conteudo = file2.read()
conteudoFiltrado = re.sub("<[^>]*>", "", conteudo)
open('./database/1.txt', "w").write(conteudoFiltrado)
