x=2
y=3
print('x=', x, 'y=', y, sep='--', end='...')


z = input('Digite valor de z: ')
print(type(z))



eval('3') # 3 number
eval('3 + 4') # 7
eval('len([1,2,3])') # 3
eval('3 > 4') # False



# Função que calcula o preço de um produto atualizado pela taxa de juros:
def juros(preco, juros): 
    res = preco * (1 + (juros / 100))
    print(res)
    return res

juros(10, 50)


def f(x):
    res = x ** 2 + 1
    print(res)
    return res

f(5)