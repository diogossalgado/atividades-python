n = int(input("Valor: "))
ultimo=1
penultimo=1

if (n==0) or (n==1) or (n==2):
    print("1")
else:
    for i in range(2,n):
        t = ultimo + penultimo
        penultimo = ultimo
        ultimo = t
        i = i + 1
print(t)