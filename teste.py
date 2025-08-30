try:
    num1 = int(input("digite um numero: "))
    num2 = int(input("digite outro numero: "))

    resultado = num1/ num2 
    print(f"o resultado da divisão é {resultado}")
# caso o ereo seja por algum valor não numerico (digitar teste)
except ValueError:
    print("digite algarismos numericos")
# caso o erro seja da divisão por zero
except ZeroDivisionError: 
    Print("divisão por zero não é permitida")
# caso o erro seja outro não tratados anteriormente 
except:
    print("digite numeros validos")

