def escreva():
    print("Ola, Mundo!")

escreva()

#Argumento
def escreva(msg):
    print(msg)

escreva("Ola, Mundo!")

#Argumento2
def soma(n1,n2):
    print(n1 + n2)

soma(1,2)
soma(3,4)

#Argumento e Retorno
def soma(n1,n2):
    return n1 + n2

print(soma(6,2))
print(soma(3,3))