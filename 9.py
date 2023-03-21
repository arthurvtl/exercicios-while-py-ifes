#temperatura

temp = float(input("Informe o valor da temperatura:")) 
quantTempInterv = 0 #Quantidade de temperaturas no intervalo 
somaTemp = 0 #Somar as temperaturas para o cálculo da média 
contTemp = 0 #Contar as temperaturas para o cálculo da média 
conttemp30 = 0
temp_maior = temp

while (temp>=0): 
    while temp<5 or temp>55: #Verifica se a temperatura é válida 
        temp=float(input("Erro. A temperatura deve ser entre 5 e 55. Digite novamente:"))  
    if (temp>temp_maior):
        temp_maior=temp
    if (temp>30):
        conttemp30 += 1
    if (temp>=20.5) and (temp <= 35.5): 
        quantTempInterv=quantTempInterv+1 
    somaTemp = somaTemp+temp #Soma os números inteiros entre N e M 
    contTemp=contTemp+1 
    temp=float(input("Informe o valor da temperatura. Para sair informe uma temperatura negativa.")) 
mediaTemp=somaTemp/contTemp 

print(f"Existem {quantTempInterv} temperaturas entre 20.5ºC e 35.5ºC.") 
print(f"A média das temperaturas é {mediaTemp:.2f}") 
print(f"A maior temperatura informada é {temp_maior}")
print(f"{conttemp30} temperaturas são maiores que 30ºC")