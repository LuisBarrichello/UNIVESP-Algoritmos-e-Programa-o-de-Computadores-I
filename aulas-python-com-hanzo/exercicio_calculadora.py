""" calculadora 

# + - / *

laço enquanto for verdadeiro faça :
n1
n2
operadores


se soma = n1 + n2

se sub = n1 - n2


se div = n1 / n2


se mult = n1 * n2

caso deseje continuar ( s/n) se sim retorna e faz outro calculo se não para o programa

continuar  = input("deseja continuar? ( s/n ): ")
if continuar.lowe() != "s":
    break

"""
def calculo_aritmetico(operacao, n1, n2):
    if operacao == 'soma':
        print('Resultado: ', n1 + n2)
    elif operacao == 'subtração':
        print('Resultado: ', n1 - n2)
    elif operacao == 'divisão':
        print('Resultado: ', n1 / n2)
    elif operacao == 'multiplicação':
        print('Resultado: ', n1 * n2)
    elif operacao == 'exponenciação':
        print('Resultado: ', n1 ** n2)


deseja_continuar = True
while deseja_continuar:
    operacao = input('Qual operação aritmetica você deseja fazer? (soma, divisão, subtração, multiplicação, expenenciacão?) ')
    
    if operacao not in ['soma', 'divisão', 'subtração', 'multiplicação', 'exponenciação']:
        print('Operação inválida. Digite uma operação válida.')
        break

    n1 = eval(input('Digite primeiro número: '))
    n2 = eval(input('Digite segundo numero número: '))

    calculo_aritmetico(operacao, n1, n2)

    deseja_continuar = input('Deseja continuar? (sim/não) ')

    if deseja_continuar.lower() != 'sim':
        break
    
