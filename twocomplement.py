
for i in range(0, 10):
    print("Zahl " + str(i) )
    zahl_binaer = bin(i)
    print("Zahl binär geschrieben:  " + zahl_binaer)
    onecomplement = ~i
    onecomplement_binaer = bin(onecomplement)
    print("1-Komplement binär geschrieben:  " + onecomplement_binaer)
    twocomplement = onecomplement + 1
    twocomplement_binaer = bin(onecomplement)
    print("2-Komplement binär geschrieben:  " + twocomplement_binaer)
 
    if (len(zahl_binaer) < len(twocomplement_binaer)):
        print("overflow")