""" 
Em que ordem os operadores nas expressões a seguir são avaliados?


2 + 3 == 4 or a >= 5
lst[1] * -3 < -10 == 0
(lst[1] * -3 < -10) in [0, True]
2 * 3**2
4 / 2 in [1, 2, 3]

"""

2 + 3 == 4 or a >= 5
""" Primeiro, a adição é realizada: 2 + 3 = 5.
Em seguida, a igualdade é verificada: 5 == 4 (False).
Então, a desigualdade é verificada: a >= 5.
Finalmente, a operação or é aplicada entre os resultados das duas comparações.
"""

lst[1] * -3 < -10 == 0
""" Primeiro, o elemento na posição 1 da lista é multiplicado por -3: lst[1] * -3.
Em seguida, a comparação é feita: lst[1] * -3 < -10.
Depois, a igualdade é verificada: -10 == 0.
Finalmente, a operação == é aplicada entre os resultados das duas comparações. """


(lst[1] * -3 < -10) in [0, True]
""" Primeiro, a multiplicação é realizada: lst[1] * -3.
Em seguida, a comparação é feita: lst[1] * -3 < -10.
Depois, é verificado se o resultado da comparação está presente na lista [0, True]. """


2 * 3**2
""" Primeiro, a potência é calculada: 3**2 = 9.
Em seguida, a multiplicação é realizada: 2 * 9. """


4 / 2 in [1, 2, 3]
""" Primeiro, a divisão é calculada: 4 / 2 = 2.
Em seguida, é verificado se o resultado da divisão está presente na lista [1, 2, 3]. """