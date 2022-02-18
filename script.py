import requests,re
from bs4 import BeautifulSoup


print('===== CONVERSOR DE MOEDA =====')
print('')
print('=-='*10)
num = float(input("Digite um valor em Real: R$ "))
print('=-='*10)
print('')

url = 'https://www.infomoney.com.br/ferramentas/cambio/'

coletando_dados = requests.get(url)
print("o status do codigo é ", coletando_dados.status_code)
print("\n")
soup = BeautifulSoup(coletando_dados.text,'lxml')

#FILTRANDO PELA TAG TBODY
tabela = str(soup.find("tbody"))
#FILTRANDO SOMENTE PELO NUMERO
valores_tabela = re.findall("[0,0-9]+", tabela)


#CAPTURANDO OS VALORES QUE IREI ULTILIZAR
dolar_str = valores_tabela[15]
euro_str = valores_tabela[18]
arg_str = valores_tabela[0]

subst1 = dolar_str.replace(",",".")
subst2 = euro_str.replace(",",".")
subst3 = arg_str.replace(",",".")


#FAZENDO A CONVERSÃO PARA FLOAT
dolar = float(subst1)
euro = float(subst2)
pesoArgentino = float(subst3)

usdbrl = round(num/dolar,3) 
eurbrl = round(num/euro, 3) 
argbrl = round(num/pesoArgentino,3)

print("\n O valor em Dólar é",usdbrl,"\n O valor em Euro é",eurbrl, "\n O valor em Peso Argentino é",arg_str)


