# Método de Euler
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

x[0] = 0.0
y[0] = 2.0

print(x[0], ',', y[0])

for j in range(n):
    y[j+1] = y[j] + h * f(x[j], y[j])
    
    x[j+1] = x[j] + h

    print(x[j+1], ',', y[j+1])


n = np.linspace(0, 1, n + 1, endpoint=True)
plt.figure()
plt.plot(n, y, 'r')
plt.grid()
plt.show()