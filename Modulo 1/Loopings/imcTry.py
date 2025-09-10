while True:
    try:
        #Dados
        nome = input("Digite seu nome: ")
        peso = float(input("Digite seu peso em (kg): "))
        altura = float(input("Digite sua altura em (m): "))

    #Cálculo
        imc = float(peso / (altura * altura))

    #Mensagem
        if imc < 18.5:
            print(f"{nome}, seu imc é de {imc}, você está abaixo do peso \n Tudo ok!")
        elif imc <= 24.9:
            print(f"{nome}, seu imc é de {imc}, você está com peso adequado \n Tudo ok!")
        elif imc <= 29.9:
            print(f"{nome}, seu imc é de {imc}, você está com sobrepeso \n Tudo ok!")
        elif imc <= 34.9:
            print(f"{nome}, seu imc é de {imc}, você está com obesidade grau I \n Cuidado com a saúde!")
        elif imc <= 39.9:
            print(f"{nome}, seu imc é de {imc}, você está com obesidade grau II \n Cuidado com a saúde!")
        else:
            print(f"{nome}, seu imc é de {imc}, você está com obesidade grau III(mórbida) \n Cuidado com a saúde!")
        break

    except:
        print("Valor inválido!")
    