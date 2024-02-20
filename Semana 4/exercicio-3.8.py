"""
Defina, diretamente no shell interativo, a função média(), que aceita dois
números como entrada e retorna a média dos números. Um exemplo de uso é:

>>> average(2, 3.5)
2.75
"""
def calcular_media(num1, num2):
    """ 
    retorna a média de x e y
    """
    media = num1 + num2 / 2
    return media

print(calcular_media(2, 3.5))