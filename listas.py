# -*- coding: utf-8 -*-

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista_2 = [70,6,20,1,2]
minha_lista_3 = ["abacaxi", 2, 9.89, True]

print(minha_lista[2])

for item in minha_lista_3:
    print(item)

minha_lista.append("limão") # adiciona um elemento na lista

print(minha_lista)

if 3 in minha_lista_2:
    print("3 está na lista")

del minha_lista[2:] # apaga elementos da lista

minha_lista_4 = [] # lista vazia
minha_lista_4.append(57)
print(minha_lista_4)

minha_lista_2.sort() # ordena a lista ou (reverse=True)
# minha_lista_2 = sorted(minha_lista_2) # ordena a lista mas como retorno
minha_lista_2.reverse() # inverte a lista
print(minha_lista_2)

# Dicionários
dicionario = {"A":"Ameixa", "B":"Bola", "C":"Cachorro"}
print(dicionario["A"])

for i in dicionario.items(): # retorna tupla com os valores
    print(i)
for i in dicionario.values(): # retorna os valores
    print(i)
for i in dicionario.keys(): # retorna as chaves
    print(i)