# Equação de bhaskara
# Escrito por: blinkner
import math

a = float(input("Entre com o coeficiente A: "))
b = float(input("Entre com o coeficiente B: "))
c = float(input("Entre com o coeficiente C: "))
x = []

delta = b**2 - 4*a*c

if delta < 0:
    print("Não possui raízes reais.")
elif delta == 0:
    x.append((-b)/(2*a))
else:
    x.append((-b + math.sqrt(delta))/(2*a))
    x.append((-b - math.sqrt(delta))/(2*a))

print("As Raízes são: ")
for i in x:
    print(i)