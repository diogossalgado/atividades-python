linhas, bases = [], []
with open('arquivo.txt') as f:
    linhas = f.readlines()

for l in linhas:
    bases.append(l.strip('\n'))
      
for i in range(0, len(bases)):
    print("{} - A: {}, C: {}, G: {}, T: {}\n".format(bases[i], bases[i].count("A"), bases[i].count("C"), bases[i].count("G"), bases[i].count("T")))

f.close()