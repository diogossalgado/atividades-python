def SomaNum(a, b):
    if (a + b < 1000) :
        print (a + b)
    else:
        raise OverflowError("Maior que 1000.") 

try:
    x = int(input("Informe 1º valor: "))
    y = int(input("Informe o 2º valor: "))
    SomaNum(x, y)
except ValueError:
    print("O valor informado não pode ser utilizado.")
