""" 
Comece executando as instruções de atribuição:

##>>> s1 = 'ant'
##>>> s2 = 'bat'
##>>> s3 = 'cod'

Escreva expressões Python usando s1, s2 e s3 e os operadores + e * a fim de
avaliar para:  


'ant bat cod'
ant ant ant ant ant ant ant ant ant ant'
'ant bat bat cod cod cod'
'ant bat ant bat ant bat ant bat ant bat ant bat ant bat'
'batbatcod batbatcod batbatcod batbatcod batbatcod'
"""
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1, s2, s3)
print((s1 + ' ') * 10)
print(s1, (s2 + ' ') * 2, (s3 + ' ') * 3)
print((s1, s2) * 7)
print((s2+s2+s3+ ' ') * 5)