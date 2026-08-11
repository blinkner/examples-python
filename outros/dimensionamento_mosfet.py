# Dimensionamento MOSFET NMOS
# Modelo: Fonte comum
# Desenvolvido por: Gabriel Marlon

import numpy as np

# Características de projeto: MOSFET 2N7000
VGS = 3
VDS = 6
Vt = 1 # Tensão de limiar
ID = 0.002 # Corrente do dreno (em A)
Gv = -10
VDD = 15
Rsig = 50
vi = 10e-3 # Tensão da fonte para pequenos sinais

RS = 1500 # Resistência do Source (Chute)
RL = 1e6 # Resistência de Carga (Chute)

R = np.array([1000, 1100, 1200, 1300, 1500, 1600, 1800, 2000, 2200, 2400, 2700, 3000, 3300, 3600, 3900, 4300, 4700, 5100, 10000, 11000, 12000, 13000, 15000, 16000, 18000, 20000, 22000, 24000, 27000, 30000, 33000, 36000, 39000, 43000, 47000, 51000, 100000, 110000, 120000, 130000, 150000, 180000, 200000, 510000], dtype='int64')

R_temp = R - RS
RS = R[np.argmin(abs(R_temp))]

if (VGS > Vt):
    print("Canal Induzido!")

    if (VDS > (VGS - Vt)):
        print("O MOSFET está atuando como amplificador.")

        gm = (2 * ID) / (VGS - Vt)
        VS = RS * ID
        VG = VGS + VS
        VD = VDS + VS

        RD = (VDD - VD) / ID

        R_temp = R - RD
        RD = R[np.argmin(abs(R_temp))]

        print(f"RS = {RS} Ohms")
        print(f"RD = {RD} Ohms")

        for RG2 in R:
            # RL = - (RD * gm * (VDD * (Rsig + RG2) - RG2 * VG)) / (VDD * (RG2 * RD + gm * Rsig + RG2 * gm) - RG2 * VG * (RD + gm))
            # RG2 = - (VDD * Rsig * Gv * (RD + RL)) / (gm * RD * RL * (VDD - VG) + VDD * Gv * (RD + RL) + VG * (RL - RD))
            RG2 = (Rsig * VDD * Gv) / (-VDD * (gm * RD + Gv) + VG * (gm * RD + Gv)) 
            RG1 = RG2 * (VDD / VG - 1)
            # RF = (RG1 * RG2) / (RG1 + RG2)
            # G = -gm * RF * RD / (Rsig + RF)

            # if RL > 0:
            print(f"RG1 = {RG1} Ohms")
            print(f"RG2 = {RG2} Ohms")
            # print(f"G = {Gv} V/V")
            print("\n")

    else:
        print("O MOSFET está atuando como chave.")
else:
    print("Falha! Não há canal induzido.")
