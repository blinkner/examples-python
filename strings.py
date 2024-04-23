# -*- coding: utf-8 -*-
a = "Gabriel"
b = "Marlon"
c = "O rato roeu a roupa do rei de roma"

concatenar = a + " " + b # concatenação
print(concatenar)

tamanho = len(concatenar) # tamanho de uma string
print(tamanho)

print(a[0]) # índice
print(concatenar[0:7])

print(concatenar.lower()) # minúscula
print(concatenar.upper()) # maiúscula

print(concatenar.strip()) # retira espaços e quebras no final
print(c.split(" ")) # separa uma string

busca = c.find("rei") # busca uma palavra e retorna sua posição
print(c[busca:])

c = c.replace("o rei","a rainha") # substitui uma palavra
print(c)