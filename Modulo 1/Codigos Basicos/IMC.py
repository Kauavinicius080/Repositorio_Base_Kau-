print("Seja bem vindo seu imenso")

nome = str(input("DIgite seu nome:"))
peso = float(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))

imc = peso / (altura * altura)

if imc <= 18.5:
    print(f"{nome} voce esta abaixo do peso {imc}")
elif imc <= 24.9:
    print(f"{nome} voce esta com o peso normal {imc}")
elif imc <= 29.9:
    print(f"{nome} voce esta com obsidade grau I {imc}")
elif imc <=39.9:
    print(f"{nome} Voce esta com obesidade grau II {imc}")
elif imc <=40:
    print(f"{nome} irmão infezlimente você esta com obesidade grau III {imc}")
