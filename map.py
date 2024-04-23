# Função map

def dobro(x):
    return x*2

valor = [1,2,3,4,5]

valor_dobrado = map(dobro, valor) # aplica uma função em toda uma lista

valor_dobrado = list(valor_dobrado) # transforma o objeto em lista
print(valor_dobrado)