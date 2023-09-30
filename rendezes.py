import re

adatok=[]
with open("ki.txt", "r", encoding="utf-8") as f:
    for x in f:
        split=x.split(";")
        split.pop(-1)

def Ellenorzes():
    string ="".join(split)
    string = string.replace("-","")
    if string.isnumeric() is True:
        return "szam"

    elif bool(re.match("^[A-Za-z]*$", string)) is True:
        return "szoveg"

    else:
        return False

def ListabaHelyezes():
    if Ellenorzes() == "szam":
        for x in split:
            adatok.append(int(x))
    if Ellenorzes() == "szoveg":
        for x in split:
            adatok.append(x) 

def Egyszeru_novekvo():
    for x in range(len(adatok) - 1):
        for y in range(x + 1, len(adatok)):
            if adatok[x] > adatok[y]:
                adatok[x], adatok[y] = adatok[y], adatok[x]
                
    for adat in adatok:
        print(adat, end=" ")
    print()

def Egyszeru_csokkeno():
    for x in range(len(adatok) - 1):
        for y in range(x + 1, len(adatok)):
            if  adatok[y] > adatok[x]:
                adatok[x], adatok[y] = adatok[y], adatok[x]
                
    for adat in adatok:
        print(adat, end=" ")
    print()

def Kertitorpe_novekvo():
    index = 0
    while index < len(adatok):
        if index == 0:
            index = index + 1
        if adatok[index] >= adatok[index - 1]:
            index = index + 1
        else:
            adatok[index], adatok[index-1] = adatok[index-1], adatok[index]
            index = index - 1        
    
    for adat in adatok:
        print(adat, end=" ")
    print()

def Kertitorpe_csokkeno():
    index = 0
    while index < len(adatok):
        if index == 0:
            index = index + 1
        if adatok[index - 1]  >= adatok[index]:
            index = index + 1
        else:
            adatok[index], adatok[index-1] = adatok[index-1], adatok[index]
            index = index - 1        
    
    for adat in adatok:
        print(adat, end=" ")
    print()

def Adatbekeres_szam():
    while True:
        try:
            inpt = int(input("írj be egy új számot: "))
            break
        except ValueError:
            print("Az adat a megadott feltételeknek nem felele meg, kérlek próbáld újra!")

    return inpt

def Adatbekeres_szoveg():
    while True:
        try:
            inpt = input("Írj be egy új szöveget: ")
            if inpt.isalpha():
                break
        except ValueError:
            print("Az adat a megadott feltételeknek nem felele meg, kérlek próbáld újra!") 

    return inpt

def Indexbekeres():
    while True:
        try:
            inpt = int(input("Adja meg a törölni kívánt adat indexét:"))
            break
        except ValueError:
            print("Nem megfelelő az adat")
        except IndexError:
            print("Nem megfelelő az index")  
    
    return inpt

def AdatTorles():
    while True:
        try:
            adat_torles_szama = int(input("Szányszor szeretnél törölni adat? "))
            break
        except ValueError:
            print("Nem számot adtál meg! Próbáld újra.")
    
    return adat_torles_szama

if Ellenorzes():
    ListabaHelyezes()

    print("A zárjelben lévő betű beírásával tudsz választani")
    inpt = input("Válassza ki az algoritmust: egyszerű cserés rendezés(e) vagy kertitörpe-rendezés(k): ")
    while inpt != "e" or inpt != "k":
        if inpt == "e" or inpt == "k":
            break
        inpt = input("Válaszd ki az algoritmust: egyszerű cserés rendezés(e) vagy kertitörpe-rendezés(k): ")

    inpt_2 = input("Válaszd ki hogy növekvő(n) vagy csökkenő(cs) legyen a renezés: ")
    while inpt_2 != "n" or inpt_2 != "cs":
        if inpt_2 == "n" or inpt_2 == "cs":
            break
        inpt_2 = input("Válaszd ki hogy növekvő(n) vagy csökkenő(cs) legyen a renezés: ")  
    
    if inpt == "e" and inpt_2 == "n":
        Egyszeru_novekvo()
        
        if Ellenorzes() == "szam":
            adatok.append(Adatbekeres_szam())
            Egyszeru_novekvo()
        else:
            adatok.append(Adatbekeres_szoveg())
            Egyszeru_novekvo()

    elif inpt == "e" and inpt_2 == "cs":
        Egyszeru_csokkeno()

        if Ellenorzes() == "szam":
            adatok.append(Adatbekeres_szam())
            Egyszeru_csokkeno()

        else:
            adatok.append(Adatbekeres_szoveg())
            Egyszeru_csokkeno()

    elif inpt == "k" and inpt_2 == "n":
        Kertitorpe_novekvo()

        if Ellenorzes() == "szam":
            adatok.append(Adatbekeres_szam())
            Kertitorpe_novekvo()

        else:
            adatok.append(Adatbekeres_szoveg())
            Kertitorpe_novekvo()

    elif inpt == "k" and inpt_2 == "cs":
        Kertitorpe_csokkeno()

        if Ellenorzes() == "szam":
            adatok.append(Adatbekeres_szam())
            Kertitorpe_csokkeno()

        else:
            adatok.append(Adatbekeres_szoveg())
            Kertitorpe_csokkeno()
    
    print("Szeretnél a listából adatot törölni? igen/nem: ", end="")
    adat_torles = input("")
    
    if adat_torles == "igen":
        torlesek_szama = AdatTorles()
        i = 0 
        while torlesek_szama > i:
            adatok.pop(Indexbekeres())
            i +=1
            print("Az új adatlista", adatok)
         
else:
    print("Az adatok nem megfelelőek")