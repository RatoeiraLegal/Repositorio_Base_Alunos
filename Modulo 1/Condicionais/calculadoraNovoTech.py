def calculadora(escolha, n1, n2):
    if escolha == 1:
        resultado = n1 + n2
    elif escolha == 2:
        resultado = n1 - n2
    elif escolha == 3:
        resultado = n1 * n2
    elif escolha == 4:
        resultado = n1 / n2
    else:
        resultado = "Nenhuma opção válida"

    return resultado
escolha = int(input("Escolha a operação: \nSoma = 1 \nSubtração = 2 \nMultiplicação = 3 \nDivisão = 4 \nEscolha: "))
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(calculadora(escolha, n1, n2))