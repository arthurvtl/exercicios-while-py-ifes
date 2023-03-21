n = int(input("Informe um número inteiro e positivo: ")) 
i = 1
while (n != 0): #Verifica se já chegou ao final da repetição 
    while(i<=n):
        if(i%5 == 0):
            print(i)
        i=i+1
    n = int(input("Informe um número inteiro e positivo:(Para sair do programa digite o numero 0)"))