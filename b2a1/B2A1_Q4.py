linhas, bases = [], []
dict = {
    "Phe": ["UUU", "UUC"], "Leu": ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"],\
    "Ile": ["AUU", "AUC", "AUA"], "Met": ['AUG'], "Val": ["GUU", "GUC", "GUA", "GUG"],\
    "Ser": ["AGU", "AGC","UCU", "UCC", "UCA", "UCG"], "Pro": ["CCU", "CCC", "CCA", "CCG"],\
    "Thr": ["ACU", "ACC", "ACA", "ACG"], "Ala": ["GCG", "GCC", "GCA", "GCG"],\
    "Tyr": ["UAU", "UAC"], "His": ["CAU", "CAC"], "Gln": ["CAA", "CAG"],\
    "Asn": ["AAU", "AAC"], "Lys": ["AAA", "AAG"], "Asp": ["GAU", "GAC"],\
    "Glu": ["GAA", "GAG"], "Cys": ["UGU, UGC"], "Arg": ["CGU, CGC, CGA, CGG", "AGA", "AGG"],\
    "Gly": ["GGU", "GGC", "GGA", "GGG"], "Trp": "UGG",\
    "STOP":["UAA", "UAG", "UGA"]
}
with open('arquivo.txt') as f:
    linhas = f.readlines()

for l in linhas:
    bases.append(l.strip('\n').upper())

count = 0
while (count != len(bases)):
    base = bases[count]
    base = list(base)
    count += 1
    for i in range(0, len(base)):
        if base[i] == "A": 
            base[i] = "U"

        elif base[i] == "T": 
            base[i] = "A"

        elif base[i] == "C": 
            base[i] = "G"

        else:
            base[i] = "C"
        
        bases[count-1] = ''.join(base)

num = 0
num2 = 0
while num != len(bases):
    base = bases[num]
    base = list(base)
    print(''.join(base)+":")
    for i in range(3, len(base)+1, 3):
        seq = ''.join(base[num2: i])
        for k, v in dict.items():
             if seq in v:
                print(k, end = " ")

        num2 += 3
    print("\n")
    num2 = 0
    num += 1
    
f.close()