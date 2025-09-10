def converterDolarReal(valor, converter):
    if converter == 1:
        convertido = valor * 5.8
    elif converter ==2:
        convertido = valor / 5.8
    else:
        convertido = "Nenhuma opção válida"

    return convertido
converter = int(input("Converter Dólar para Real digite 1: \nConverter Real para Dólar digite 2:"))
valor = float(input("Digite o valor a ser convertido: "))

print(converterDolarReal(valor, converter))