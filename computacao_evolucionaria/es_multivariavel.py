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
Fcusto = lambda X,Y: (9 * np.sin(X)*np.sin(Y)) / (X * Y)

#Declaração das variáveis

popsize = 15 #número de indivíduos da população
nvar = 2
gen = 0 #contador do número de gerações
genmax = 40 #número máximo de gerações (repetições do processo de busca SGA)
n_filhos = 30
sigma = 0.1
lim_sup = np.array([8, -0,1])
lim_inf = np.array([0.1, -10])

pop = np.empty((popsize,nvar)) #população em número real
pop.fill(np.nan) #limpeza da memória, configurando-a como nan

pop_t = np.empty((nvar, popsize))
pop_t.fill(np.nan)

f = np.empty(popsize) #função fitness ou função custo -- população candidata
f.fill(np.nan) #limpeza da memória, configurando-a como nan

f_y = np.empty(popsize + n_filhos) #função fitness ou função custo -- população candidata

ff = np.empty(popsize) #função fitness ou função custo -- população filhos
ff.fill(np.nan) #limpeza da memória, configurando-a como nan

f_best = np.empty((genmax, 1)) # Variável para plotagem no gráfico f_best x gen.
f_best.fill(np.nan)

pop_y = np.empty((n_filhos + popsize, nvar)) #população selecionada -- pais
pop_f = np.empty((n_filhos, nvar)) #população criada do cruzamento -- filhos
pop_f.fill(np.nan)

#Avaliação da função objetiva

# Make data.
X = np.arange(0.1, 8, 0.01)
Y = np.arange(-10, -0.1, 0.01)
X, Y = np.meshgrid(X, Y)
Z = Fcusto(X, Y)

#Etapa de Avaliação da População Inicial
for i in range(popsize):
    for j in range(0, nvar):
        pop[i][j] = np.random.uniform(lim_inf[j], lim_sup[j]) #população em número real
    f[i] = Fcusto(pop[i][0], pop[i][1])


#Avaliação da solução ótima (primeira geração)
pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima da primeira geração:')
print('x_best=',pop[pos])
print('f_best',f[pos])

#Etapa de plotagem da população inicial
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_xlim(0.1, 8)
ax.set_ylim(-10, -0.1)
ax.set_zlim(0,10)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

colors = ('k')
c_list = []
for c in colors:
    c_list.extend([c] * 15)

pop_t = pop.transpose()
ax.scatter(pop_t[0], pop_t[1], f, c=c_list)

plt.show()

#---------------------------------------------------------#

""" Início de execução do loop principal do SGA"""

#---------------------------------------------------------#

while (gen<genmax):
    #rotina de seleção dos pais
    for i in range(n_filhos):
        p1 = np.random.randint(0, popsize) # seleciona o pai 1
        p2 = np.random.randint(0, popsize) # seleciona o pai 2

        for j in range(nvar):
            pop_f[i][j] = (pop[p1][j] + pop[p2][j]) / 2 # faz o cruzamento utilizando a média dos pais
            pop_f[i][j] = pop_f[i][j] + sigma * np.random.normal(0, 1) # faz a mutação normal
            if j == 0 and (pop_f[i][j] < 0.1 or pop_f[i][j] > 8):
                pop_f[i] = np.array([4.4914, -1.0857])
            elif j == 1 and (pop_f[i][j] < -10 or pop_f[i][j] > -0.1):
                pop_f[i] = np.array([4.4914, -1.0857])

    pop_y = np.concatenate((pop, pop_f)) # agrupa os pais e filhos em um array
    for j in range(len(pop_y)):
        f_y[j] = Fcusto(pop_y[j][0], pop_y[j][1]) # calcula a função custo

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

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#Etapa de plotagem da população inicial
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_xlim(0.1, 8)
ax.set_ylim(-10, -0.1)
ax.set_zlim(0, 10)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

pop_t = pop.transpose()
ax.scatter(pop_t[0], pop_t[1], f, c=c_list)

plt.show()

# Define as gerações a serem plotadas no gráfico.
x = np.linspace(0, genmax, genmax, endpoint=True)

# Plota o gráfico do melhor valor custo por geração.
plt.figure()
plt.plot(x, f_best, 'r')
plt.title('Melhor valor custo por geração')
plt.ylim((0,10))
plt.xlabel('gen')
plt.ylabel('f_best')
plt.grid()
plt.show()