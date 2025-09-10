#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

def contador(n):
    quantidade = len(str(n))
    print(quantidade)

n = int(input("Digite um número positivo: "))
contador(n)