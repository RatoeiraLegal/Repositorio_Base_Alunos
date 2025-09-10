# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números ÍMPARES no vetor ímpar. Imprima os três vetores.

lista = []
par = []
impar = []
repetidor = 1


while repetidor <= 20:
    n = int(input(f"Digite o {repetidor}º: "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    repetidor += 1

print(f"Total: \n {lista}")
print(f"Pares: \n {par}")
print(f"impares: \n {impar}")