#Programa mostrar todos os pares no intervalo de 1 a N,  
#sendo N um número inteiro e positivo 

n = int(input("Informe um número inteiro e positivo:")) 
i = 1
while (i<=n):
    if i%2==0: 
        print(i,end=" ") 
    i=i+1 
else: 
    print("\nFim do programa") 