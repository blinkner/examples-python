# Desenvolvido por: blinkner

import random

# Gera uma população aleatória pela função random.
def pop1(popsize):
    pop = list(range(popsize))

    for i in pop:
        pop[i] = random.random()

    return pop

# Gera uma população aleatória pela função uniform.
def pop2(intervalo_min, intervalo_max, popsize):
    pop = list(range(popsize))

    for i in pop:
        pop[i] = random.uniform(intervalo_min, intervalo_max)

    return pop

# Gera uma população aleatória pela função randrange.
def pop3(intervalo_min, intervalo_max, popsize, passo=1):
    pop = list(range(popsize))

    for i in pop:
        pop[i] = random.randrange(intervalo_min, intervalo_max, passo)

    return pop

# Gera uma população aleatória pela função randint.
def pop4(intervalo_min, intervalo_max, popsize):
    pop = list(range(popsize))

    for i in pop:
        pop[i] = random.randint(intervalo_min, intervalo_max)

    return pop