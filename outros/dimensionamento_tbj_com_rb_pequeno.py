# Dimensionamento de um TBJ (RB não pode ser desconsiderado)
# Desenvolvido por: Gabriel Marlon e Marcelo Alves

import numpy as np

vi = 25e-3 # Tensão de fonte (pequenos sinais)
Rsig = 50 # Resistência da fonte (pequenos sinais)
f = 1e3 # Frequência
G = -290 # Ganho (235)
Vt = 25e-3 # Tensão de temperatura
VCC = 15 # Tensão da fonte (12)
Vbe = 0.7 # Queda de tensão entre a base e o emissor

# Configuráveis de acordo com o gráfico do TBJ BC547B
IC = 12.5e-3 # Corrente no emissor (12.5e-3)
IB = 50e-6 # Corrente na base (50e-6)
IE = IC + IB
b = IC / IB
Vce = 3 # Tensão entre o coletor e o emissor (5)
RB = (Vce - Vbe) / IB

rpi = Vt/IB
gm = IC/ Vt

RC = (-G * (Rsig * RB + Rsig * rpi + RB * rpi)) / (G * (Rsig + Rsig * rpi * gm + rpi) - rpi * (1 - RB * gm))
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
print(f"RB = {RB}")
print(f"RC = {RC}")
print(f"RE = {RE}")
print(f"PC = {PC}")
print(f"PE = {PE}")