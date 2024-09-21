#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementação do Algoritmo de Evolução Diferencial

@author: Prof. Lucas S. Oliveira
@modificado por: Gabriel Marlon Viana

Data: 11/09/2024

"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import Closed_Loop as cl
plt.close('all')

#######################################################################
#declaração de algumas funções auxiliares internas do algoritmo ED

def Escolha_abc(Np): #A função Escolha_abc retorna três indivíduos diferentes, para realização da operação de mutação. Para tal, basta informar o número de indivíduos da população, Np.
    a = np.random.randint(0,Np)
    b = np.random.randint(0,Np)
    c = np.random.randint(0,Np)
    
    if a==b:
        while (a==b):
            b = np.random.randint(0,Np)
    
    if a==c or b==c:
        while a==c or b==c:
            c = np.random.randint(0,Np)
    return a,b,c
#######################################################################
#Passo 01: Declaração dos Parâmetros do Algoritmo

n = 3 #ordem do problema de otimização.
Np = 22 #número de indivíduos da população.
Cr = 0.65 #limiar de cruzamento.
gen_max = 50 #número máximo de gerações.
g = 0 #contador de geração
Bu = np.array([40, 5, 2]) #vetor com os limite superior da região de busca por parâmetro/característica.
Bl = np.array([0, 0, 0]) #vetor com os limite inferior da região de busca por parâmetro/característica.

P = np.empty((Np,n)) #matriz da população genitora, em que cada linha representa um indivíduo e cada coluna uma característica.
P.fill(np.nan) 

V = np.empty((Np,n)) #matriz da população mutante, em que cada linha representa um indivíduo e cada coluna uma característica.
V.fill(np.nan)

U = np.empty((Np,n)) #matriz da população candidata, em que cada linha representa um indivíduo e cada coluna uma característica.
U.fill(np.nan)

Fp = np.empty(Np)
Fp.fill(np.nan)

Fu = np.empty(Np)
Fu.fill(np.nan)

Fbest = np.empty(gen_max) #Vetor que apresenta a solução ótima por geração
Fbest.fill(np.nan)

#######################################################################
#Passo 02: Inicialização da População Genitora: g=0

for i in range(Np): #loop para execução da eq. (4) do slide 11
    for j in range(n):
        P[i,j] = np.random.uniform(0,1)*(Bu[j]-Bl[j]) + Bl[j]
        
while g<gen_max:       ######################################################################
    #Passo 03: Mutação --- Usando da tabela Slide 13 estratégia 7
    
    for i in range(Np):
        a,b,c = Escolha_abc(Np)
        F = 0.5 + 0.5*np.random.uniform(0,1)
        V[i] = P[a] + F*(P[b]-P[c])
    
######################################################################
    #Passo 04: Cruzamento Binomial
        
    for i in range(Np): #loop para execução da eq. (6) do slide 14 
        k = np.random.randint(0,Np) #escolha aleatória de um indivíduo da população.
        for j in range(n): #teste combinacional -- case da eq. (6)~
            if np.random.uniform(0,1) <= Cr:
                U[i,j] = V[k,j]
            else:
                U[i,j] = P[k,j]
    
######################################################################
    #Passo 05: Seleção via competição individual.
    for i in range(Np):
        Fp[i] = cl.sim(P[i,0], P[i,1], P[i,2])
        Fu[i] = cl.sim(U[i,0], U[i,1], U[i,2])
    
    
    for i in range(Np):
        if Fu[i]<Fp[i]:
            P[i] = U[i]
            Fp[i] = Fu[i]
    
######################################################################
    #Passo 06: Atualização dos critérios de parada.
    pos = Fp.argmin()
    Fbest[g] = Fp[pos]
    g = g + 1
    
######################################################################
#Processamento após conclusão do processo de busca.

print('Solução Ótima')
print('f_best(x,y)=',Fbest[-1])
print('Indivíduo')
print(P[pos])

plt.figure()
plt.plot(Fbest,'b')
plt.grid()
plt.xlabel('Geração')
plt.ylabel('F_best(x,y)')
plt.show()
    

#X = np.arange(-10, 10, 0.01) #Definindo o domíno do eixo x
#Y = np.arange(-5, 5, 0.01) #Definindo o domíno do eixo y
#X, Y = np.meshgrid(X, Y) #Criando a matriz do grid de superfície

#Z = Fcusto(X,Y) #Função Custo

# Plot da Superfície da Função Custo
#fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
#surf = ax.plot_surface(X, Y, Z,cmap=cm.coolwarm,linewidth=0, antialiased=False)


#fig = plt.figure()
#ax = fig.add_subplot(111,aspect='equal') 
#ax.contour(X,Y,Z,levels=60)
#ax.set_xlim(-10,10)
#ax.set_ylim(-5,5)
#plt.show()
    
    