# list comprehension

x = [1, 2, 3, 4, 5]
# Valores elevados ao quadrado
y = [i**2 for i in x] # [valor a adicionar laço condição]

print("Usando list comprehension")
print(x)
print(y)

# Apenas valores ímpares
z = [i for i in x if i%2==1]

print(z)