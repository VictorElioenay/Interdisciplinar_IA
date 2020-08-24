import requests
import re
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import FirefoxProfile

lista_links = open("lista.txt",'r') # From where get the website's links

regex_rule = '(<[^><]*>)' # Match any HTML tag
regex_rule_script = '(<script[^><]*>)' # Match <script> tag
# ...

for link in lista_links:
    r = requests.get(link)
    # Filter
    text_split = r.text.split("</head>")
    new_text = re.sub(regex_rule,'',text_split[1])
    print(new_text)