# -*- coding: utf-8 -*-
import random

# random.seed(1) # força retornar mesmos valores
numero = random.randint(0,10) # numero aleatorio entre 0 e 10
print(numero)

lista = [6,45,9]
numero = random.choice(lista) # valor aleatorio de uma lista
print(numero)