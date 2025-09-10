#Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação
while True:
    A = int(input("Digite a população inicial A: "))
    B = int(input("Digite a população inicial B: "))
    taxa1 = int(input("Digite a taxa do A em %: "))
    taxa2 = int(input("Digite a taxa do B em %: "))
    anos = 0
    if A and B and taxa1 and taxa2 and anos 

while A <= B:
    CrescA = (A * taxa1) / 100
    CrescB = (B * taxa2) / 100
    A += CrescA
    B += CrescB
    anos += 1

print(f"levaria {anos} anos")