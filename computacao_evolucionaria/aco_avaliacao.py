#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: lqsoliveira
@modificado por: Gabriel Marlon Viana

Implementação do algoritmo baseado em colônia de formigas.
"""

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#######################################################################
#Funções auxiliares
def seleciona_proxima_cidade(Cidade_atual, Cidades_Visitada):
    P = calculo_probabilidade(Cidade_atual, Cidades_Visitada)
    Cidades_disponiveis = np.arange(num_cidades)
    Proxima_visita = np.random.choice(Cidades_disponiveis, p=P)
    #Proxima_visita = P.argmax() 
    return Proxima_visita

def calculo_probabilidade(Cidade_atual, Cidades_Visitada):
    Cidades_nao_visitadas = np.delete(np.arange(num_cidades), Cidades_Visitada)
    probabilidade = np.zeros(num_cidades)
    total = 0.0
    for cidade in Cidades_nao_visitadas:
        total += (tau[Cidade_atual][cidade] ** alfa) * ((1.0 / D[Cidade_atual][cidade]) ** beta)
    for cidade in Cidades_nao_visitadas:
        probabilidade[cidade] = (tau[Cidade_atual][cidade] ** alfa) * ((1.0 / D[Cidade_atual][cidade]) ** beta) / total
    return probabilidade

def Calculo_distancia(rota):
    total_distance = 0
    for i in range(num_cidades - 1):
        total_distance += D[rota[i]][rota[i + 1]]
    total_distance += D[rota[-1]][rota[0]]  # Volta para a cidade inicial
    return total_distance


#######################################################################
#Passo 01: Declaração dos Parâmetros do Algoritmo

num_cidades = 42 #ordem do problema de otimização (número de cidades a serem visitadas).
num_formigas = 1000 #número de formigas que atuarão no processo de busca

alfa = 1 # Fator de importância da trilha de feromônios
beta = 4 # Fator de importância da visibilidade (distância)
rho = 0.5  # Taxa de evaporação de feromônio
Q = 1 #volume de feromônio desprendido ao longo da rota

gen_max = 200 #Critério de parada: número máximo de gerações.
g = 0 #Variável auxiliar para contagem de gerações.

D = np.empty((num_cidades, num_cidades))
D.fill(np.nan)

f_best = np.empty(gen_max)
f_best.fill(np.nan)

best_rota = None
best_distancia = float('inf')

cidades = np.array([
    [170, 85],
    [166, 88],
    [133, 73],
    [140, 70],
    [142, 55],
    [126, 53],
    [125, 60],
    [119, 68],
    [117, 74],
    [99, 83],
    [73, 79],
    [72, 91],
    [37, 94],
    [6, 106],
    [3, 97],
    [21, 82],
    [33, 67],
    [4, 66],
    [3, 42],
    [27, 33],
    [52, 41],
    [57, 59],
    [58, 66],
    [88, 65],
    [99, 67],
    [95, 55],
    [89, 55],
    [83, 38],
    [85, 25],
    [104, 35],
    [112, 37],
    [112, 24],
    [113, 13],
    [125, 30],
    [135, 32],
    [147, 18],
    [147.5, 36],
    [154.5, 45],
    [157, 54],
    [158, 61],
    [172, 82],
    [174, 87]
    ])

#matriz de custo -- distância entre as cidades.
for i in range(num_cidades):
    for j in range(num_cidades):
        D[i][j] = np.sqrt((cidades[i][0] - cidades[j][0])**2 + (cidades[i][1] - cidades[j][1])**2)

#matriz inicial de feromônios
Conc_Inicial_feromonio = 0.1111
tau = np.ones((num_cidades, num_cidades)) * Conc_Inicial_feromonio

#######################################################################
#Passo 02: loop principal

while g<gen_max:
    print("Geração: ", g, sep=' ')

    for ant in range(num_formigas):
        Cidade_atual = np.random.randint(num_cidades) #busca randômica da cidade.
        Cidades_Visitada = [Cidade_atual] #histórico das cidades visitadas.
        
        #Loop para criação da trilha que a formiga irá percorrer
        while len(Cidades_Visitada) < num_cidades:
            Proxima_visita = seleciona_proxima_cidade(Cidade_atual, Cidades_Visitada)
            Cidades_Visitada.append(Proxima_visita)
            Cidade_atual = Proxima_visita
        Distancia_Percorrida = Calculo_distancia(Cidades_Visitada)
        
        # Atualização da melhor solução (melhor rota e menor distância percorrida)
        if Distancia_Percorrida < best_distancia:
            best_distancia = Distancia_Percorrida
            best_rota = Cidades_Visitada
        
        # Atualização da matriz de feromônios na trilha
        for i in range(num_cidades - 1):
            if i ==0:
                tau[Cidades_Visitada[-1]][Cidades_Visitada[0]] += Q / Distancia_Percorrida #somando a contribuição do último segmento de aresta
            tau[Cidades_Visitada[i]][Cidades_Visitada[i + 1]] += Q / Distancia_Percorrida
        tau *= (1.0 - rho) #aplicando a taxa de evaporação

    f_best[g] = best_distancia
    g +=1

print("Melhor caminho encontrado:", best_rota)
print("Menor distância a ser percorrida:", best_distancia)
    
plt.figure()
plt.plot(np.arange(0,gen_max),f_best,'b')
plt.grid()
plt.ylabel('f_best')
plt.xlabel('geração')
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    