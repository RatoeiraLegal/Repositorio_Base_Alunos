#Faça um Programa que leia três números e mostre o maior deles.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um terceiro número: "))
maior = n1

if n2 > maior:
    maior = n2
elif n3 > maior:
    maior = n3
else:
    maior = n1

print (f"O manior número é {maior}")