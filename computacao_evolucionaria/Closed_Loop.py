#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data:26/06/2024

@author: Lucas Silva de Oliveira

Esse código simula a dinâmica em malha fechada do conntrole de nível em um tanque com uso de um controlador PID em paralelo.
"""

import numpy as np #Importando a biblioteca numpy - para ambiente matemático com vetores
import matplotlib.pyplot as plt #importando a biblioteca matplotlib - para plotagem
plt.close('all') #fechando todas as janelas com figuras

def sim(Kp,Ki,Kd):
    
    """
    Essa função simula a dinâmica em malha fechada do controle de              nível em um tanque com uso de um controlador PID em paralelo.
    
Parâmetros de entrada:
    ganho proporcional -- Kp, float
    ganho integral -- Ki, float
    ganho derivativo -- Kd, float
Parâmetros de retorno: 
    vetor erro de seguimento de referência.
    vetor com a resposta do sistema
    vetor com o sinal de controle"""
    
    # Definição de algumas constantes do processo.
    T = 1 # (s) período de amostragem
    tf = 6000 # (s) duração do teste
    t = np.arange(0,tf+T,T) #vetor de tempo do experimento
    
    amp = 57 #amplitude do sinal de controle, esse deve ser um valor pertencente ao intervalo 0<= amp <= 100
    u = amp*np.ones(len(t)) #Vetor do sinal de controle
    
    h = np.empty(len(t)) #pre-alocação na memória do estado do sistema - h=altura da coluna de líquido em (cm). Atenção:
    # o tanque possui limitação física, desse modo a altura deve permanecer ao intervalo: 0 <= h <= 70 cm.
    h.fill(np.nan)
    h[0] = 40 #Condição inicial do sistema
    h[1] = 40 #Condição inicial do sistema
    soma = 0
    e = np.empty(len(t))
    e.fill(np.nan)
    e[0] = 0
    r =  np.empty(len(t))
    r.fill(np.nan)
    
    r[0:500]= 40
    r[500:1250] = 45
    r[1250:2000]=37
    r[2000:2750]=41.8878
    r[2750::]= 40 + 5*np.cos(0.005*t[2750::])
    
    for i in range(1,len(t)-1): #simulação do sistema em malha aberta
        e[i] = r[i]-h[i]
        soma +=e[i]
        
        u[i] = 57 + Kp*e[i] + Ki*soma + Kd*(e[i]-e[i-1])
        
        if u[i] > 100: #saturação do sinal de controle
            u[i] = 100
        elif u[i]<0:
            u[i]=0
        else:
            pass
        
        h[i+1] = h[i] + T*(16.998*u[i] + 354.781 - (12.741*h[i]+817.874))/3019
    
    #custo =  np.sum(np.sqrt((e)**2))/(len(e))
    custo = 0
    for i in range(len(e)-1):
        custo += np.sqrt((e[i])**2)
    custo = custo / (len(e)-1)
        
    plt.figure(1)
    plt.subplot(2,1,1) #Plotando a saída do sistema
    plt.plot(t,h,'b')
    plt.plot(t,r,'k--')
    plt.ylabel('h(cm)')
    plt.xlim((0,tf))
    plt.ylim((0,80))
    plt.grid()
    
    plt.subplot(2,1,2) #Plotando o sinal de controle
    plt.plot(t,u,'b')
    plt.xlabel('Times$(s)$')
    plt.ylabel('u(%)')
    plt.xlim((0,tf))
    plt.ylim((0,100))
    plt.grid()
    plt.show()

    #return e,h,u
    return custo