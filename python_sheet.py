import numpy
import math
import random

print("Olá, Mundo!")
random.random() # Float aleatório entre 0 e 1.
random.uniform(0, 10) # Float aleatório entre 0 e 10.
random.randint(0, 10) # Inteiro aleatório entre 0 e 10.
random.randrange(0, 10, 2) # Inteiro aleatório entre 0 e 10 com passo 2.
random.choice([6, 20, 50]) # Valor aleatorio de uma lista
range(inicio, fim, passo)
list()
input("Entre com um valor: ") # Entrada de dados

# Manipulação de arquivos
arquivo = open("arquivo.txt", "a") # Abre o arquivo ("r" para ler, "w" para escrever, "a" para ler e escrever)
texto_completo = arquivo.read() # Lê o texto do arquivo
linhas = arquivo.readlines() # Retorna as linhas do arquivo
arquivo.write("Esse é o meu arquivo\n") # Escreve no arquivo
arquivo.close() # Fecha o arquivo

# Tratamento de erros
try:
    print(2/0)
except:
    print("Não é permitida divisão por 0")

def soma(x, y): # Função
    return x+y

# Função enumerate
lista = ["abacate", "bola", "cachorro"]
for i, nome in enumerate(lista):
    print(i, nome)