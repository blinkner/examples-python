# Dimensionamento de TBJ
# Desenvolvido por: Gabriel Marlon e Marcelo Alves

import numpy as np

n_pontos = 100
Rb1 = np.zeros(n_pontos)
Rb2 = np.zeros(n_pontos)
Rc = np.zeros(n_pontos)
Re = np.zeros(n_pontos)

R = np.array([1000, 1100, 1200, 1300, 1500, 1600, 1800, 2000, 2200, 2400, 2700, 3000, 3300, 3600, 3900, 4300, 4700, 5100, 10000, 11000, 12000, 13000, 15000, 16000, 18000, 20000, 22000, 24000, 27000, 30000, 33000, 36000, 39000, 43000, 47000, 51000, 100000, 110000, 120000, 130000, 150000, 180000, 200000, 510000], dtype='int64')

j = 0 # Contador de deduções realizáveis
def dimensionamento_tbj(Rf):
    global j
    vi = 10e-3 # Tensão de fonte (pequenos sinais)
    Rbb = 50 # Resistência da fonte (pequenos sinais)
    f = 1e3 # Frequência
    G = -10 # Ganho
    Vt = 25e-3 # Tensão de temperatura
    Vcc = 12 # Tensão da fonte
    Vbe = 0.7 # Queda de tensão entre a base e o emissor

    # Configuráveis de acordo com o gráfico do TBJ
    Ic = 0.45e-3 # Corrente no emissor
    Ib = 1.38e-6 # Corrente na base
    Vce = 9.82 # Tensão entre o coletor e o emissor

    Ie = Ic + Ib
    v0 = vi * G

    # Engenharia reversa
    vbe = (Rf * vi) / (Rf + Rbb)
    # dVc = (2/3) * Vcc
    dVc = (-v0 * Vt) / vbe
    Vc = Vcc - dVc
    Ve = Vc - Vce

    Re = Ve / Ie
    Vb = Ve + Vbe

    rpi = Vt / Ib
    Rth = (Rf * rpi) / (rpi - Rf)
    
    Rc = (Vcc - Vc) / Ic

    Vth = Rth * Ib + Vc - Vce + Vbe

    Rb1 = Rth * Vcc / Vth

    Rb2 = Vth * Rb1 / (Vcc - Vth)

    if (Rb1 < 0 or Rb2 < 0 or Rc < 0 or Re < 0):
        return 0, 0, 0, 0
    else:
        if j == 10:
            return 0, 0, 0, 0
        
        print(f"Rf = {Rf}")
        print(f"vbe = {vbe}")
        print(f"dVc = {dVc}")
        print(f"rpi = {rpi}")
        print(f"Vth = {Vth}")
        print(f"Rth = {Rth}")
        print(f"Vb = {Vb}")
        print(f"Vc = {Vc}")
        print(f"Ve = {Ve}")
        print(f"Ib = {Ib}")
        print(f"Ic = {Ic}")
        print(f"Ie = {Ie}")
        print(f"Rb1 = {Rb1}")
        print(f"Rb2 = {Rb2}")
        print(f"Rc = {Rc}")
        print(f"Re = {Re}")
        print("\n")

        j=j+1
        return Rb1, Rb2, Rc, Re

Rf = np.linspace(6, 100, n_pontos)

for i in range(len(Rf)):
    Rb1[i], Rb2[i], Rc[i], Re[i] = dimensionamento_tbj(Rf[i])
print(f"Contador = {j}")