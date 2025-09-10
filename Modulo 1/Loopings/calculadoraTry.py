while True:
    try:
        print()
        escolha = int(input("Escolha a operação: \nSoma = 1 \nSubtração = 2 \nMultiplicação = 3 \nDivisão = 4 \nEscolha: "))
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        def calculadora(escolha, n1, n2):
            if escolha == 1:
                resultado = n1 + n2
            elif escolha == 2:
                resultado = n1 - n2
            elif escolha == 3:
                resultado = n1 * n2
            elif escolha == 4:
                resultado = n1 / n2
            return resultado
        break
    except:
        print()
        print("Digite um valor válido!")
        print()

print()
print(f"Resultado: {calculadora(escolha, n1, n2)}")