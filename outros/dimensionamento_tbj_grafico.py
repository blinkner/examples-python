# Dimensionamento de TBJ pelo gráfico
# Desenvolvido por: Gabriel Marlon e Marcelo Alves

import numpy as np

vi = 10e-3 # Tensão de fonte (pequenos sinais)
Rsig = 50 # Resistência da fonte (pequenos sinais)
f = 1e3 # Frequência
G = -250 # Ganho
Vt = 25e-3 # Tensão de temperatura
VCC = 12 # Tensão da fonte
Vbe = 0.7 # Queda de tensão entre a base e o emissor

# Configuráveis de acordo com o gráfico do TBJ
IC = 12.5e-3 # Corrente no emissor
IB = 50e-6 # Corrente na base
IE = IC + IB
b = IC / IB
Vce = 5 # Tensão entre o coletor e o emissor
RB = 86e3

RC = - G * (Rsig + Vt / IB) / b
VC = VCC - RC * IE
# VE = VC - Vce
# RE = VE / IE
# VB = VE + Vbe
VB = VC - RB * IB
VE = VB - Vbe
RE = VE / IE

PC = RC * IE**2
PE = RE * IE**2

print(f"IC = {IC}")
print(f"IB = {IB}")
print(f"IE = {IE}")
print(f"b = {b}")
print(f"VC = {VC}")
print(f"VB = {VB}")
print(f"VE = {VE}")
print(f"RC = {RC}")
print(f"RE = {RE}")
print(f"PC = {PC}")
print(f"PE = {PE}")