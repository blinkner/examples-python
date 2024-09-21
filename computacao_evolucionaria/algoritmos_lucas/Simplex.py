#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 10:04:03 2024

@author: lqsoliveira
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.close('all')

###############################################################################
#Passo Nº01: Definição dos Vértices do Politopo
v = np.array([[0,0],[1.2,0],[0,0.8]])

###############################################################################
#Passo Nº02: Avaliação da Função Custo para os Vértices

X = np.arange(-10, 10, 0.01) #Definindo o domíno do eixo x
Y = np.arange(-10, 10, 0.01) #Definindo o domíno do eixo y
X, Y = np.meshgrid(X, Y) #Criando a matriz do grid de superfície

Z = X**2-4*X+Y**2-Y-X*Y #Função Custo

# Plot da Superfície da Função Custo
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(X, Y, Z,cmap=cm.coolwarm,linewidth=0, antialiased=False)


fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111,aspect='equal') 
ax.contour(X,Y,Z,levels=60)
ax.set_xlim(-2,5)
ax.set_ylim(-2,5)
plt.show()

n = len(v) #busca o número de vértices do politopo, consequentemente o espaço 
#dimensional do problema, uma vez que o espaço (número de colunas) é n-1.

fc = np.empty(n)
fc.fill(np.nan)

for i in range(n):
    fc[i] = v[i,0]**2-4*v[i,0]+v[i,1]**2-v[i,1]-v[i,0]*v[i,1]

###############################################################################
#Passo Nº03:

foc = np.sort(fc) #Função custo em ordem crescente

voc = np.empty((n,n-1)) #variável para armazenar os vértices em ordem crescente
# B < G < W.
voc.fill(np.nan)

for i in range(n):
    pos = np.argwhere(fc == foc[i]) 
    voc[i,:] = v[pos,:]

ax.plot(voc[0,0],voc[0,1],'*g')
ax.plot(voc[1,0],voc[1,1],'*',color='orange')
ax.plot(voc[2,0],voc[2,1],'*r')

###############################################################################
#Passo Nº04: Construção do politopo. Não é necessária para solução do algoritmo
#trata-se apenas de uma questão visual da evolução do processo.

ax.plot(voc[0:2,0],voc[0:2,1],'-m')
ax.plot(voc[1:,0],voc[1:,1],'-m')
ax.plot([voc[2,0],voc[0,0]],[voc[2,1],voc[0,1]],'-m')

###############################################################################
#Passo Nº05: Cálculo do Centro de Gravidade
aux = 0
lim = 10
fbest = np.empty(lim+1)
fbest.fill(np.nan)
fbest[0] = foc[0]
while aux< lim:
    vm = (voc[0]+voc[1])/2
    fvm = vm[0]**2-4*vm[0]+vm[1]**2-vm[1]-vm[0]*vm[1]
    
    ax.plot(vm[0],vm[1],'*b')
    
    ###############################################################################
    #Passo Nº06: Cálculo do Ponto de Reflexão
    
    vr = vm + (vm-voc[n-1])
    fvr = vr[0]**2-4*vr[0]+vr[1]**2-vr[1]-vr[0]*vr[1]
    ax.plot(vr[0],vr[1],'*c')
    
    ###############################################################################
    #Passo Nº07: Avaliação do Politopo
    
    if fvr<foc[0]:
        #cálculo da extensão
        ve = vm + 2*(vm-voc[n-1])
        fve = ve[0]**2-4*ve[0]+ve[1]**2-ve[1]-ve[0]*ve[1]
        ax.plot(ve[0],ve[1],'*m')
        if fve < fvr: #condição de extensão válida!
            #ordenação das funções custo fB< fG < fW
            foc[1:] = foc[0:n-1]
            foc[0] = fve
            #ordenação do novo vértice vB< vG < vW
            voc[1:,:] = voc[0:n-1,:]
            voc[0] = ve
        else: #condição de extensão não é válida, porém fvr<fvb
            #ordenação das funções custo fB< fG < fW
            foc[1:] = foc[0:n-1]
            foc[0] = fvr
            #ordenação do novo vértice vB< vG < vW
            voc[1:,:] = voc[0:n-1,:]
            voc[0] = vr
            
    elif fvr< foc[1]: #condição válida fvr<fvg
        #ordenação das funções custo fB< fG < fW
        foc[2:] = foc[1:n-1]
        foc[1] = fvr
        
        #ordenação do novo vértice vB< vG < vW
        voc[2:,:] = voc[1:n-1,:]
        voc[1] = vr
    
    else:
        vc = voc[-1] + 0.5*(vm-voc[-1])
        fvc = vc[0]**2-4*vc[0]+vc[1]**2-vc[1]-vc[0]*vc[1]
        ax.plot(vc[0],vc[1],'*g')
        if fvc<foc[-1]:
            if foc[1]< fvc: #condição de contração válida
                voc[-1] = vc
                foc[-1] = fvc
            else:
                if foc[0]< fvc:
                    foc[2:] = foc[1:n-1]
                    foc[1] = fvc
                    
                    voc[2:,:] = voc[1:n-1,:]
                    voc[1] = vc
                else:
                    foc[1:] = foc[0:n-2]
                    foc[0] = fvc
                    
                    voc[1:,:] = voc[0:n-2,:]
                    voc[0] = vc
        else: #condição de shrink válida!
            vs = (voc[0] -voc[-1])/2
            fvs = vs[0]**2-4*vs[0]+vs[1]**2-vs[1]-vs[0]*vs[1]
                
            foc[-1] = fvs
            voc[-1] = vs
                
            #criando variáveis auxiliares
            fc =foc
            v = voc
                
            foc = np.sort(foc) #colocando a função custo em ordem crescente
            for i in range(n): #colocando os vértices em ordem crescente
                pos = np.argwhere(fc == foc[i]) 
                voc[i,:] = v[pos,:]
                
    print('--')
    print(foc[0])
    print(foc[1])
    print(foc[2])
    aux = aux+1
    fbest[aux] = foc[0]
    
plt.figure()
plt.plot(np.arange(lim+1),fbest,'*r')  
plt.grid() 

print('Solução Ótima: f(x,y)',fbest[-1])  
        
                

        