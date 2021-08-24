import csv

class dicionario(dict):
  
    def __init__(self):
        self = dict()
          
    def add(self, key, value):
        self[key] = value

notas = dicionario()
media = 0
with open('notas.csv', 'r') as arquivo:
    leitor = csv.reader(arquivo)
    for linha in leitor:
        surfista = linha[0]
        linha.remove(surfista)
        linha.remove(max(linha))
        linha.remove(min(linha))

        for i in range(0, len(linha)):
            linha[i] = float(linha[i])

        media = sum(linha)/len(linha)
        media = ('{:.2f}'.format(media))

        if surfista in notas.keys():
            notas[surfista].append(media)
        else:
            notas.add(surfista, [])
            notas[surfista].append(media)

for i in notas:
    maior = max(notas[i])
    notas[i].remove(maior)
    maior2 = (max(notas[i]))
    print(i, "-", '{:.2f}'.format(float(maior) + float(maior2)))
            
arquivo.close()
