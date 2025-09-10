#Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def reverso(n):
    print(str(n)[::-1])

n = int(input("Digite um número: "))

reverso(n)