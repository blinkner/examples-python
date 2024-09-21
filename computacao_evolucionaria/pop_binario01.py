#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:03:38 2024

@author: lqsoliveira
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#Funções

def b2r(x,a,b):
    """A função b2r converte um número binário em número real. Em que:
    x é um array contendo o número binário (indivíduo)
    a é o limite inferior do domínio real
    b é o limite superior do domínio real"""
    d = 0 #variável auxiliar, somador.
    nbits = len(x) #busca pelo tamanho do array de bits
    for i in range((nbits-1), -1,-1): 
        d = d + x[i]*2**(nbits-1 -i) # implementação do somatório da Eq(8)
    return d/(2**nbits)*(b-a)+a #implementação da Eq(8)

#Declaração das variáveis

popsize = 40 #número de indivíduos da população
nbits = 12 #número de bits que define um indivíduo.
gen = 0 #contador do número de gerações
genmax = 40 #número máximo de gerações (repetições do processo de busca SGA)
pc = 0.75 # limiar taxa de cruzamento. Sugestão 0.65 <= pc <=0.8
pm = 0.025 # limiar taxa de mutação. Sugestão: 0.01 <= pm <= 0.05


#Inicialização da população em binário
pop_2 = np.random.randint(0,2,(popsize,nbits))

pop_10 = np.empty(popsize) #população em número real
pop_10.fill(np.nan) #limpeza da memória, configurando-a como nan
f = np.empty(popsize) #função fitness ou função custo -- população candidata
f.fill(np.nan) #limpeza da memória, configurando-a como nan
ff = np.empty(popsize) #função fitness ou função custo -- população filhos
ff.fill(np.nan) #limpeza da memória, configurando-a como nan

f_best = np.empty((genmax, 1)) # Variável para plotagem no gráfico f_best x gen.
f_best.fill(np.nan)

pop_y = np.empty((popsize,nbits)) #população selecionada -- pais
pop_f = np.empty((popsize,nbits)) #população criada do cruzamento -- filhos

#Avaliação da função objetiva
x= np.arange(-1,2.001,0.001) #criando os pontos do domínio da função custo, x\in[-1,2]
y= x*np.sin(10*np.pi*x) + 2 #calculando a imagem de x, ou seja, f(x).

#Etapa de Avaliação da População Inicial
for i in range(popsize):
    pop_10[i] = b2r(pop_2[i,:],-1,2) #conversão binário para real
    f[i] = pop_10[i]*np.sin(10*np.pi*pop_10[i]) + 2 #implementação da função custo

#Avaliação da solução ótima (primeira geração)
pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima da primeira geração:')
print('x_best=',pop_10[pos])
print('f_best',f[pos])

#Etapa de plotagem da população inicial
plt.figure()
plt.plot(x,y,'b') #plot da função no domínio em avaliação.
plt.plot(pop_10,f,'r*') #plot dos indivíduos da primeira geração
plt.grid()
plt.show()

#---------------------------------------------------------#

""" Início de execução do loop principal do SGA"""

#---------------------------------------------------------#

