linhas, infectados = [], []
cont, i = 0, 2

with open('questão.txt') as f:
    linha = f.readlines()

#Para cada linha do arquivo
for l in linha:
    #Remove o "\n" que o readlines() gera e adciona os elementos à uma lista.
    linhas.append(l.strip('\n'))

#Caso o infectado tenha participado de ao menos uma reunião ele é adicionado a uma lista.
if int(linhas[1][-1]) > 0:
    infectados.append(linhas[1][0])
#Caso contrário o programa apenas retorna 0 infectados e encerra.
else:
    print("0")
    exit()

#Enquanto o contador for diferente do total de reuniões
while cont != int(linhas[0][-1]):
    #Verifica se um infectado já participou de ao menos uma reunião
    if i >= int(linhas[1][-1]):
        for x in range(2, len(linhas[i]), 2):
            #Se sim, verifica se um infectado está presente
            if linhas[i][x] in infectados:
                for y in range(2, len(linhas[i]), 2):
                    #Caso esteja todos os não infectados são adicionados à uma lista.
                    if linhas[i][y] not in infectados:
                        infectados.append(linhas[i][y])
    cont += 1
    i += 1

#Imprime a quantidade de infectados
print(len(infectados))

f.close()
