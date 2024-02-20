temp_celsius = eval(input('Digite a temperatura em celsius: '))

def calcular_temperatura_de_fa_celsius(temperatura_celsius):
    temp_fahrenheit = 1.8 * temperatura_celsius + 32
    print(temp_fahrenheit, 'graus Fahrenheit.')
    return temp_fahrenheit

calcular_temperatura_de_fa_celsius(temp_celsius)