# Dimensionamento de Engrenagens: Módulo de Resistência e Desgaste
# Desenvolvido por: Gabriel Marlon

import numpy as np

# Funções
MR = lambda MT, KT, K1, z, K, Y, sigma, cv, K2: ((2 * MT * KT * K1)/(z * K * np.pi * Y * sigma * cv * K2))**(1/3)
CV = lambda v: 3/(3+v)
D = lambda z, m: z * m
V = lambda d, n: (np.pi * d * n)/60000
MD = lambda MT, K, z, cv, c: ((2 * MT)/(K* np.pi * z * cv * c))**(1/3)
C = lambda b, z1, z2, E1, E2, sigma_c: (np.sin(2 * b * np.pi / 180)/4.4) * ((z1 * z2)/(z1 + z2)) * ((E1 + E2)/(E1 * E2)) * sigma_c**2
SIGMA_C = lambda HB, n, h, t: (0.5 * HB)/(60 * n * h / (10**6))**t

mr = np.zeros(10)
d = np.zeros(10)
v = np.zeros(10)
cv = np.zeros(10)

# Variáveis
K1 = 1.25 # Fator de serviço
K2 = 1.6 # Fator de correção do fator de forma Y
KT = 1.43 # Fator de concentração de tensões
Ks = 3.5 # Coeficiente de segurança
K = 8
Y = 0.295 # Fator de forma
sigma_lr = 60 # Tensão limite de resistência
HB = 200 # Dureza Brinell
h = 20000 # Vida útil (em horas)
t = 1/6
E1 = E2 = 200000 # Módulo de elasticidade (em Mpa)
b = 20 # Ângulo
z = z1 = 16 # Número de dentes do pinhão
z2 = 128 # Número de dentes da coroa
MT = 35093.38 # Momento Torçor
n = 240 # Rotação

sigma_adm = sigma_lr / Ks # Tensão admissível
E1 = E2 = E1/9.807 # Módulo de elasticidade (em kgf/mm2)

tol = 0.001 # Tolerância

print("Cálculo do Módulo de Resistência")
print("cv \t\t\t m \t\t\t d \t\t\t v \t\t\t cv")

cv[0] = 0.5 # Chute inicial de cv

i = 0
while (1):
    mr[i] = MR(MT, KT, K1, z, K, Y, sigma_adm, cv[i], K2)

    d[i] = D(z, mr[i])
    v[i] = V(d[i], n)
    cv[i+1] = CV(v[i])

    print(cv[i], "\t", mr[i], "\t", d[i], "\t", v[i], "\t", cv[i+1])

    if (abs(mr[i] - mr[i-1]) < tol):
        break
    i += 1

print("mr =", mr[i])
print("\n")

sigma_c = SIGMA_C(HB, n, h, t)
c = C(b, z1, z2, E1, E2, sigma_c)
md = MD(MT, K, z, cv[i], c)

print("Cálculo do Módulo de Desgaste")
print("sigma_c =", sigma_c)
print("c =", c)
print("md =", md)

if (md > mr[i]):
    HB = (HB**(-2/3) * mr[i] / md) ** (-3/2)
    print("Novo HB =", HB)
