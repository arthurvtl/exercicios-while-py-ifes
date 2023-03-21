n=int(input("Informe um número inteiro e positivo:" )) 
m=int(input("Informe um número inteiro e positivo:" )) 
contMult3 = 0 
contDiv48 = 0 
soma = 0 
i = n 

while (i<=m): 
    if (i%3==0): #conta múltiplos de 3  
        contMult3 = contMult3+1 
    if (48%i==0): #Conta divisores de 48 
        contDiv48 = contDiv48+1 
    soma = soma+i #Soma os números inteiros entre N e M 
    i=i+1 

print("Existem ",contMult3," múltiplos de 3 entre ",n," e ",m) 
print("Existem ",contDiv48," divisores de 48 entre ",n," e ",m) 
print("Soma dos números entre ",n," e ",m, " é:",soma) 