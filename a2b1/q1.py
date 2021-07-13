try:
    x=int(input("Entre com um número: "))
    y=int(input("Entre com outro número: "))
except ValueError:
    print("O valor informado não é um número inteiro.")

try:
    print( x,'/', y,'=', x/y )
except ZeroDivisionError:
    print("O valor não pode ser dividido por zero.")

