"""
Desenhe um diagrama representando o estado dos nomes e objetos após esta execução:

>>> a = [5, 6, 7]
>>> b = a
>>> a = 3
"""

  [5, 6, 7]  <-- b
    ↑
    |
    a

  3  <-- a
  [5, 6, 7]  <-- b

