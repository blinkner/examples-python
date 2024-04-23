# -*- coding: utf-8 -*-
# Faça um programa que receba duas notas digitadas pelo usuário.
# Se a nota for maior ou igual a seis, escreva aprovado, senão escreva reprovado.

def media(x,y):
    return (x+y)/2

nota1 = int(input("Entre com a primeira nota: "))
nota2 = int(input("Entre com a segunda nota: "))

nota_final = media(nota1, nota2)

if nota_final >= 6:
    print("APROVADO!")
else:
    print("REPROVADO!")