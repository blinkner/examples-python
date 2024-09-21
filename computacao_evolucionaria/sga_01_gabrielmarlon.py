# Desenvolvido por: Gabriel Marlon Viana
# Matrícula: 20243002252

import funcoes_01_gabrielmarlon as funcoes
import numpy as np
import matplotlib.pyplot as plt

# Define a população inicial pela função pop2 (random.uniform) entre o intervalo de -1 e 2.
popsize = 15
pop = funcoes.pop2(-1, 2, popsize)

# Avalia cada indivíduo pela função objetivo.
f = []
for x in pop:
    f.append(x * np.sin(10 * np.pi * x) + 2)

# Define a curva a ser plotada no gráfico.
x = np.linspace(-1, 2, 256, endpoint=True)
y = x * np.sin(10 * np.pi * x) + 2

# Plota o gráfico da primeira geração da população.
plt.figure(figsize=(8,5), dpi=(120))
plt.plot(x, y, color='blue', linewidth=2.5, linestyle='-', label="função objetiva")
plt.plot(pop, f, color='red', marker='o', linewidth=0, label="indivíduo da população")
plt.title('Primeira geração da população')
plt.legend()
plt.xlabel('x')
plt.ylabel('f (x)')
plt.show()