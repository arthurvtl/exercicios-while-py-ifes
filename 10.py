n = int(input("Informe um número inteiro e positivo: ")) 
i = 1 
cont_64 = 0
soma = 0
while (i<=n): #Verifica se já chegou ao final da repetição 
    if(i%5 == 0):
          soma=soma + i
    if(64%i == 0):
          cont_64 += 1
    i=i+1 
    
print(f"A soma dos múltiplos de 5 entre 1 e N é {soma}")
print (f"A quantidade de números do intervalo são divisores de 64 entre 1 e N é {cont_64}")