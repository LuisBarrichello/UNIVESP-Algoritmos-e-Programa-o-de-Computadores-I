"""
Escreva a função negativos(), que aceita uma lista como entrada e exibe, um por
linha, os valores negativos na lista. A função não deverá retornar nada.

>>> negatives([4, 0, −1, −3, 6, −9])
-1
-3
-9
"""

def negativos(lista):
    """ 
    exibe os números negativos contidos na lista
    """
    for num in lista:
        if num < 0:
            print(num)

negativos([4, 0, -1, -3, 6, -9])

