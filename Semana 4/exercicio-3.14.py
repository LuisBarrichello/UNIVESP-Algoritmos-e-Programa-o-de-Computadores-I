"""
Implemente a função trocaPU(), que aceita uma lista como entrada e troca o primeiro e
último elementos da lista. Você pode considerar que a lista não estará vazia.
A função não deverá retornar nada.

>>> ingredientes = [’farinha’, ’açúcar’, ’manteiga’, ’maçãs’]
>>> trocaPU(ingredientes)
>>> ingredientes
[’maçãs’, ’açúcar’, ’manteiga’, ’farinha’]
"""
def trocaPU(lista):
    if len(lista) < 1:
        return 'Lista não pode ser fazia'
    
    if len(lista) >= 2:
        # Trocando o primeiro e o último elementos usando indexação
        lista[0], lista[-1] = lista[-1], lista[0]

ingredientes = ['farinha', 'açúcar', 'manteiga', 'maçãs']
trocaPU(ingredientes)
print(ingredientes)  # Saída: ['maçãs', 'açúcar', 'manteiga', 'farinha']