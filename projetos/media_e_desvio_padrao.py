import numpy as np

# Média Aritmética
quantidade = int(input('Quantidade de valores: '))

media = 0
valores = np.empty((quantidade, 1))
valores.fill(np.nan)

for i in range(quantidade):
    print('valor', i + 1, ':', sep=' ')
    valores[i] = float(input(' '))
    media += valores[i]

media /= quantidade

print('A média é:', media, sep=' ')

# Desvio Padrão
desvio_padrao = 0
for i in range(quantidade):
    desvio_padrao += (media - valores[i])**2

desvio_padrao /= quantidade * (quantidade - 1)

print('O desvio padrão é:', desvio_padrao, sep=' ')