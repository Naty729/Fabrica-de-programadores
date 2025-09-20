try:
    base = int(input("Digite a base para ver sua tabuada: "))
    inicio = int(input("Digite o início da tabuada: "))
    fim = int(input("Digite o fim da tabuada: "))
    i = 1

    print(f"Tabuada do {base}")
    while i <= fim:
    if i >= inicio:
        print(f"{base} x {i} = {base * i}")
    i += 1

except ValueError:
    print("entrada invalida! por favor digite numeros inteiros para a base, inicio e fim.")

except Exception as e: 
    print("ocorreu um erro inesperado: (e). por favor, tente novamente")
