# idade, sexo e salario

idade = int(input("Informe a idade do habitante:")) 
soma_salaraio = 1
cont_salario = 0
cont_F = 0
idade_menor = idade
idade_maior = idade
menor_salario = 9999999999
idade_menor_salario = 0
sexo_menor_salario = " "

while (idade>=0):
    sexo=input("Informe o sexo do habitante(M/F): ") 
    salario=float(input("Informe o salario do habitante: "))
    cont_salario += 1
    soma_salaraio= soma_salaraio + salario
    if (idade>idade_maior):
        idade_maior = idade
    if (idade<idade_menor):
        idade_menor = idade
    if (salario < menor_salario):
        menor_salario = salario
        idade_menor_salario = idade
        sexo_menor_salario = sexo
    if (sexo == "F"):
        cont_F += 1
    idade=int(input("Informe a idade do habitante. Para sair, informe uma idade negativa:"))

media_salario = soma_salaraio/cont_salario
print(f"A media de salario dos habitantes é {media_salario}")
print(f"A quantidade de mulheres entre os habitantes é {cont_F}")
print(f"A menor idade entre dos habitantes é {idade_menor} e a maior idade entre os habitantes é {idade_maior}")
print(f"A pessoa com menor salário {menor_salario} tem {idade_menor_salario} anos e é do sexo {sexo_menor_salario}")