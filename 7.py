#Programa para ler números reais, e mostrar: 
#a) Quantos estão no intervalo entre 10 e 50; 
#b) Quantos são negativos 
# Sair quando for digitado o valor zero 

num = int(input("Informe um núm. inteiro e positivo:"))
contNum = 0
contNeg = 0
while (num != 0):
    if (num >= 10 and num<=50 ):
        contNum += 1
    if (num<0):
        contNeg += 1
    num=int(input("Informe um núm. inteiro e positivo:Terminar com num igual a 0: "))
    
print(f"A quantidade de números informados entre 10 e 50 é {contNum}")
print(f"A quantidade de numeros negativos informados é {contNeg} ")