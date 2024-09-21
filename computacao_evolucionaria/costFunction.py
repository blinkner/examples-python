#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import control as ctl
import matplotlib.pyplot as plt
import numpy as np

# Sinal de referência
t = np.arange(0, 100, 0.1)
ref = np.zeros_like(t)

def simulacao_malha(Kp, Ti, Td, showFigure = False, legend = False):

    # Função de transferência do sistema
    # Sistema: G(s) = 1/s*(s+1)*(s+5) = 1/(s**3 + 6*s**2 + 5*s)
    numerador_sistema = [1]
    denominador_sistema = [1, 6, 5, 0]
    sistema = ctl.TransferFunction(numerador_sistema, denominador_sistema)

    # Criar a função de transferência do controlador PID
    numerador_pid = [Kp * Td, Kp, Kp / Ti]
    denominador_pid = [1, 0]
    controlador = ctl.TransferFunction(numerador_pid, denominador_pid)

    # Malha fechada
    sistema_malha_fechada = ctl.feedback(controlador * sistema)

    for i in range(len(t)):
        if t[i] < 20: ref[i] = 0
        elif 20 <= t[i] < 40: ref[i] = 1
        elif 40 <= t[i] < 60: ref[i] = 0.5
        elif 60 <= t[i] < 80: ref[i] = 1.5
        elif t[i] >= 80: ref[i] = 1

    # Simulação da malha fecha para a referência dada
    _, resposta = ctl.forced_response(sistema_malha_fechada, t, ref)

    # Calculo do erro 
    custo =  np.sum(np.sqrt((resposta - ref)**2))/(len(ref))

    if showFigure:
        if(legend=='Sintonia DE'): plt.plot(t, ref, 'k--', label='Referência')
        plt.plot(t, resposta, label=legend)
        plt.plot(t, ref, 'k--')
        plt.grid()
        plt.show()
    return custo
