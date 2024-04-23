# -*- coding: utf-8 -*-

# 'r' para ler, 'w' para escrever, 'a' para ler e escrever

arquivo = open("arquivo.txt")
# linhas = arquivo.readlines()
texto_completo = arquivo.read()
arquivo.close()

print(texto_completo)

w = open("arquivo.txt","a")
w.write("Esse é o meu arquivo\n")
w.close()