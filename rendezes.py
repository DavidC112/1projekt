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
    Egyszerurendezes_csokkeno()
    Egyszerurendezes_novekvo()
    Kertitorperendezes_csokkeno()
    Kertitorperendezes_novekvo()
else:
    print("Az adatok nem megfelelőek")