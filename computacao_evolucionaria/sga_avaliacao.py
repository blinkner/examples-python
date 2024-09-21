#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:03:38 2024

@author: lqsoliveira
"""
import numpy as np
import matplotlib.pyplot as plt
import Closed_Loop as cl
plt.close('all')

#Funções
def b2r(x,a,b):
    """A função b2r converte um número binário em número real. Em que:
    x é um array contendo o número binário (indivíduo)
    a é o limite inferior do domínio real
    b é o limite superior do domínio real"""
    d = 0 # variável auxiliar, somador.
    nbits = len(x) # busca pelo tamanho do array de bits
    for i in range((nbits-1), -1,-1): 
        d = d + x[i]*2**(nbits-1 -i) # implementação do somatório da Eq(8)
    return d/(2**nbits)*(b-a)+a # implementação da Eq(8)
def Busca_pai(p):
    x_rand = np.random.rand() # sorteio de um valor aleatório
    soma = 0 # variável auxiliar, acumulador
    j = 0 # variável auxiliar, contador
    while (soma<x_rand): # loop de implementação do método da roleta
        soma += p[j] # atualização do acumulador
        j+=1 # atualização do contador
    return j-1

# Declaração das variáveis
popsize = 22 # número de indivíduos da população
nbits = 16 # número de bits que define um indivíduo.
genmax = 50 # número máximo de gerações (repetições do processo de busca SGA)
execucao = 1 # contador de execuções
max_execucao = 15 # número máximo de execuções
pc = 0.82 # limiar taxa de cruzamento. Sugestão 0.65 <= pc <=0.8
pm = 0.04 # limiar taxa de mutação. Sugestão: 0.01 <= pm <= 0.05
n = 3 # número de cromossomos
lim_sup = np.array([10, 5, 7]) # limites superiores
lim_inf = np.array([0, 0, 0]) # limites inferiores

while execucao <= max_execucao:
    gen = 0 # contador do número de gerações

    pop_10 = np.empty((popsize,n)) # população em número real
    pop_10.fill(np.nan) # limpeza da memória, configurando-a como nan

    f = np.empty(popsize) # função fitness ou função custo -- população candidata
    f.fill(np.nan) # limpeza da memória, configurando-a como nan

    ff = np.empty(popsize) # função fitness ou função custo -- população filhos
    ff.fill(np.nan) # limpeza da memória, configurando-a como nan

    f_best = np.empty(genmax) # memória melhor função custo
    f_best.fill(np.nan) # limpeza da memória, configurando-a como nan

    pop_f = np.empty((popsize,n*nbits)) # população criada do cruzamento -- filhos

    # Inicialização da população em binário
    pop_2 = np.random.randint(0,2,(popsize,n*nbits))

    # Etapa de Avaliação da População Inicial
    for i in range(popsize):
        for j in range(n):
            pop_10[i,j] = b2r(pop_2[i,j*nbits:(j+1)*nbits],lim_inf[j],lim_sup[j]) #conversão binário para real coordenada x
        f[i] = cl.sim(pop_10[i][0], pop_10[i][1], pop_10[i][2]) #Calculando a função custo

    # Avaliação da solução ótima (primeira geração)
    pos = f.argmin() #busca da posição no array f, do menor valor de f(x)
    print('Solução ótima da primeira geração:')
    print('x_best=',pop_10[pos])
    print('f_best',f[pos])

    #---------------------------------------------------------#

    """ Início de execução do loop principal do SGA"""

    #---------------------------------------------------------#
    while (gen<genmax):
        print('Geracao:', gen, sep=' ')

        p = f/np.sum(f) # cálculo da função custo relativo (normalizado) Eq(9)
        p = (1 - p) / (popsize - 1)

        pop_f.fill(np.nan) # limpeza da memória, configurando-a como nan
        
        # Rotina de seleção dos pais, método da roleta, cruzamento e mutação
        for i in range(popsize):
            p1 = Busca_pai(p) # seleção do pai via método da roleta
            p2 = Busca_pai(p) # seleção do pai via método da roleta
            if p1==p2: # verifica-se os pais selecionados é o mesmo. Nesse caso busca-se um novo pai, caso a condição seja satisfeita
                while p1==p2:
                    p2 = Busca_pai(p)

            if np.random.rand()>= pc: # condição de avaliação do limiar de cruzamento
                l = np.random.randint(0,nbits) # sorteio do índice para troca dos genes
                for j in range(n): # etapa de cruzamento por recombinação.
                    pop_f[i,j*nbits:j*nbits+l] = pop_2[p1,j*nbits:j*nbits+l]
                    pop_f[i,j*nbits+l:(j+1)*nbits] = pop_2[p2,j*nbits+l:(j+1)*nbits]
            else:
                if p[p1]>p[p2]:
                    pop_f[i] = pop_2[p1]
                else:
                    pop_f[i] = pop_2[p2]
                    
            if np.random.rand() <= pm: # etapa de mutação
                l = np.random.randint(0,nbits)
                for j in range(n):
                    pop_f[i,j*nbits+l] = 1 - pop_f[i,j*nbits+l]
                
        # Etapa de avaliação da função fitness --  População de Filhos
        ff.fill(np.nan) # limpeza da memória, configurando-a como nan
        for i in range(popsize):
            for j in range(n):
                pop_10[i,j] = b2r(pop_f[i,j*nbits:(j+1)*nbits],lim_inf[j],lim_sup[j]) # conversão binário para real coordenada x
            ff[i] = cl.sim(pop_10[i][0], pop_10[i][1], pop_10[i][2]) # calculando a função custo

        pop_2 = pop_f.copy()
        f = ff.copy()
        
        # Avaliação da solução ótima na geração i
        pos = f.argmin()
        f_best[gen] = f[pos] # salvando a f_best da i-ésima geração

        gen+=1 # atualização do contador de gerações   

    for i in range(popsize):
        for j in range(n):
            pop_10[i,j] = b2r(pop_2[i,j*nbits:(j+1)*nbits],lim_inf[j],lim_sup[j]) # conversão binário para real coordenada x 

    pos = f.argmin() # busca da posição no array f, do maior valor de f(x)
    print('Solução ótima:')
    print('x_best=',pop_10[pos])
    print('f_best',f[pos])

    #best = cf.simulacao_malha(pop_10[pos][0], pop_10[pos][1], pop_10[pos][2], showFigure=True)

    # Dados para serem exportados para o arquivo
    dados = list()
    dados.append(str(execucao)) # Execução
    dados.append(str(pop_10[pos][0])) # Kp
    dados.append(str(pop_10[pos][1])) # Ki
    dados.append(str(pop_10[pos][2])) # Kd
    dados.append(str(f[pos])) # RMSE

    arquivo = open('algoritmos/avaliacao/sga_dados.txt', 'a')

    for i in range(len(dados)):
        arquivo.writelines(dados[i])
        if i < len(dados)-1:
            arquivo.write('\t')

    arquivo.write('\n')
    arquivo.close()

    #plt.figure()
    #plt.plot(np.arange(0,genmax),f_best,'b')
    #plt.grid()
    #plt.ylabel('f_best')
    #plt.xlabel('geração')
    #plt.show()

    execucao += 1