# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
#Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. 

def conversor (hora, minutos):
    if hora < 12:
        print(f"São {hora}:{minutos} A.M.")
    else:
        hora = hora - 12
        print(f"São {hora}:{minutos} P.M") 

hora = int(input("Digite as horas: "))
minutos = int(input("Digite os minutos: "))

conversor(hora,minutos)

#caguei para duas funções, ta funcionando sem