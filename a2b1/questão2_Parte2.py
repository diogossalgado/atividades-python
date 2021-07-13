#Programa 2
vetor = [1, 2, 3, 4, 5]
try:
    print (vetor[7])
except IndexError:
    print("A posição não está presente no vetor.") # Erro tratado