import requests

awesome_api = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
requisicao = requests.get(awesome_api)
print(requisicao.json)

dolar_real = float(requisicao.json()["USDBRL"]["bid"])
euro_real = float(requisicao.json()["EURBRL"]["bid"])
bitcoin_real = float(requisicao.json()["BTCBRL"]["bid"])

valor_real = float(input("digite o valor em R$ "))

print(f"{valor_real:.2f} em dólar $ {valor_real / dolar_real:.2f}")
