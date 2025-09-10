#Faça um Programa que peça dois números e imprima o maior deles.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

if n2 < n1:
    print(f"O número {n1} é o maior")
else:
    print(f"O número {n2} é o maior")