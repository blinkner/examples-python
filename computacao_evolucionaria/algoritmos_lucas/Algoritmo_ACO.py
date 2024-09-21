#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 20:11:15 2024
@author: lqsoliveira

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

num_cidades = 5 #ordem do problema de otimização (número de cidades a serem visitadas).
num_formigas = 5 #número de formigas que atuarão no processo de busca

alfa = 0.1 # Fator de importância da trilha de feromônios
beta = 4 # Fator de importância da visibilidade (distância)
rho = 0.05  # Taxa de evaporação de feromônio
Q = 1 #volume de feromônio desprendido ao longo da rota

gen_max = 200 #Critério de parada: número máximo de gerações.
g = 0 #Variável auxiliar para contagem de gerações.

best_rota = None
best_distancia = float('inf')

#matriz de custo -- distância entre as cidades.
D = np.array([
    [0, 1, 2.2, 2, 4.1],
    [1,0,1.4,2.2,4],
    [2.2,1.4,0,2.2,3.2],
    [2,2.2,2.2,0,2.2],
    [4.1,4,3.2,2.2,0]
    ])

#matriz inicial de feromônios
Conc_Inicial_feromonio = 0.1111
tau = np.ones((num_cidades, num_cidades)) * Conc_Inicial_feromonio

#######################################################################
#Passo 02: loop principal

while g<gen_max:
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
    g +=1

print("Melhor caminho encontrado:", best_rota)
print("Menor distância a ser percorrida:", best_distancia)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    