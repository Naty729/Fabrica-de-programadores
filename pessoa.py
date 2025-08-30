
# Solicitando os dados para o cadastro 
nome_completo = input("Digite o nome: ")
email = input("Digite o e-mail: ")

# Criando o arquivo pessoa como txt para gravação dos dados 
arquivo = open("pessoa.txt", "a")
arquivo.write(f"{nome_completo} | {email}\n")
# Arquivo.write(nome_completo, "|" email)
arquivo.close()