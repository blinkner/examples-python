import numpy as np
import math
import random
from functools import reduce

print("Olá, Mundo!")

random.random() # Float aleatório entre 0 e 1.
random.uniform(0, 10) # Float aleatório entre 0 e 10.
random.randint(0, 10) # Inteiro aleatório entre 0 e 10.
random.randrange(0, 10, 2) # Inteiro aleatório entre 0 e 10 com passo 2.
random.choice([6, 20, 50]) # Valor aleatorio de uma lista.

range(0, 10, 2) # Retorna uma sequência e inteiros de 0 a 10 com passo 2.
map(funcao, [1, 2, 3]) # Aplica uma função em cada elemento de uma lista, transformando-a em um objeto.
reduce(funcao, [1, 2, 3]) # Aplica uma função de forma iterativa a cada dois items de uma lista.
list() # Transforma um objeto em uma lista.

input("Entre com um valor: ") # Entrada de dados.

# Manupulação de strings
frase = "Olá" + ", " + "Mundo!" # Concatenação
len(frase) # Tamanho de uma string
frase[0] # Índice
frase[0:7] # Índice
frase.lower() # Minúsculas
frase.upper() # Maiúsculas
frase.strip() # Retira espaços e quebras no final
frase.split(" ") # Separa uma string
frase.find("Mundo") # Retorna a posição de uma palavra
frase.replace("Mundo", "Python") # Substitui uma palavra

# Manipulação de arquivos
arquivo = open("arquivo.txt", "a") # Abre o arquivo ("r" para ler, "w" para escrever, "a" para ler e escrever)
texto_completo = arquivo.read() # Lê o texto do arquivo
linhas = arquivo.readlines() # Retorna as linhas do arquivo
arquivo.write("Esse é o meu arquivo\n") # Escreve no arquivo
arquivo.close() # Fecha o arquivo

# Listas
lista = ["abacaxi", 2, 9.89, True]
lista.append("limão") # Adiciona item a lista
del lista[2:] # Apaga itens da lista
lista.sort() # Ordena a lista ou (reverse=True)
sorted(lista) # Ordena a lista como retorno
lista.reverse() # Inverte a lista

# Dicionários
dicionario = {"A":"Ameixa", "B":"Bola", "C":"Cachorro"}
for i in dicionario.items(): # Retorna tupla com os valores
    print(i)
for i in dicionario.values(): # Retorna os valores
    print(i)
for i in dicionario.keys(): # Retorna as chaves
    print(i)

# List Comprehension
x = [1, 2, 3, 4, 5]
y = [i**2 for i in x] # Valores elevados ao quadrado
z = [i for i in x if i%2==1] # Valores ímpares

# Estrutura condicional
x = 1
y = 2
if x == y:
    print("numeros iguais")
elif y > x:
    print("2 maior que 1")
else:
    print("2 menor que 1")

# Estruturas de repetição
x = 0
while x < 10:
    print(x)
    x += 1

for i in [0,"ola","biscoito","bolacha",9.99]:
    print(i)

for i in range(10,20,2): # (inicio, fim, passo)
    print(i)

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

# Função zip (concatena listas)
lista1 = [1,2,3,4,5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$ 2,00", "R$ 5,00", "N/A", "N/A", "N/A"]
for numero, nome, valor in zip(lista1, lista2, lista3):
    print(numero, nome, valor)