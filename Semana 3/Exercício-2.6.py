""" 
Primeiro, execute a atribuição
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
Agora, escreva duas expressões Python que são avaliadas, respectivamente,
como a primeiro e a última palavras em palavras, na ordem do dicionário.
"""
palavras = ['taco', 'bola', 'celeiro', 'cesta', 'peteca']
palavras.sort()
print(palavras)
print(palavras[0])
print(palavras[-1])

# Ou

primeira_palavra = sorted(palavras)[0]
ultima_palavra = sorted(palavras)[-1]

print("Primeira palavra:", primeira_palavra)
print("Última palavra:", ultima_palavra)

""" 
a função sorted() retorna uma nova lista ordenada, não modificando a lista original. Se você deseja modificar a lista original, pode usar o método sort() diretamente na lista
"""