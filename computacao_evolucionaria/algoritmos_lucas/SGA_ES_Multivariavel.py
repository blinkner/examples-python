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
from mpl_toolkits import mplot3d
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

def Busca_pai(p):
    x_rand = np.random.rand() #sorteio de um valor aleatório
    soma = 0 #variável auxiliar, acumulador
    j = 0 #variável auxiliar, contador
    while (soma<x_rand): #loop de implementação do método da roleta
        soma += p[j] #atualização do acumulador
        j+=1 #atualização do contador
    return j-1


Fcusto = lambda X,Y: 0.4/(1+0.02*((X+20)**2 + (Y+20)**2)) + 0.2/(1+0.5*((X+1)**2 + (Y+5)**2)) +0.15/(1+0.03*((X-30)**2 + (Y+30)**2))


#Declaração das variáveis

popsize = 40 #número de indivíduos da população
nbits = 12 #número de bits que define um indivíduo.
gen = 0 #contador do número de gerações
genmax = 150 #número máximo de gerações (repetições do processo de busca SGA)
pc = 0.75 # limiar taxa de cruzamento. Sugestão 0.65 <= pc <=0.8
pm = 0.025 # limiar taxa de mutação. Sugestão: 0.01 <= pm <= 0.05
n = 2 #número de cromossomos
lim_sup = np.array([40,10])
lim_inf = np.array([-40,-40])

#Inicialização da população em binário
pop_2 = np.random.randint(0,2,(popsize,n*nbits))

pop_10 = np.empty((popsize,n)) #população em número real
pop_10.fill(np.nan) #limpeza da memória, configurando-a como nan
f = np.empty(popsize) #função fitness ou função custo -- população candidata
f.fill(np.nan) #limpeza da memória, configurando-a como nan
ff = np.empty(popsize) #função fitness ou função custo -- população filhos
ff.fill(np.nan) #limpeza da memória, configurando-a como nan

f_best = np.empty(genmax) #memória melhor função custo
f_best.fill(np.nan) #limpeza da memória, configurando-a como nan


#pop_y = np.empty((popsize,n*nbits)) #população selecionada -- pais
pop_f = np.empty((popsize,n*nbits)) #população criada do cruzamento -- filhos

#Avaliação da função objetiva
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# Make data.
X = np.arange(-40, 40, 0.01)
Y = np.arange(-40, 10, 0.01)
X, Y = np.meshgrid(X, Y)
Z = Fcusto(X, Y)

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,linewidth=0, antialiased=True)

# Customize the z axis.
ax.set_zlim(0,0.5)
ax.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
ax.zaxis.set_major_formatter('{x:.02f}')

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

#Etapa de Avaliação da População Inicial
for i in range(popsize):
    for j in range(n):
        pop_10[i,j] = b2r(pop_2[i,j*nbits:(j+1)*nbits],lim_inf[j],lim_sup[j]) #conversão binário para real coordenada x
    f[i] = Fcusto(pop_10[i,0],pop_10[i,1]) #Calculando a função custo

#Avaliação da solução ótima (primeira geração)
pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima da primeira geração:')
print('x_best=',pop_10[pos])
print('f_best',f[pos])

X1 = pop_10[:,0].copy()
Y1 = pop_10[:,1].copy()
F1 = f.copy()
#Etapa de plotagem da população inicial
fig2 = plt.figure()
 
# syntax for 3-D projection
ax2 = plt.axes(projection ='3d')
ax2.plot3D(X1,Y1,F1,'*') #plot dos indivíduos da primeira geração

#---------------------------------------------------------#

""" Início de execução do loop principal do SGA"""

#---------------------------------------------------------#

while (gen<genmax):
    p = f/np.sum(f) #cálculo da função custo relativo (normalizado) Eq(9)
    pop_f.fill(np.nan) #limpeza da memória, configurando-a como nan
    
    #rotina de seleção dos pais, método da roleta, cruzamento e mutação
    for i in range(popsize):
        p1 = Busca_pai(p) #seleção do pai via método da roleta
        p2 = Busca_pai(p) #seleção do pai via método da roleta
        if p1==p2: #verifica-se os pais selecionados é o mesmo. Nesse caso busca-se um novo pai, caso a condição seja satisfeita
            while p1==p2:
             p2 = Busca_pai(p)

        if np.random.rand()>= pc: #condição de avaliação do limiar de cruzamento
            l = np.random.randint(0,nbits) #sorteio do índice para troca dos genes
            for j in range(n): #etapa de cruzamento por recombinação.
                pop_f[i,j*nbits:j*nbits+l] = pop_2[p1,j*nbits:j*nbits+l]
                pop_f[i,j*nbits+l:(j+1)*nbits] = pop_2[p2,j*nbits+l:(j+1)*nbits]
        else:
            if p[p1]>p[p2]:
                pop_f[i] = pop_2[p1]
            else:
                pop_f[i] = pop_2[p2]
                
        if np.random.rand() <= pm: #etapa de mutação
            l = np.random.randint(0,nbits)
            for j in range(n):
                pop_f[i,j*nbits+l] = 1- pop_f[i,j*nbits+l]
            
    
    #Etapa de avaliação da função fitness --  População de Filhos
    ff.fill(np.nan) #limpeza da memória, configurando-a como nan
    for i in range(popsize):
        for j in range(n):
            pop_10[i,j] = b2r(pop_f[i,j*nbits:(j+1)*nbits],lim_inf[j],lim_sup[j]) #conversão binário para real coordenada x
        ff[i] = Fcusto(pop_10[i,0],pop_10[i,1]) #Calculando a função custo

    #Etapa de seleção da nova geração
    
    for i in range(popsize):
        if f[i]<ff[i]: #condição para seleção do filho
            pop_2[i] =pop_f[i] #filho, sendo incluído na população candidata
            f[i] =ff[i] #atualização da função custo
        else: 
            pass
    
    #avaliação da solução ótima na geração i
    pos = f.argmax()
    f_best[gen] = f[pos] #salvando a f_best da i-ésima geração
    
    gen+=1 #atualização do contador de gerações   

for i in range(popsize):
    for j in range(n):
        pop_10[i,j] = b2r(pop_f[i,j*nbits:(j+1)*nbits],lim_inf[j],lim_sup[j]) #conversão binário para real coordenada x
    f[i] = Fcusto(pop_10[i,0],pop_10[i,1]) #Calculando a função custo    

pos = f.argmax() #busca da posição no array f, do maior valor de f(x)
print('Solução ótima:')
print('x_best=',pop_10[pos])
print('f_best',f[pos])


fig3 = plt.figure(3)
 
# syntax for 3-D projection
ax3 = plt.axes(projection ='3d')
ax3.plot3D(pop_10[:,0],pop_10[:,1],f,'*') #plot dos indivíduos da primeira geração
plt.show()

plt.figure()
plt.plot(np.arange(0,genmax),f_best,'b')
plt.grid()
plt.ylabel('f(x)')
plt.xlabel('geração')
plt.show()

    