#Escreva expressões Python correspondentes ao seguinte:
import math

# O comprimento da hipotenusa em um triângulo retângulo cujos dois outros lados têm comprimentos a e b
def calcular_hipotenusa(a,b):
    hipotenusa = math.sqrt(a**2 + b**2) #sqrt calcula a raiz quadrada
    return hipotenusa

# Exemplo de uso:
lado_a = 3
lado_b = 4
hipotenusa = calcular_hipotenusa(lado_a, lado_b)
print("A hipotenusa é:", hipotenusa)

# O valor da expressão que avalia se o comprimento da hipotenusa acima é 5
hipotenusa_maior_que_cinco = hipotenusa > 5

# A área de um disco com raio a
def calcular_area_circular(raio_a):
    area_circular = math.pi * raio_a**2
    return area_circular

# Exemplo de uso:
raio_a = 10
area_circular = calcular_area_circular(raio_a)
print('Area do circulo é: ', int(area_circular))

# O valor da expressão Booleana que verifica se um ponto com coordenadas x e y está dentro de um círculo com centro ( a, b ) e raio r 
""" A fórmula para calcular a distância entre dois pontos (x2, y1) e (x2, y2)
distancia = Raiz Quadrada de (x2 - x1)**2 + (y2 - y1)**2
"""

def ponto_esta_dentro_do_circulo(x, y, a, b, raio):
    distancia_centro_ponto = math.sqrt((x - a)**2 + (y - b)**2)
    return distancia_centro_ponto <= raio

# Exemplo de uso:
centro_x = 0
centro_y = 0
raio = 5
ponto_x = 3
ponto_y = 4

esta_dentro = ponto_esta_dentro_do_circulo(ponto_x, ponto_y, centro_x, centro_y, raio)
print("O ponto está dentro do círculo:", esta_dentro) # True