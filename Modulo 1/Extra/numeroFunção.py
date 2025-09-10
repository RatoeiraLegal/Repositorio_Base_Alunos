#Faça um programa para imprimir:
#   1
#    2   2
#    3   3   3
#    .....
#    n   n   n   n   n   n  ... n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro e 

def repetição(n):
    start = 1
    while start <= n:
        print((str(start) + ' ')* start)
        print()
        start += 1

n = int(input("Digite um número: "))
repetição(n)