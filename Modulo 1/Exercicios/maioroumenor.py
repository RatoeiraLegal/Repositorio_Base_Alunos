#Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um segundo número: "))
n3 = int(input("Digite um terceiro número: "))

#Maior
if n1 > n2 and n1 > n3:
    print (f"O número {n1} é o maior")
elif n2 > n1 and n2 > n3:
    print (f"O número {n2} é o maior")
else:
    print (f"O maior número é {n3}")

#Menor
if n1 < n2 and n1 < n3:
    print (f"O número {n1} é o menor")
elif n2 < n1 and n2 < n3:
    print (f"O número {n2} é o menor")
else:
    print (f"O menor número é {n3}")
