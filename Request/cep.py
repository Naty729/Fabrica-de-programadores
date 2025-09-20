import requests 

cep = input("digite seu cep: ")
Via_cep = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(Via_cep)

print(requisicao)

print(f"CEP: {requisicao.json()["cep"]}")
print(f"RUA: {requisicao.json()["logradouro"]}")
print(f"CEP: {requisicao.json()["bairro"]}")
print(f"LOCALIDADE: { requisicao.json()["localidade"]}")
print(f"CEP: {requisicao.json()["estado"]}")