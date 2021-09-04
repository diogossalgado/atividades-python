linhas, infectados = [], []
cont, i = 0, 2

with open('questão.txt') as f:
    linha = f.readlines()

for l in linha:
    #Removendo o "\n" que o readlines() gera e adcionando os elementos à uma lista.
    linhas.append(l.strip('\n'))

if int(linhas[1][-1]) > 0:
    infectados.append(linhas[1][0])
else:
    print("0")
    exit()

while cont != int(linhas[0][-1]):
    if i >= int(linhas[1][-1]):
        for x in range(2, len(linhas[i]), 2):
            if linhas[i][x] in infectados:
                for y in range(2, len(linhas[i]), 2):
                    if linhas[i][y] not in infectados:
                        infectados.append(linhas[i][y])
    cont += 1
    i += 1

print(len(infectados))

f.close()