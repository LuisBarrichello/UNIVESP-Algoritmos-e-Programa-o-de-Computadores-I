"""
Implemente a função perímetro(), que aceita, como entrada, o raio de um círculo
(um número não negativo) e retorna o perímetro do círculo. Você deverá escrever sua
implementação em um módulo chamado perímetro.py. Um exemplo de uso é:

>>> perimeter(1)
6.283185307179586
"""
import math

def calcular_perimetro(raio):
    perimetro = 2 * math.pi * raio
    return perimetro

print(calcular_perimetro(15))