# Desenvolvido por: Gabriel Marlon Viana
# Matrícula: 20243002252

import random

# Transforma o número binário em real
def binarioParaReal(binario, intervalo_min, intervalo_max):
    binario_inverso = binario[::-1]
    somatorio = 0
    bits = len(binario)

    for i in range(bits):
        somatorio += binario_inverso[i] * (2**i)

    real = (somatorio / (2**bits)) * (intervalo_max - intervalo_min) + intervalo_min

    return real

# Roleta de seleção para escolher os melhores pais.
def roletaDeSelecao(custo_relativo):
    posicao = 0
    somador = 0
    x_rand = random.random()

    while posicao < len(custo_relativo):
        somador += custo_relativo[posicao]

        if somador >= x_rand:
            break
        
        posicao += 1
    return posicao

# Processo de cruzamento de pais.
def cruzamento(filho_1, filho_2):
    y = random.randint(0, len(filho_1)-1)
    cromossomos_reservas = filho_1[y:]

    filho_1[y:] = filho_2[y:]
    filho_2[y:] = cromossomos_reservas[0:]

    return filho_1, filho_2

# Processo de mutação direta do filho.
def mutacao(filho):
    j = random.randint(0, len(filho)-1)

    filho[j] = 1 if filho[j] == 0 else 0

    return filho