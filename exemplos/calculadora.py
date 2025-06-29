# Calculadora básica
# Escrito por: blinkner

num1 = int(input("Entre com o primeiro número: "))
num2 = int(input("Entre com o segundo número: "))
sinal = input("Entre com o sinal [+, -, *, /]: ")

# Dicionário com as operações
op = {
    "+":num1 + num2,
    "-":num1 - num2,
    "*":num1 * num2,
    "/":num1 / num2
}

print(op[sinal])