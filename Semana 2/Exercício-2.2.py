""" 
Traduza os comandos a seguir para expressões Booleanas em Python e avalie-as:

A soma de 2 e 2 é menor que 4.
O valor de 7 // 3 é igual a 1 + 1.
A soma de 3 ao quadrado e 4 ao quadrado é igual a 25.
A soma de 2, 4 e 6 é maior que 12.
1387 é divisível por 19.
31 é par. (Dica: o que o resto lhe diz quando você divide por 2?)
O preço mais baixo dentre R$ 34,99, R$ 29,95 e R$ 31,50 é menor que R$ 30,00.*
"""

expressao1 = 2 + 2 > 4
expressao2 = 7 // 3 == 1 + 1
expressao3 = 3**2 + 4**2 == 25
expressao4 = 2 + 4 + 6 > 12
expressao5 = 1387 % 19 == 0
print(expressao1, expressao2, expressao3, expressao4, expressao5)


if 31 % 2 == 0:
    print('é par')
else:
    print('é impar')

precos = [34.99, 29.95, 31.50]
menor_preco = min(precos)
print(menor_preco < 30)