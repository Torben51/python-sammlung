einrueckung = "     "
nummern = "1"

for x in range(2, 8):
    print(einrueckung + nummern)
    nummern = str(x) + nummern + str(x)
    einrueckung = einrueckung[:-1]