wort = input("Gebe ein Wort ein: ")
dict = {}

for i in range(len(wort)):
    if wort[i] in dict:
        dict[wort[i]] = dict[wort[i]] + 1
    else:
        dict[wort[i]] = 1

print(dict)