# Cálculo de IMC

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Entre com seu peso: (kg): "))
altura = float(input("Entre com sua altura (m): "))

IMC = calcular_imc(peso, altura)

if IMC >= 16 and IMC <= 16.9:
    situacao = "Muito abaixo do peso."
elif IMC >= 17 and IMC <= 18.4:
    situacao = "Abaixo do peso."
elif IMC >= 18.5 and IMC <= 24.9:
    situacao = "Peso normal."
elif IMC >= 25 and IMC <= 29.9:
    situacao = "Acima do peso."
elif IMC >= 30 and IMC <= 34.9:
    situacao = "Obesidade grau I."
elif IMC >= 35 and IMC <= 40:
    situacao = "Obesidade grau II."
elif IMC > 40:
    situacao = "Obesidade grau III."
else:
    situacao = "Extremamente abaixo do peso."

print("\nSeu IMC é:")
print(IMC)
print("Você está: " + situacao)
