""" 
Escreva expressões algébricas Python correspondentes aos seguintes comandos:  

A soma dos 5 primeiros inteiros positivos.
A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).
O número de vezes que 73 cabe em 403.
O resto de quando 403 é dividido por 73.
2 à 10ª potência.
O valor absoluto da distância entre a altura de Sara (54 polegadas) e a
altura de Mark (57 polegadas).
O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
"""

##A soma dos 5 primeiros inteiros positivos.
soma = 1 + 2 + 3 + 4 + 5
print(soma)
## ou

##A range()função retorna uma sequência de números, começando em 0 por padrão, aumentando em 1 (por padrão) e parando antes de um número especificado.
soma1 = sum(range(1,6))
print(soma1)


##A idade média de Sara (idade 23), Mark (idade 19) e Fátima (idade 31).

mediaIdades = (23 + 19 + 31) / 3
## ou
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

def calcular_media_idade(pessoas):
    total_idades = sum(pessoa.idade for pessoa in pessoas)
    return total_idades / len(pessoas)

sara = Pessoa('Sara', 23)
mark = Pessoa('Mark', 19)
fatima = Pessoa('Fátima', 31)

pessoas = [sara, mark, fatima]

media_idades = calcular_media_idade(pessoas)
print("A idade média é:", int(media_idades))


##O número de vezes que 73 cabe em 403.
result = 403 // 73
print(result)

## O resto de quando 403 é dividido por 73.
result_resto = 403 % 73
print(result)

## 2 à 10ª potência.
result_potencia = 2**10
print(result_potencia)


##O valor absoluto da distância entre a altura de Sara (54 polegadas) e a altura de Mark (57 polegadas).
altura_sara = 54
altura_mark = 57

distancia_absoluta = abs(altura_sara - altura_mark)
print(distancia_absoluta)

## O menor preço entre os seguintes preços: R$ 34,99, R$ 29,95 e R$ 31,50.
precos = [34.99, 29.95, 31.50]
menor_preco = min(precos)
print("O menor preço é: R$", menor_preco)