# cont divisivel por 5  e 2
num = int(input("Informe um núm. inteiro e positivo:"))

contNumDiv2 = 0
contNumDiv5 = 0
contNumDiv10 = 0
contNumNDiv = 0

while (num > 0 ):
    if (num%2 == 0 ):
        contNumDiv2 +=1 
    if (num%5 == 0 ):
        contNumDiv5 += 1
    if (num%10 == 0):
        contNumDiv10 += 1
    if (num%2 != 0 and num%5 != 0 and num%10 != 0  ):
        contNumNDiv += 1
    num=int(input("Informe um núm. inteiro e positivo:Terminar com num menor que 0: "))
    
print(f" A quantidade de numeros que são divisíveis por 2 é {contNumDiv2}")
print(f" A quantidade de numeros que são divisíveis por 5 é {contNumDiv5}")
print(f" A quantidade de numeros que são divisíveis por 10 é {contNumDiv10}")
print(f" A quantidade de numeros que não são divisíveis por 2,5 e 10 é {contNumNDiv}")