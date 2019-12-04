def przelicz(liczba, fr, to):
    PREPARE = "Input:```\n" + liczba + " from " + str(fr) + "-base to " + str(to) + "-base```\nOutput:```\n"
    licz = liczba.split(".")
    pot = len(licz[0])-1
    suma = 0
    for i in licz[0]:
        if(ord(i) >= 65 and ord(i) <= 90):
            suma += (ord(i)-55)*(fr**pot)
        else:
            suma += int(i)*(fr**pot)
        pot -= 1
    odp = []
    while(suma != 0):
        res = suma%to
        if(res >= 10):
            odp.append(chr(res+55))
        else:
            odp.append(str(res))
        suma//=to
    PREPARE += "".join(odp[::-1]) + "```"
    return PREPARE
        
        