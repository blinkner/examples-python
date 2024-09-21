#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:03:38 2024

@author: lqsoliveira
"""
import numpy as np
import matplotlib.pyplot as plt
import costFunction as cf
plt.close('all')

#Declaração das variáveis

popsize = 70 #número de indivíduos da população
n = 3
genmax = 10000 #número máximo de gerações (repetições do processo de busca SGA)
n_filhos = 140 #número de filhos
limite = 1e-05 # limite
nlimite = 200 # número de repetições do limite
execucao = 1 # contador de execuções
max_execucao = 33 # número máximo de execuções
sigma = 0.125 # desvio padrão
lim_sup = np.array([15, 15, 15]) # limite superior
lim_inf = np.array([0, 0, 0]) # limite inferior


while execucao <= max_execucao:
    gen = 0 #contador do número de gerações
    cont_limite = 0 # contador da quantidade de vezes que o limite foi satisfeito

    pop = np.empty((popsize, n)) #população em número real
    pop.fill(np.nan) #limpeza da memória, configurando-a como nan

    pop_t = np.empty((n, popsize))
    pop_t.fill(np.nan)

    f = np.empty(popsize) #função fitness ou função custo -- população candidata
    f.fill(np.nan) #limpeza da memória, configurando-a como nan

    f_y = np.empty(popsize + n_filhos) #função fitness ou função custo -- população candidata

    ff = np.empty(popsize) #função fitness ou função custo -- população filhos
    ff.fill(np.nan) #limpeza da memória, configurando-a como nan

    f_best = np.empty((genmax, 1)) # Variável para plotagem no gráfico f_best x gen.
    f_best.fill(np.nan)

    pop_y = np.empty((n_filhos + popsize, n)) #população selecionada -- pais
    pop_y.fill(np.nan)

    pop_f = np.empty((n_filhos, n)) #população criada do cruzamento -- filhos
    pop_f.fill(np.nan)

    #Etapa de Avaliação da População Inicial
    for i in range(popsize):
        for j in range(0, n):
            pop[i][j] = np.random.uniform(lim_inf[j], lim_sup[j]) #população em número real
        f[i] = cf.simulacao_malha(pop[i][0], pop[i][1], pop[i][2])

    #Avaliação da solução ótima (primeira geração)
    pos = f.argmin() #busca da posição no array f, do maior valor de f(x)
    print('Solução ótima da primeira geração:')
    print('x_best=',pop[pos])
    print('f_best',f[pos])

    #---------------------------------------------------------#

    """ Início de execução do loop principal do SGA"""

    #---------------------------------------------------------#

    while (gen<genmax and cont_limite<nlimite):
        print('Geração:', gen, sep=' ')
        #rotina de seleção dos pais
        for i in range(n_filhos):
            p1 = np.random.randint(0, popsize) # seleciona o pai

            for j in range(n):
                pop_f[i][j] = pop[p1][j] + sigma * np.random.normal(0, 1) # faz a mutação normal
                if pop_f[i][j] < 0 or pop_f[i][j] > 15:
                    pop_f[i] = np.array([0.1, 0.1, 0.1])

        pop_y = np.concatenate((pop, pop_f)) # agrupa os pais e filhos em um array
        for j in range(len(pop_y)):
            f_y[j] = cf.simulacao_malha(pop_y[j][0], pop_y[j][1], pop_y[j][2]) # calcula a função custo

        for i in range(popsize): # busca os melhores indivíduos para manter na população
            pos= f_y.argmin()
            pop[i] = pop_y[pos]
            f[i] = f_y[pos]
            f_y[pos] = 1000

        pos = f.argmin()
        f_best[gen] = f[pos]

        if abs(f_best[gen] - f_best[gen-1]) < limite:
            cont_limite += 1
        else:
            cont_limite = 0

        gen+=1 #atualização do contador de gerações
        
    #Avaliação da solução ótima
    pos = f.argmin() #busca da posição no array f, do maior valor de f(x)
    print('Solução ótima:')
    print('x_best=',pop[pos])
    print('f_best',f[pos])

    #best = cf.simulacao_malha(pop[pos][0], pop[pos][1], pop[pos][2], showFigure=True)

    # Dados para serem exportados para o arquivo
    dados = list()
    dados.append(str(execucao)) # Execução
    dados.append(str(pop[pos][0])) # Kp
    dados.append(str(pop[pos][1])) # Ti
    dados.append(str(pop[pos][2])) # Td
    dados.append(str(f[pos])) # RMSE

    if gen == genmax:
        dados.append('geração') # Critério
    else:
        dados.append('limite') # Critério

    arquivo = open('ep_dados.txt', 'a')

    for i in range(len(dados)):
        arquivo.writelines(dados[i])
        if i < len(dados)-1:
            arquivo.write('\t')

    arquivo.write('\n')
    arquivo.close()

    # Plota o gráfico do melhor valor custo por geração.
    #plt.figure()
    #plt.plot(np.arange(0, genmax), f_best, 'r')
    #plt.title('Melhor valor custo por geração')
    #plt.xlabel('gen')
    #plt.ylabel('f_best')
    #plt.grid()
    #plt.show()

    execucao += 1