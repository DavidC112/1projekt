adatok=[]
with open("ki.txt", "r", encoding="utf-8") as f:
    for x in f:
        split=x.split(";")
        split.pop(-1)

def Ellenorzes():
    szam = "szam"
    szoveg = "szoveg"

    string ="".join(split)
    string = string.replace("-","")
    if string.isnumeric() == True:
        return szam

    elif string.isalpha() == True:
        return szoveg

    else:
        return False

def Listabahelyezes():
    if Ellenorzes() == "szam":
        for x in split:
            adatok.append(int(x))
    if Ellenorzes() == "szoveg":
        for x in split:
            adatok.append(x) 

def Egyszerurendezes_novekvo():
    for x in range(len(adatok) - 1):
        for y in range(x + 1, len(adatok)):
            if adatok[x] > adatok[y]:
                adatok[x], adatok[y] = adatok[y], adatok[x]
                
    print(adatok)
def Egyszerurendezes_csokkeno():
    for x in range(len(adatok) - 1):
        for y in range(x + 1, len(adatok)):
            if  adatok[y] > adatok[x]:
                adatok[x], adatok[y] = adatok[y], adatok[x]
                
    print(adatok)
def Kertitorperendezes_novekvo():
    index = 0
    while index < len(adatok):
        if index == 0:
            index = index + 1
        if adatok[index] >= adatok[index - 1]:
            index = index + 1
        else:
            adatok[index], adatok[index-1] = adatok[index-1], adatok[index]
            index = index - 1        
    print(adatok)
def Kertitorperendezes_csokkeno():
    index = 0
    while index < len(adatok):
        if index == 0:
            index = index + 1
        if adatok[index - 1]  >= adatok[index]:
            index = index + 1
        else:
            adatok[index], adatok[index-1] = adatok[index-1], adatok[index]
            index = index - 1        
    print(adatok)

Listabahelyezes()

if Ellenorzes():
    inpt = input("Válaszd ki az algoritmust: egyszerű(e) vagy kertitörpe-rendezés(k): ")
    while inpt != "e" or inpt != "k":
        if inpt == "e" or inpt == "k":
            break
        inpt = input("Válaszd ki az algoritmust: egyszerű(e) vagy kertitörpe-rendezés(k): ")

    inpt_2 = input("Válaszd ki hogy növekvő(n) vagy csökkenő(cs) legyen a renezés: ")
    while inpt_2 != "n" or inpt_2 != "cs":
        if inpt_2 == "n" or inpt_2 == "cs":
            break
        inpt_2 = input("Válaszd ki hogy növekvő(n) vagy csökkenő(cs) legyen a renezés: ")  
    
    if inpt == "e" and inpt_2 == "n":
        Egyszerurendezes_novekvo()
    elif inpt == "e" and inpt_2 == "cs":
        Egyszerurendezes_csokkeno()
    elif inpt == "k" and inpt_2 == "n":
        Kertitorperendezes_novekvo()
    elif inpt == "k" and inpt_2 == "cs":
        Kertitorperendezes_csokkeno()
else:
    print("Az adatok nem megfelelőek")