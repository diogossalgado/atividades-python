
n = int(input("Digite o valor: "))
cont = 1
n_fat = 1
while cont <= n:
    n_fat = n_fat * cont
    cont = cont + 1

print("{}! = {}".format(n, n_fat))