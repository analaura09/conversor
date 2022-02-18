import requests

print('===== CONVERSOR DE MOEDA =====')
print('')
print('=-='*10)
num = float(input("Digite um valor em Real: R$ "))
print('=-='*10)
print('')

url = "http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,ARS-BRL"


coletando_dados = requests.get(url)
data = coletando_dados.json()

#COLETANDO O VALOR DO DOLAR
dolar_str = data['USDBRL']['high']

#COLETANDO O VALOR DO EURO
euro_str = data['EURBRL']['high']

#COLETANDO O VALOR DO PESO ARGENTINO
pesoArgentino_str = data['ARSBRL']['high']

#CONVERTENDO STRING PARA VALORES DO TIPO FLOAT
dolar = float(dolar_str)
euro = float(euro_str)
pesoArgentino = float(pesoArgentino_str)

#CONVERTENDO O NUMERO RECEBIDO NO INPUT PARA DOLAR/EURO/PESO ARGENTINO
usd = (round(num/dolar,2))
eur = (round(num/euro,2))
ars = (round(num/pesoArgentino,2))

print(f"o valor de R${num} em Dolar é",usd)
print(f"o valor de R${num} em Euro é",eur)
print(f"o valor de R${num} em Peso Argentino é",ars)