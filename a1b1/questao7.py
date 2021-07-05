n = 1
cont = 0
n1 = 0
rodou = 0
while (n != 0):
    n = int(input("Valor: "))
    rodou = rodou + 1
    cont = cont + 1
    if cont == 1:
        n1 = n
    if cont == 2:
        soma = n + n1
        cont = 0
        
rodou = rodou - 1
print(soma, rodou)
print(soma/rodou)