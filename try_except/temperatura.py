try:
    print("Converte Celsius para Fahrenheit")

    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32

    print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}°F')

except ValueError: 
    print("entrada invalida. por favor, digite um valor numerico para a tempetura")

except Exception as e: 
    print(f"ocorreu um erro inesperado: (e). por favor, tente novamente.")