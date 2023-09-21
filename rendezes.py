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

Listabahelyezes()

if Ellenorzes():
    print("müködik")
else:
    print("Az adatok nem megfelelőek")