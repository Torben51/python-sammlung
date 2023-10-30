dna = input("Schriebe eine DNA-Sequenz mit A, T, C, G: ")
l = list(dna)
ergebnis = l
for i in range(len(l)):
    if l[i] == 'A':
        l[i] = 'T'
    elif l[i] == 'T':
        l[i] = 'A'
    elif l[i] == 'C':
        l[i] = 'G'
    elif l[i] == 'G':
        l[i] = 'C'
    ergebnis[len(l) - i - 1] = l[i]
print(ergebnis)