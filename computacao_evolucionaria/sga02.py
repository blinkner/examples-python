# Desenvolvido por: blinkner

import computacao_evolucionaria.funcoes02 as funcoes
import numpy as np
import matplotlib.pyplot as plt
import math

# Variáveis gerais
popsize = 15 # Tamanho da população
bits = 12 # Quantidade de bits dos indivíduos da população
maxgen = 30 # Número máximo de gerações
gen = 0 # Monitoramento de gerações
pc = 0.8 # Taxa de cruzamento
pm = 0.05 # Taxa de mutação
intervalo_max = 2 # Intervalo superior
intervalo_min = -1 # Intervalo inferior

pop = np.empty((popsize, bits)) # Inicialização do vetor de população binário.
pop.fill(np.nan)

pop_real = np.empty((popsize, 1)) # Inicialização do vetor de população real.
pop_real.fill(np.nan)

f = np.empty((popsize, 1)) # Inicialização do vetor da função custo.
f.fill(np.nan)

p = np.empty((popsize, 1)) # Inicialização do vetor de valor custo relativo.
p.fill(np.nan)

filhos = np.empty((popsize, bits)) # Inicialização do vetor dos filhos.
filhos.fill(np.nan)

f_filhos = np.empty((popsize, 1)) # Inicialização do vetor da função custo para os filhos.
f_filhos.fill(np.nan)

f_best = np.empty((maxgen, 1)) # Variável para plotagem no gráfico f_best x gen.
f_best.fill(np.nan)

# Criação da população inicial.
pop = np.random.randint(0, 2, (popsize, bits))

# Transforma os indivíduos da população inicial de valores binários em reais e os avalia pela função objetivo.
for i in range(popsize):
    pop_real[i] = funcoes.binarioParaReal(pop[i], intervalo_min, intervalo_max)
    f[i] = pop_real[i] * np.sin(10 * np.pi * pop_real[i]) + 2

# Variável para controle da f_best a ser plotada no gráfico.
f_best[gen] = max(f)
gen += 1

while gen < maxgen:
    # Define o valor custo relativo de cada indivíduo para fazer a seleção de pais.
    for i in range(popsize):
        p[i] = f[i] / np.sum(f)
    
    pais = [] # Variável para controle dos pais escolhidos a cada iteração.
    indices_disponiveis = list(range(popsize)) # Variável para controlar quais pais ainda não foram escolhidos.
    # Roleta de seleção para escolher os melhores pais.
    i = 0
    while i < math.ceil(popsize / 2):
        # Escolha dos pais de forma individual e não repetitiva.
        for j in range(2):
            if len(indices_disponiveis) == 0:
                break

            indice_pai = funcoes.roletaDeSelecao(p)
            while True:
                # Verifica se o pai ainda não foi escolhido, se já foi, escolhe outro pai.
                if indice_pai in indices_disponiveis:
                    break
                else:
                    indice_pai = funcoes.roletaDeSelecao(p)
            indices_disponiveis.remove(indice_pai)
            pais.append(indice_pai)
        
        # Evita o cruzamento do último pai que não possui par.
        if len(indices_disponiveis) == 0:
            break

        # Cruzamento dos pais escolhidos nessa iteração.
        tc = np.random.rand()
        if tc >= pc:
            filhos[pais[0]], filhos[pais[1]] = funcoes.cruzamento(pop[pais[0]], pop[pais[1]])

            # Mutação dos direta de cada filho.
            for j in range(2):
                tm = np.random.rand()
                if tm <= pm:
                    filhos[pais[j]] = funcoes.mutacao(filhos[pais[j]])

        # Limpa a lista de controle de pais para os próximos serem escolhidos.
        pais = []

        # Incrementa a iteração de escolha de pais.
        i += 1

    pop_real.fill(np.nan)

    # Transforma os indivíduos da população de binário para real e os avalia pela função objetivo.
    for i in range(popsize):
        pop_real[i] = funcoes.binarioParaReal(filhos[i], intervalo_min, intervalo_max)
        f_filhos[i] = pop_real[i] * np.sin(10 * np.pi * pop_real[i]) + 2

    for i in range(popsize):
        if f_filhos[i] > f[i]:
            pop[i] = filhos[i]
            f[i] = f_filhos[i]

    f_best[gen] = max(f)

    filhos.fill(np.nan)
    f_filhos.fill(np.nan)

    # Incrementa a iteração de nova geração.
    gen += 1

# Define as gerações a serem plotadas no gráfico.
x = np.linspace(0, 30, 30, endpoint=True)

# Plota o gráfico do melhor valor custo por geração.
plt.figure(figsize=(8,5), dpi=(120))
plt.plot(x, f_best, color='red', marker='o', linewidth=0, label='custo máximo por geração')
plt.title('Melhor valor custo por geração')
plt.legend()
plt.xlabel('geração')
plt.ylabel('custo máximo')
plt.show()