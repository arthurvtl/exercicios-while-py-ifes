contHabMAlt = 0 
somaHabId = 0 
contHabId = 0 
cont_dif = 0
idade = int(input("Informe a idade do habitante:")) 
cont_idadeF = 0
soma_idadeF = 1

while (idade>=0): 
    sexo=input("Informe o sexo do habitante(M/F:") 
    altura=float(input("Informe a altura do habitante, em metros:")) 
    if (sexo=="M") and (altura>=1.70): 
        contHabMAlt=contHabMAlt+1 
    if idade>=20 and idade<=40: 
        somaHabId=somaHabId+altura 
        contHabId=contHabId+1 
    if (altura>1.65 and altura<1.85) and (sexo == "F") and (idade>30):
        cont_dif += 1
    if (sexo == "F"):
        cont_idadeF += 1 
        soma_idadeF = soma_idadeF + idade
    idade=int(input("Informe a idade do habitante. Para sair, informe uma idade negativa:")) 
if contHabId>0: 
    mediaHabAlt=somaHabId/contHabId 
    print(f"Média de altura dos habitantes com idade entre 20 e 40 anos: {mediaHabAlt:.2f}") 
else: 
    print("Nenhum habitante tem entre 20 e 40 anos.") 
media_idadeF = soma_idadeF/cont_idadeF

print(f"A média de idade das pessoas do sexo feminino {media_idadeF}")
print(f"{contHabMAlt} são do sexo masculino e tem acima de 1.70m.")
print(f"{cont_dif} habitantes tem entre altura entre 1.65m e 1.85m, são do sexo feminino e tem acima de 30 anos de idade.  ")