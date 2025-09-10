#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
p1 = float(input("Digite o valor do primeiro produto: "))
p2 = float(input("Digite o valor do segundo produto: "))
p3 = float(input("Digite o valor do terceiro produto: "))

if p1 < p2 and p1 < p3:
    print (f"O produto de {p1} é o mais barato")
elif p2 < p1 and p2 < p3:
    print (f"O produto de {p2} é o mais barato")
else:
    print (f"O produto de {p3} é o mais barato")