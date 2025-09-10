while True:   
    try:
        converter = int(input("Converter Dólar para Real digite 1: \nConverter Real para Dólar digite 2: \nEscolha: "))
        valor = float(input("Digite o valor a ser convertido: "))
        def converterDolarReal(valor, converter):
            if converter == 1:
                convertido = valor * 5.8
            elif converter ==2:
                convertido = valor / 5.8
            return convertido
        break
    except:
        print()
        print("Valor invlálido!")
        print()
 

print(converterDolarReal(valor, converter))