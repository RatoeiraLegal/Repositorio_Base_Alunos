# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

lista = []

repetidor = 0
while repetidor <=3:
    notas = int(input("Digite uma nota: "))
    lista.append(notas)
    repetidor += 1

print("Notas: ")
print(lista)
soma = sum(lista)
média = soma/4
print(f"Média: {média}")