while (gen<genmax):
    p = f/np.sum(f) #cálculo da função custo relativo (normalizado) Eq(9)
    pop_y.fill(np.nan) #limpeza da memória, configurando-a como nan
    
    #rotina de seleção dos pais, método da roleta
    for i in range(popsize): 
        x_rand = np.random.rand() #sorteio de um valor aleatório
        soma = 0 #variável auxiliar, acumulador
        j = 0 #variável auxiliar, contador
        while (soma<x_rand): #loop de implementação do método da roleta
            soma += p[j] #atualização do acumulador
            j+=1 #atualização do contador
        pop_y[i]=pop_2[j-1] #pai selecionado
    
    pop_f.fill(np.nan) #limpeza da memória, configurando-a como nan
    
    #Rotina de implementação do cruzamento e mutação
    for i in range(0,popsize,2):
        if np.random.rand()>= pc: #condição de avaliação do limiar de cruzamento
            p1 = np.random.randint(0,popsize) #seleção do primeiro pai
            p2 = np.random.randint(0,popsize) #seleção do segundo pai
            l = np.random.randint(0,nbits) #sorteio do índice para troca dos genes
            #Impressão dos pais -- Etapa de conferência do código
            print('pai 01')
            print(pop_y[p1,:])
            print('pai 02')
            print(pop_y[p2,:])
            print("índice l:",l)
            
            #Realização do cruzamento -- obtenção dos filhos
            pop_f[i,0:l] = pop_y[p1,0:l]
            pop_f[i,l:] =pop_y[p2,l:]
            pop_f[i+1,0:l] = pop_y[p2,0:l]
            pop_f[i+1,l:] =pop_y[p1,l:]
            
            #Impressão dos filhos gerados -- Etapa de conferência do código
            print('novo pop_y[i]')
            print(pop_f[i,:])
            print(pop_f[i+1,:])
        else: #Em caso de não atendimento a condição de cruzamento, os pais se tornam os filhos
            p1 = np.random.randint(0,popsize)
            p2 = np.random.randint(0,popsize)
            pop_f[i] = pop_y[p1]
            pop_f[i+1] = pop_y[p2]
        #######################################################
        #Rotina de mutação para o primeiro filho
        if np.random.rand()<= pm:
            j = np.random.randint(0,nbits) #sorteio do índice para mutação de gene do primeiro filho
            
            #Impressão do filho que receberá mutação - Etapa de conferência do código
            print('filho 01')
            print(pop_f[i])

            #Realização da mutação
            pop_f[i][j] = 1 if pop_f[i][j] == 0 else 0

            #Impressão do filho após mutação - Etapa de conferência do código
            print('novo filho')
            print(pop_f[i])

        #Rotina de mutação para o segundo filho
        if np.random.rand()<= pm:
            j = np.random.randint(0,nbits) #sorteio do índice para mutação de gene do segundo filho
            
            #Impressão do filho que receberá mutação - Etapa de conferência do código
            print('filho 02')
            print(pop_f[i+1])

            #Realização da mutação
            pop_f[i+1][j] = 1 if pop_f[i+1][j] == 0 else 0

            #Impressão do filho após mutação - Etapa de conferência do código
            print('novo filho')
            print(pop_f[i+1])
        ########################################################

    #Etapa de avaliação da função fitness --  População de Filhos
    ff.fill(np.nan) #limpeza da memória, configurando-a como nan
    for i in range(popsize):
        pop_10[i] = b2r(pop_f[i,:],-1,2) #conversão binário para real
        ff[i] = pop_10[i]*np.sin(10*np.pi*pop_10[i]) + 2 #cálculo da função fitness
    
    #Etapa de seleção da nova geração
    for i in range(popsize):
        if f[i]<ff[i]: #condição para seleção do filho
            pop_2[i] =pop_f[i] #filho, sendo incluído na população candidata
            f[i] =ff[i] #atualização da função custo
        else: 
            pass

    for i in range(popsize):
        pop_10[i] = b2r(pop_2[i,:],-1,2) #conversão binário para real

    f_best[gen] = max(f)
    gen+=1 #atualização do contador de gerações
    
#Avaliação da solução ótima
pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima:')
print('x_best=',pop_10[pos])
print('f_best',f[pos])

plt.figure()
plt.plot(x,y,'b') #plot da função no domínio em avaliação.
plt.plot(pop_10,f,'r*') #plot dos indivíduos da primeira geração
plt.grid()
plt.show()

# Define as gerações a serem plotadas no gráfico.
x = np.linspace(0, genmax, genmax, endpoint=True)

# Plota o gráfico do melhor valor custo por geração.
plt.figure()
plt.plot(x, f_best, 'r*')
plt.title('Melhor valor custo por geração')
plt.ylim((0,4))
plt.xlabel('gen')
plt.ylabel('f_best')
plt.grid()
plt.show()