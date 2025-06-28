# Algoritmo de Evolução Diferencial - ED
# Desenvolvido por: blinkner

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

Fcusto = lambda x,y: x**2 - 4*x + y**2 - y - x*y

n = 2
gen = 0
genmax = 50
Cr = 0.65
Np = 7*n
cruzamento = 'exp' # 'exp' para exponencial e 'bin' para binomial
mutacao = 'best' # 'best' ou 'rand'
lim_sup = np.array([10, 5])
lim_inf = np.array([-10, -5])

v = np.empty((Np, n))
v.fill(np.nan)

u = np.empty((Np, n))
u.fill(np.nan)

fx = np.empty(Np)
fx.fill(np.nan)

fu = np.empty(Np)
fu.fill(np.nan)

f_best = np.empty(genmax)
f_best.fill(np.nan)

x = np.random.rand(Np, n) * (lim_sup - lim_inf) + lim_inf
for i in range(Np):
    fx[i] = Fcusto(x[i][0], x[i][1])

while gen < genmax:
    # Mutação
    for i in range(Np):
        if mutacao == 'best':
            a = fx.argmin()
        elif mutacao == 'rand':
            a = np.random.randint(0, Np)

        b = np.random.randint(0, Np)
        c = np.random.randint(0, Np)

        while b == a or b == c:
            b = np.random.randint(0, Np)
        while c == a or c == b:
            c = np.random.randint(0, Np)

        F = 0.5 + 0.5 * np.random.rand()
        v[i] = x[a] + F * (x[b] - x[c])

    # Cruzamento
    if cruzamento == 'bin':
        for i in range(Np):
            for j in range(n):
                if np.random.rand() <= Cr:
                    u[i][j] = v[i][j]
                else:
                    u[i][j] = x[i][j]
    elif cruzamento == 'exp':
        u = x.copy()
        for i in range(Np):
            p1 = np.random.randint(0, n)
            p2 = np.random.randint(0, n)
            aux = 0

            j = 0
            while aux < p2:
                if j >= p1:
                    u[i][j] = v[i][j]
                    aux += 1
                j += 1

                if j == (Np):
                    p1 = 0
                    j = 0

    # Competição
    for i in range(Np):
        fu[i] = Fcusto(u[i][0], u[i][1])

    for i in range(Np):
        if fu[i] <= fx[i]:
            x[i] = u[i]
            fx[i] = fu[i]

    pos = fx.argmin()
    f_best[gen] = fx[pos]

    gen += 1

print('Solução ótima:')
print(f_best[gen - 1])

# Plota o gráfico do melhor valor custo por geração.
plt.figure()
plt.plot(np.arange(0, genmax), f_best, 'r')
plt.title('Melhor valor custo por geração')
plt.xlabel('gen')
plt.ylabel('f_best')
plt.grid()
plt.show()