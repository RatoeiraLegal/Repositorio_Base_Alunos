# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

lista = []
consoantes = []
vogais = ['a' , 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

repetidor = 1

while repetidor <= 10:
    caracteres = input("Digite caracteres: ")
    lista.append(caracteres)
    if caracteres not in vogais:
        consoantes.append(caracteres)
    repetidor += 1

print(consoantes)
print("Conta com os dedos aí")