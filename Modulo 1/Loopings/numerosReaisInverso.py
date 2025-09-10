# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

lista = []
repetidor = 0
while repetidor <=9:
    n = float(input("Digite um número: "))
    lista.append(n)
    repetidor +=1

lista = lista[::-1]
print(lista)