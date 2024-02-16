""" 
Dada a lista de notas de trabalho de casa dos alunos

#>>> notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

escreva:

Uma expressão que avalia para o número de 7 notas.
Uma instrução que muda a última nota para 4.
Uma expressão que avalia para a nota mais alta.
Uma instrução que classifica as notas da lista.
Uma expressão que avalia para a média das notas.
"""

notas = [9, 7, 7, 10, 3, 9, 6, 6, 2]

#Uma expressão que avalia para o número de 7 notas.
quantidade_de_setes = notas.count(7)
print("Número de notas 7:", quantidade_de_setes)

#Uma instrução que muda a última nota para 4.
notas[-1] = 4
print("Última nota modificada para 4:", notas[-1])

#Uma expressão que avalia para a nota mais alta.
nota_mais_alta = max(notas)
print("Nota mais alta:", nota_mais_alta)

#Uma instrução que classifica as notas da lista.
notas.sort()
print("Notas ordenadas:", notas)adas)

#Uma expressão que avalia para a média das notas.
media = sum(notas) / len(notas)
print("Média das notas:", media)