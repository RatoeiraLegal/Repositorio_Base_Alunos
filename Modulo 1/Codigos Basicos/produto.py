#nome do produto/valor/desconto/calcule o desconto/calcule o preço final/ apresentar preço e o nome

nome_produto = input("Qual o nome do produto? ")
valor_produto = float(input("Qual o valor do produto? "))
desconto = int(input("Qual o valor do desconto? "))

valor_desconto = valor_produto * (desconto / 100)
valor_final = valor_produto - valor_desconto
print (f"O produto {nome_produto} está por R$ {valor_final}")