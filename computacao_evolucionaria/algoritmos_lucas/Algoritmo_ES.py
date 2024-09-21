#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 20:09:55 2024

@author: lqsoliveira
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

##############################################
#Execução do Passo 1: Declaração das variáveis

popsize = 15 #número de indivíduos da população
gen = 0 #contador do número de gerações
genmax = 50 #número máximo de gerações (repetições do processo de busca SGA)
lambd = 30 #numero filhos
sigma = 0.1 #desvio padrão usado na mutação

pop_mu = np.empty(popsize) #população em número real
pop_mu.fill(np.nan) #limpeza da memória, configurando-a como nan

fmu = np.empty(popsize) #função fitness ou função custo -- população candidata
fmu.fill(np.nan) #limpeza da memória, configurando-a como nan

f_best = np.empty(genmax) #memória melhor função custo
f_best.fill(np.nan) #limpeza da memória, configurando-a como nan

pop_y = np.empty(lambd) #população criada do cruzamento -- filhos
pop_y.fill(np.nan)

#Avaliação da função objetiva
x= np.arange(-1,2.001,0.001) #criando os pontos do domínio da função custo, x\in[-1,2]
y= x*np.sin(10*np.pi*x) + 2 #calculando a imagem de x, ou seja, f(x).


##################################################################
#Execução do Passo 2: Criação da população geração 0

pop_mu = np.random.uniform(-1,2,popsize)
fmu = pop_mu*np.sin(10*np.pi*pop_mu)+2

#Etapa de plotagem da população inicial
plt.figure()
plt.plot(x,y,'b') #plot da função no domínio em avaliação.
plt.plot(pop_mu,fmu,'r*') #plot dos indivíduos da primeira geração
plt.grid()
plt.show()

while gen<genmax:
    ##################################################################
    #Execução do Passo 3: Cruzamento intermediário
    for i in range(lambd):
        x1 = np.random.randint(0,popsize)
        x2 = np.random.randint(0,popsize)
        pop_y[i] = (pop_mu[x1]+pop_mu[x2])/2
    
    ##################################################################
    #Execução do Passo 4: Mutação Normal
    
    for i in range(lambd):
        pop_y[i] = pop_y[i] + sigma*np.random.normal(0,1)
        if pop_y[i] >2 or pop_y[i] <-1: #penalização
            pop_y[i] = 1.95
        
    
    ##################################################################
    #Execução do Passo 5: Seleção  -- Método (mu+sigma)-ES
    
    pop = np.concatenate((pop_mu,pop_y))
    f_pop = pop*np.sin(10*np.pi*pop)+2
    
    for i in range(popsize):
        pos= f_pop.argmax()
        pop_mu[i] = pop[pos]
        fmu[i] = f_pop[pos]
        f_pop[pos] = -1000
    
    f_best[gen] = fmu[0]
    gen = gen + 1

pos = fmu.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima:')
print('x_best=',pop_mu[pos])
print('f_best',fmu[pos])

plt.figure()
plt.plot(x,y,'b') #plot da função no domínio em avaliação.
plt.plot(pop_mu,fmu,'r*') #plot dos indivíduos da primeira geração
plt.grid()
plt.show()

plt.figure()
plt.plot(np.arange(0,genmax),f_best,'b')
plt.grid()
plt.ylabel('f(x)')
plt.xlabel('Geração')
plt.show()