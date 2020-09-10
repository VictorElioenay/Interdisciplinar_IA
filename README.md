# Buscador Gluglu :turkey:
Projeto de Inteligência Artificial 1s/2020 desenvolvido no IFSULDEMINAS - Campus Poços de Caldas, o projeto visa a extração de informações de páginas web, tokenização, radicalização, estemerização e indexação de acordo com relevância do conteúdo das páginas.

## Instalação:

### Requisitos
* Python 3 instalado [Python](https://python.org)
* Bibliotecas NLTK, requests e tkinter instaladas
  
O atual projeto utiliza as bibliotecas requests, mltk e tkinter (esta última já vem instalada na versão mais recente do Python 3)

As bibliotecas requests e nltk devem ser instaladas por meio dos seguintes comandos:
~~~ Python
 pip install requests
 pip install nltk
~~~
ou
~~~Python3
 pip3 install requestes
 pip3 install nltk
~~~

Caso seja necesário (se ele não vier na instalação padrão do Python) é possível instalar o tkinter pelo seguinte comando:
~~~ Python
 pip install tkinter
~~~
ou
~~~Python3
 pip3 install tkinter
~~~

## Utilização:

### Para iniciar o projeto 
~~~ Python
 python src/interface.py
~~~

O banco de dados local fica dentro da pasta `./database/` caso queira utilizar um banco de dados diferente pode alterar o arquivo `./links.txt` ou fazer um outro e depois selecione-o com o borão de "Carregar" na interface gráfica, coloque apenas um link por linha denne arquivo. O download das páginas web pode demorar, é possível acompanhar o processo pelo console (Terminal, CMD, PowerShell) em que o programa está sendo executado, durante o download e o processamento das informações a interface pode ficar ociosa.

## Contato 
Qualquer prolema informe-nos

 * [Luiz Gustavo Chinelato Setten](mailto:luiz.setten@alunos.ifsuldeminas.edu.br)
 * [Pedro Henrique Borges Prado](mailto:pedro.prado@alunos.ifsuldeminas.edu.br)
 * [Victor Elioenay Santos Narciso](mailto:victor.narciso@alunos.ifsuldeminas.edu.br)
 * [Yuri PSS da Silva](mailto:yuri.silva@alunos.ifsuldeminas.edu.br)