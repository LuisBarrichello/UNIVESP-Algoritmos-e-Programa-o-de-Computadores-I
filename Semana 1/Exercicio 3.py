'''
Realizar a leitura dos valores de quatro notas escolares bimestrais de um aluno
representadas pelas variáveis N1, N2, N3 e N4. Calcular a média aritmética
(variável MD) desse aluno e apresentar a mensagem “Aluno Aprovado com média” se a
média obtida for maior ou igual a 5; caso contrário, apresentar a mensagem “Aluno
Reprovado com média”. Informar também, após a apresentação das mensagens, o valor
da média obtida pelo aluno.
'''

nota_1 = float(input('Nota:'))
nota_2 = float(input('Nota:'))
nota_3 = float(input('Nota:'))
nota_4 = float(input('Nota:'))

def calculaMedia(nota_1: float, nota_2: float, nota_3: float, nota_4: float):
    media = (nota_1 + nota_2 + nota_3 + nota_4) / 4
    return media

resultado = calculaMedia(nota_1, nota_2, nota_3, nota_4)

if resultado >= 5:
    print('Aluno Aprovado com média ', resultado)
else:
    print('Aluno Reprovado com média ', resultado)