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

#Declaração das variáveis

popsize = 15 #número de indivíduos da população
gen = 0 #contador do número de gerações
genmax = 50 #número máximo de gerações (repetições do processo de busca SGA)
n_filhos = 30
sigma = 0.1
lim_sup = 2
lim_inf = -1

pop = np.empty(popsize) #população em número real
pop.fill(np.nan) #limpeza da memória, configurando-a como nan
f = np.empty(popsize) #função fitness ou função custo -- população candidata
f.fill(np.nan) #limpeza da memória, configurando-a como nan
ff = np.empty(popsize) #função fitness ou função custo -- população filhos
ff.fill(np.nan) #limpeza da memória, configurando-a como nan

f_best = np.empty((genmax, 1)) # Variável para plotagem no gráfico f_best x gen.
f_best.fill(np.nan)

pop_y = np.empty(n_filhos + popsize) #população selecionada -- pais
pop_f = np.empty(n_filhos) #população criada do cruzamento -- filhos
pop_f.fill(np.nan)

#Avaliação da função objetiva
x= np.arange(-1,2.001,0.001) #criando os pontos do domínio da função custo, x\in[-1,2]
y= x*np.sin(10*np.pi*x) + 2 #calculando a imagem de x, ou seja, f(x).

#Etapa de Avaliação da População Inicial
for i in range(popsize):
    pop[i] = np.random.uniform(lim_inf, lim_sup) #conversão binário para real
    f[i] = pop[i]*np.sin(10*np.pi*pop[i]) + 2 #implementação da função custo

#Avaliação da solução ótima (primeira geração)
pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima da primeira geração:')
print('x_best=',pop[pos])
print('f_best',f[pos])

#Etapa de plotagem da população inicial
plt.figure()
plt.plot(x,y,'b') #plot da função no domínio em avaliação.
plt.plot(pop,f,'r*') #plot dos indivíduos da primeira geração
plt.grid()
plt.show()

#---------------------------------------------------------#

""" Início de execução do loop principal do SGA"""

#---------------------------------------------------------#

while (gen<genmax):
    #rotina de seleção dos pais
    for i in range(n_filhos):
        p1 = np.random.randint(0, popsize) # seleciona o pai 1
        p2 = np.random.randint(0, popsize) # seleciona o pai 2

        pop_f[i] = (pop[p1] + pop[p2]) / 2 # faz o cruzamento utilizando a média dos pais
        pop_f[i] = pop_f[i] + sigma * np.random.normal(0, 1) # faz a mutação normal
        if pop_f[i] > 2 or pop_f[i] < -1: # verifica se o filho está entre os limites para puni-lo
            pop_f[i] = 1.550

    pop_y = np.concatenate((pop, pop_f)) # agrupa os pais e filhos em um array
    f_y = pop_y*np.sin(10*np.pi*pop_y)+2 # calcula a função custo

    for i in range(popsize): # busca os melhores indivíduos para manter na população
        pos= f_y.argmax()
        pop[i] = pop_y[pos]
        f[i] = f_y[pos]
        f_y[pos] = -1000

    f_best[gen] = max(f)
    gen+=1 #atualização do contador de gerações
    
#Avaliação da solução ótima
pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima:')
print('x_best=',pop[pos])
print('f_best',f[pos])

plt.figure()
plt.plot(x,y,'b') #plot da função no domínio em avaliação.
plt.plot(pop,f,'r*') #plot dos indivíduos da primeira geração
plt.grid()
plt.show()

# Define as gerações a serem plotadas no gráfico.
x = np.linspace(0, genmax, genmax, endpoint=True)

# Plota o gráfico do melhor valor custo por geração.
plt.figure()
plt.plot(x, f_best, 'r')
plt.title('Melhor valor custo por geração')
plt.ylim((0,4))
plt.xlabel('gen')
plt.ylabel('f_best')
plt.grid()
plt.show()