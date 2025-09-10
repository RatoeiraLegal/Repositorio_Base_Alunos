#Faça um programa para imprimir:
#   1
#    1   2
#    1   2   3
#    .....
#    1   2   3   ...  n
#para um n informado pelo usuário. Use uma função que receba um valor n inteiro 

def repetição(n):
    start = 1
    while start <= n:
        repetidor = 1
        linha = ''
        while repetidor <= start:
            linha += str(repetidor) + ' '
            repetidor += 1
        print(linha)
        start += 1

n = int(input("Digite um número: "))
repetição(n)