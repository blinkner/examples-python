#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:03:38 2024

@author: lqsoliveira
"""
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
from matplotlib.ticker import LinearLocator
plt.close('all')
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

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
nvar = 2 #número de variáveis
gen = 0 #contador do número de gerações
genmax = 40 #número máximo de gerações (repetições do processo de busca SGA)
pc = 0.75 # limiar taxa de cruzamento. Sugestão 0.65 <= pc <=0.8
pm = 0.025 # limiar taxa de mutação. Sugestão: 0.01 <= pm <= 0.05


#Inicialização da população em binário
pop_2 = np.random.randint(0,2,(popsize,nbits * nvar))

pop_10 = np.empty((popsize, nvar)) #população em número real
pop_10.fill(np.nan) #limpeza da memória, configurando-a como nan
pop_10_x = np.empty(popsize) #população em número real
pop_10_x.fill(np.nan) #limpeza da memória, configurando-a como nan
pop_10_y = np.empty(popsize) #população em número real
pop_10_y.fill(np.nan) #limpeza da memória, configurando-a como nan
f = np.empty(popsize) #função fitness ou função custo -- população candidata
f.fill(np.nan) #limpeza da memória, configurando-a como nan
ff = np.empty(popsize) #função fitness ou função custo -- população filhos
ff.fill(np.nan) #limpeza da memória, configurando-a como nan

f_best = np.empty((genmax, nvar)) # Variável para plotagem no gráfico f_best x gen.
f_best.fill(np.nan)

pop_y = np.empty((popsize,nbits * nvar)) #população selecionada -- pais
pop_f = np.empty((popsize,nbits * nvar)) #população criada do cruzamento -- filhos

#Avaliação da função objetiva
X = np.arange(-40, 40, 0.01) #criando os pontos do domínio da função custo, x\in[-40, 40]
Y = np.arange(-40, 10, 0.01) #criando os pontos do domínio da função custo, x\in[-40, 10]
X, Y = np.meshgrid(X, Y)
Z = 0.4/(1+0.02*((X+20)**2 + (Y+20)**2)) + 0.2/(1+0.5*((X+1)**2 + (Y+5)**2)) +0.15/(1+0.03*((X-30)**2 + (Y+30)**2))

#Etapa de Avaliação da População Inicial
for i in range(popsize):
    for j in range(nvar):
        if j == 0:
            pop_10[i][j] = b2r(pop_2[i][0:12],-40,40) #conversão binário para real
            pop_10_x[i] = pop_10[i][j]
        else:
            pop_10[i][j] = b2r(pop_2[i][12:24],-40,10) #conversão binário para real
            pop_10_y[i] = pop_10[i][j]
    f[i] = 0.4/(1+0.02*((pop_10[i][0]+20)**2 + (pop_10[i][1]+20)**2)) + 0.2/(1+0.5*((pop_10[i][0]+1)**2 + (pop_10[i][1]+5)**2)) +0.15/(1+0.03*((pop_10[i][0]-30)**2 + (pop_10[i][1]+30)**2)) #implementação da função custo


#print(pop_10)

#Etapa de plotagem da população inicial
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_xlim(-40,40)
ax.set_ylim(-40,10)
ax.set_zlim(0,0.5)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

colors = ('k')
c_list = []
for c in colors:
    c_list.extend([c] * 40)

ax.scatter(pop_10_x, pop_10_y, f, c=c_list)

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
            #print('pai 01')
            #print(pop_y[p1,:])
            #print('pai 02')
            #print(pop_y[p2,:])
            #print("índice l:",l)
            
            #Realização do cruzamento -- obtenção dos filhos
            pop_f[i,0:l] = pop_y[p1,0:l]
            pop_f[i,l:nbits] =pop_y[p2,l:nbits]
            pop_f[i,nbits:nbits + l] = pop_y[p1,nbits:nbits + l]
            pop_f[i,nbits + l:] =pop_y[p2,nbits + l:]

            pop_f[i+1,0:l] = pop_y[p2,0:l]
            pop_f[i+1,l:] =pop_y[p1,l:]
            pop_f[i+1,nbits:nbits + l] = pop_y[p2,nbits:nbits +l]
            pop_f[i+1,nbits + l:] =pop_y[p1,nbits + l:]
            
            #Impressão dos filhos gerados -- Etapa de conferência do código
            #print('novo pop_y[i]')
            #print(pop_f[i,:])
            #print(pop_f[i+1,:])
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
            #print('filho 01')
            #print(pop_f[i])

            #Realização da mutação
            pop_f[i][j] = 1 - pop_f[i][j]
            pop_f[i][nbits + j] = 1 - pop_f[i][j]

            #Impressão do filho após mutação - Etapa de conferência do código
            #print('novo filho')
            #print(pop_f[i])

        #Rotina de mutação para o segundo filho
        if np.random.rand()<= pm:
            j = np.random.randint(0,nbits) #sorteio do índice para mutação de gene do segundo filho
            
            #Impressão do filho que receberá mutação - Etapa de conferência do código
            #print('filho 02')
            #print(pop_f[i+1])

            #Realização da mutação
            pop_f[i+1][j] = 1 - pop_f[i+1][j]
            pop_f[i+1][nbits + j] = 1 - pop_f[i+1][j]

            #Impressão do filho após mutação - Etapa de conferência do código
            #print('novo filho')
            #print(pop_f[i+1])
        ########################################################

    #Etapa de avaliação da função fitness --  População de Filhos
    ff.fill(np.nan) #limpeza da memória, configurando-a como nan
    for i in range(popsize):
        for j in range(nvar):
            if j == 0:
                pop_10[i][j] = b2r(pop_f[i][0:12],-40,40) #conversão binário para real
                pop_10_x[i] = pop_10[i][j]
            else:
                pop_10[i][j] = b2r(pop_f[i][12:24],-40,10) #conversão binário para real
                pop_10_y[i] = pop_10[i][j]
        ff[i] = 0.4/(1+0.02*((pop_10[i][0]+20)**2 + (pop_10[i][1]+20)**2)) + 0.2/(1+0.5*((pop_10[i][0]+1)**2 + (pop_10[i][1]+5)**2)) +0.15/(1+0.03*((pop_10[i][0]-30)**2 + (pop_10[i][1]+30)**2)) #implementação da função fitness

    #Etapa de seleção da nova geração
    for i in range(popsize):
        if f[i]<ff[i]: #condição para seleção do filho
            pop_2[i] =pop_f[i] #filho, sendo incluído na população candidata
            f[i] =ff[i] #atualização da função custo
        else: 
            pass
    
    # Atualiza a população decimal escolhida
    for i in range(popsize):
        for j in range(nvar):
            if j == 0:
                pop_10[i][j] = b2r(pop_2[i][0:12],-40,40) #conversão binário para real
                pop_10_x[i] = pop_10[i][j]
            else:
                pop_10[i][j] = b2r(pop_2[i][12:24],-40,10) #conversão binário para real
                pop_10_y[i] = pop_10[i][j]

    f_best[gen] = max(f)
    gen+=1 #atualização do contador de gerações


fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#Etapa de plotagem da população inicial
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_xlim(-40,40)
ax.set_ylim(-40,10)
ax.set_zlim(0,0.5)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

ax.scatter(pop_10_x, pop_10_y, f, c=c_list)

plt.show()

pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima:')
print('x_best=',pop_10[pos])
print('f_best',f[pos])

plt.figure()
plt.plot(np.arange(0,genmax),f_best,'b')
plt.grid()
plt.ylabel('f(x)')
plt.xlabel('geração')
plt.show()

#print(pop_10)
