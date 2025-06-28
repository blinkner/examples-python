# Método de Runge-Kutta de 4ª Ordem
# Para resolução numérica de EDOs
# Escrito por: blinkner 

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

f = lambda x, y: x - y + 2 # EDO
h = 0.1 # Passo
x_i = 0 # Intervalo inicial
x_f = 1 # Invervalo final
n = (int) ((x_f - x_i) / h) # Quantidade de subintervalos

x = np.empty(n + 1)
x.fill(np.nan)
y = np.empty(n + 1)
y.fill(np.nan)

x[0] = 0.0 # Valor inicial de x
y[0] = 2.0 # Valor inicial de y

print(x[0], ',', y[0])

for j in range(n):
    K1 = f(x[j], y[j])
    K2 = f(x[j] + (h/2), y[j] + (h/2) * K1)
    K3 = f(x[j] + (h/2), y[j] + (h/2) * K2)
    K4 = f(x[j] + h, y[j] + h * K3)
    y[j+1] = y[j] + (h/6) * (K1 + 2 * K2 + 2 * K3 + K4)

    x[j+1] = x[j] + h

    print(x[j+1], ',', y[j+1])

n = np.linspace(0, 1, n + 1, endpoint=True)
plt.figure()
plt.plot(n, y, 'r')
plt.grid()
plt.show()