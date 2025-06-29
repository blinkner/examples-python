# Notas escolares
# Escrito por: blinkner

def media(x,y):
    return (x+y)/2

nota1 = int(input("Entre com a primeira nota: "))
nota2 = int(input("Entre com a segunda nota: "))

nota_final = media(nota1, nota2)

if nota_final >= 6:
    print("APROVADO!")
else:
    print("REPROVADO!")
