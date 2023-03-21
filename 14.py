num = int(input("Informe um número inteiro:"))
soma = 0
i = 2
j = 2

while (i<=num):
    if (i%5==0):
        print(i)
    else:
        if (j%3==0):
            soma=soma+j
    i=i+1
    j=j+2
    
print("soma:",soma)