# -*- coding: utf-8 -*-

# Coleta os dados
autor = input("Autor: ")
titulo = input("Título: ")
ano = str(int(input("Ano: ")))
link = input("Link: ")
acesso = input("Dia de acesso: ")

# Inverte o nome do autor
autor = autor.split(" ")
autor = autor[1].upper() + ", " + autor[0]

# Cria a referência
referencia = autor + ". " + titulo + ". " + ano + ". " + "Disponível em: " + link + ". " + "Acesso em: " + acesso + "."

print("\n")
print(referencia)