valor_total = int(input("Digite o preço original: "))
porcentagem = int(input("Digite o desconto: "))

desconto = valor_total * (porcentagem/100)
preço_final = valor_total - desconto
print("O valor com o desconto é",preço_final,"R$")