#Beolvasás, adatszerkezet létrehozása
l=[]
with open("ki.txt", "r", encoding="utf-8") as f:
    for x in f:
        adatok=x.strip("\n").strip(";")
        l.append(adatok) 
        
def Ellenorzes():
    #ez kicsit másképp működik mint ahogy nekem kell   
    """if all([isinstance(x, int) for x in l]) is True:
        print("Az adatszerkezet megfelelő")
    else:
        print("Az adatszerkezet nem megfelelő")"""            

Ellenorzes()

