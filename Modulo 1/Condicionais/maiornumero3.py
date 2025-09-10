#Faça um programa que leia 5 números e informe o maior número.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um terceiro número: "))
n4 = int(input("Digite um quarto número: "))
n5 = int(input("Digite um quinto número: "))
maior = 0

while True:
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
        maior = n1
    if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        maior = n2
    if n3 > n2 and n3 > n1 and n3 > n4 and n3 > n5:
        maior = n3
    if n4 > n2 and n4 > n3 and n4 > n1 and n4 > n5:
        maior = n4
    if n5 > n2 and n5 > n3 and n5 > n4 and n5 > n1:
        maior = n5
    break 
print(f"O maior é o {maior}")