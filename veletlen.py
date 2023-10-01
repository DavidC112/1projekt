#Plusz feladat: Színezés + Ha az kevesebb számot generálunk mint amennyi lehetőség van az alsó és felső határ között akkor különböző dzámokat generál.

piros = "\033[91m"
zold = "\033[92m"
alap = "\033[0m"

import random
import os

karakter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


print("Melyik opciót szeretnéd választani:\n1. Számok Generálása\n2. Betűk generálása.\n3. ki.txt ellenőrzése számokkal\n4. ki.txt ellenőrzése betűkkel")



def fel1():
    try:                                                                                                #hibakezelés
        sz_also = int(input("Mennyi legyen az alsó határ: ")) 
        sz_felso = int(input("Mennyi legyen a felső határ: ")) 
        sz_db = int(input("Mennyi számot generáljon: ")) 
    except ValueError:                                                                          
        print(f"{piros}Hibás adatokat adtál meg.{alap}")                        
        return
    if sz_also > sz_felso:
        print(f"{piros}Az alsó határ nem lehet nagyobb mint a felső.{alap}")

                                                                                                        #ha működik

    else:
        szamok = []
        if sz_felso - sz_also >= sz_db:
            while(len(szamok)) < sz_db:
                x = random.randint(sz_also, sz_felso)
                if x not in szamok:
                    szamok.append(x)


            with open("ki.txt", "w", encoding="UTF-8") as f: 
                for x in szamok:
                    f.write(f"{x};")


            with open('ki.txt', 'rb+') as f:
                f.seek(-1, os.SEEK_END)             #utolsó ';' törlése
                f.truncate()
                

        else:
            with open("ki.txt", "w", encoding="UTF-8") as f: 
                for i in range(sz_db):
                    x = random.randint(sz_also, (sz_felso))
                    f.write(f"{x};")


            with open('ki.txt', 'rb+') as f:        
                f.seek(-1, os.SEEK_END)
                f.truncate()
                



def felt2():
    try:                                                                                                    #hibakezelés
        b_db = int(input("Mennyi szöveg legyen generálva: "))
    except ValueError:
        print(f"{piros}Hibás adatokat adtál meg.{alap}")
        return

    with open("ki.txt", "w", encoding="UTF-8") as f:
            for i in range(b_db):
                for i in range(random.randint(1, 20)):
                    x= random.choice(range(len(karakter)))
                    f.write(f"{karakter[x]}")
                f.write(f";")

    with open("ki.txt", "rb+") as f:
        f.seek(-1, os.SEEK_END)
        f.truncate()



def fel3():
    try:                                                                                                    #hibakezelés
        sz_also = int(input("Mennyi volt az alsó határ: ")) 
        sz_felso = int(input("Mennyi volt a felső határ: ")) 
        sz_db = int(input("Mennyi szám volt generálva: ")) 
    except ValueError:
        print(f"{piros}Hibás adatokat adtál meg.{alap}")
        return
    

    adatok = []
    db = 0


    try:
        with open("ki.txt", "r", encoding="UTF-8") as f:
            adatok= f.read().split(';')
    except FileNotFoundError:
        print(f"{piros}Nem található a 'ki.txt'.{alap}")
        return
    adatok = [eval(i) for i in adatok]

    for x in adatok:
        db += 1
        if sz_also > x  and x > sz_felso:
              print(f"{piros}A 'ki.txt' nem felel meg a megadott paramétereknek.{alap} 1")
              break
              
    if db != sz_db :
        print(db)  
        print(f"{piros}A 'ki.txt' nem felel meg a megadott paramétereknek.{alap}2")
            
    else:
            print(f"{zold}A 'ki.txt' megfelel a megadott paramétereknek.{alap}")  


        
def fel4():
    try:                                                                                            #hibakezelés                                                                      
        b_db = int(input("Mennyi szöveg volt generálva: "))
    except ValueError:
        print(f"{piros}Hibás adatokat adtál meg.{alap}")
        return
     
    try:                                                                                            #hibakezelés  
        with open("ki.txt", "r", encoding="UTF-8") as f:
            adatok= f.read().split(';')
    except FileNotFoundError:
        print(f"{piros}Nem található a 'ki.txt'.{alap}")
        return  
    

    betuk = []
    y = True
    for x in adatok:
        for i in range(len(x)):
            betuk.append(x[i])

    if len(adatok) != b_db:
        y = False
        print(b_db)
        print(len(adatok))
        print(f"{piros}A fálj nem felel meg a megadott paramétereknek.{alap}")

    for x in betuk:
        if x not in karakter:
            y = False
            print(f"{piros}A fálj nem felel meg a megadott paramétereknek.{alap}")
            break

    if y == True:
        print(f"{zold}Nincs hiba a fájlban.{alap}")

        



while True:
    valasztas = input("Írd be a választott lehetőség számát: ")
    if valasztas == "1":
        print("1") 
        fel1()       
        break

    elif valasztas == "2":
        print("2")
        felt2()
        break

    elif valasztas == "3":
        print("3")
        fel3()
        break

    elif valasztas == "4":
        print("4")
        fel4()
        break
    
    else:
        print(f"{piros}Nincs ilyen opció.{alap}")  