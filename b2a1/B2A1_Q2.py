linhas, bases = [], []
base = ' '
with open('arquivo.txt') as f:
    linhas = f.readlines()

for l in linhas:
    bases.append(l.strip('\n'))
      
count = 0
while (count != len(bases)):
    base = bases[count]
    tam = len(base)
    print("Base Nitrogenada:", base)
    base = list(base)
    count += 1
    for i in range(0, tam):
        if base[i] == "A": 
            base[i] = "T"

        elif base[i] == "T": 
            base[i] = "A"

        elif base[i] == "C": 
            base[i] = "G"

        else:
            base[i] = "C"

    print("Fita Suplementar:", ''.join(base), "\n")
             
f.close()