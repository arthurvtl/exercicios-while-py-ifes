# cont 10 e 50
num = int(input("Informe um núm. inteiro e positivo: "))
contNum = 0
soma = 1
while (num != 0):
    if (num >= 10 and num<=50 ):
        contNum += 1
    else:
        soma = soma + num
    num=int(input("Informe um núm. inteiro e positivo:Terminar com num igual a 0: "))

print(f"A quantidade de números informados entre 10 e 50 é {contNum}")
print(f"A soma dos números fora desse intervalo é {soma:.2f}")