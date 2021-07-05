palindromo = str(input("Informe a palavra: "))
if palindromo == palindromo[::-1]:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")