# Simplex Search Algorithm - SSA Multivariável
# Desenvolvido por Gabriel Marlon

import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

Fcusto = lambda x,y: x**2 - 4*x + y**2 - y - x*y

n = 3 # número de vértices
iteracao = 0 # contador de iterações
max_iteracoes = 10 # número de iterações
v = np.empty((n, 2)) # inicialização do array de vértices
v.fill(np.nan) # limpeza do array de vértices
v[0] = np.array([0.0, 0.0])
v[1] = np.array([1.2, 0.0])
v[2] = np.array([0.0, 0.8])

f = np.empty(n) # inicialização do array da função custo
f.fill(np.nan) # limpeza do array da função custo

for i in range(n):
    f[i] = Fcusto(v[i][0], v[i][1]) # cálculo da função custo

w = f.argmax()
b = f.argmin()

fa = f.copy() # array auxiliar
fa[b] = 1000
g = fa.argmin()

while iteracao < max_iteracoes:
    m = (v[b] + v[g]) / 2

    vr = m + (m - v[w])
    fr = Fcusto(vr[0], vr[1])

    if fr < f[b]:
        ve = m + 2*(m - v[w])
        fe = Fcusto(ve[0], ve[1])

        if fe < fr:
            v[w] = v[g]
            f[w] = f[g]

            v[g] = v[b]
            f[g] = f[b]

            v[b] = ve
            f[b] = fe
        else:
            v[w] = v[g]
            f[w] = f[g]

            v[g] = v[b]
            f[g] = f[b]

            v[b] = vr
            f[b] = fr
    elif fr < f[g]:
        v[w] = v[g]
        f[w] = f[g]

        v[g] = vr
        f[g] = fr
    else:
        vc = v[w] + 0.5*(m - v[w])
        fc = Fcusto(vc[0], vc[1])

        if fc < f[w]:
            if f[g] < fc:
                v[w] = vc
                f[w] = fc
            else:
                if f[b] < fc:
                    v[w] = v[g]
                    f[w] = f[g]

                    v[g] = vc
                    f[g] = fc
                else:
                    v[w] = v[g]
                    f[w] = f[g]

                    v[g] = v[b]
                    f[g] = f[b]

                    v[b] = vc
                    f[b] = fc
        elif fc > f[w]:
            vs = (v[b] + v[w]) / 2
            fs = Fcusto(vs[0], vs[1])

            v[w] = vs
            f[w] = fs

    print('Iteração', iteracao, sep=' ')
    print(v[b], ', ', f[b])
    print(v[g], ', ', f[g])
    print(v[w], ', ', f[w])
    iteracao += 1

v_best = v[b]
f_best = f[b]

print(v_best)
print('Solução ótima:')
print(f_best)