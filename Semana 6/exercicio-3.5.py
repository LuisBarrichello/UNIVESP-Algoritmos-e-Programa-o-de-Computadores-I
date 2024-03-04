"""
Implemente um programa que solicite do usuário uma lista de palavras
(ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de
quatro letras nessa lista.

>>>
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare pote

"""

lista_palavras = input('Digite uma lista de palavras, separadas por espaço: ')

lista_palavras = lista_palavras.split()

for palavra in lista_palavras:
    if len(palavra) == 4:
        print(palavra)

