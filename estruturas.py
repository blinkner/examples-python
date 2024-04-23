# -*- coding: utf-8 -*-
x = 1
y = 2
lista1 = [1,2,3,4,5]
lista2 = ["ola","mundo","!"]
lista3 = [0,"ola","biscoito","bolacha",9.99]

# Condicionais
if x == y:
    print("numeros iguais")
elif y > x:
    print("y maior que x")
else:
    print("y é maior que x")

# Repetição
while x < 10:
    print(x)
    x += 1

for i in lista2:
    print(i)

for i in range(10,20,2): # (inicio, fim, passo)
    print(i)