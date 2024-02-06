'''
Ler uma temperatura em graus Celsius e apresentá-la convertida
em graus Fahrenheit. A fórmula de conversão é F ← C * 9 / 5 + 32,
sendo F a temperatura em Fahrenheit e C a temperatura em Celsiu
'''

temperatura_celsius = float(input('Digite a temperatura para conversao em Fahrenheit:  '))

def conversaoDeTemperaturaParaFahrenheit(temperatura_celsius):
    temperatura_fahrenheit = temperatura_celsius * 9 / 5 + 32
    return temperatura_fahrenheit

resultado = conversaoDeTemperaturaParaFahrenheit(temperatura_celsius)
print('A temperatura em Fahrenheit é:', resultado)