peso = float(input("Qual o seu peso? "))
altura = float(input("Qual sua altura? "))
imc = peso /(altura * altura)

if imc >= 30:
    print("Cuidado com a saúde")
else:
    print("Tudo ok")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesidade Grau I")
elif imc < 39.9:
    print("Obesidade Grau II")
else:
    prit("Obesidade Grau III (mórbida)")