import random
import string

print("Melyik opciót szeretnéd választani:\n1. Számok Generálása\n2. Betűk generálása.\n3. ki.txt ellenőrzése számokkal\n4. ki.txt ellenőrzése betűkkel")


def fel1():
    sz_also = int(input("Mennyi legyen az alsó határ: ")) 
    sz_felso = int(input("Mennyi legyen a felső határ: ")) 
    sz_db = int(input("Mennyi számot generáljon: ")) 
    
    
    with open("ki.txt", "w", encoding="UTF-8") as f: 
        for i in range(sz_db):
            x = random.randint(sz_also, (sz_felso))
            f.write(f"{x};")



def felt2():
    karakter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    b_db = int(input("Mennyi szöveg legyen generálva: "))
    with open("ki.txt", "w", encoding="UTF-8") as f:
            for i in range(b_db):
                for i in range(random.randint(1, 20)):
                    f.write(f"{random.choice(range(len(karakter)))}")
                
                f.write(f";")



def fel3():
     
    sz_also = int(input("Mennyi legyen az alsó határ: ")) 
    sz_felso = int(input("Mennyi legyen a felső határ: ")) 
    sz_db = int(input("Mennyi szám volt generálva: ")) 
    adatok = []
    db = 0


    with open("ki.txt", "r", encoding="UTF-8") as f:
        adatok= f.read().split(';')
        del adatok[-1]

    adatok = [eval(i) for i in adatok]

    for x in adatok:
        db += 1
        if sz_also > x  and x > sz_felso:
              print("A 'ki.txt' nem felel meg a megadott paramétereknek.")
              break
              
             
        if db != sz_db :  
            print("A 'ki.txt' nem felel meg a megadott paramétereknek.")
            break
            
        else:
            print("A 'ki.txt' megfelel a megadott paramétereknek.") 


        
def fel4():
    b_db = int(input("Mennyi szöveg volt generálva: "))
    with open("ki.txt", "r", encoding="UTF-8") as f:
        adatok= f.read().split(';')
        del adatok[-1]
    print(adatok)
    betuk = []
    for x in adatok:

        for i in range(len(x)):
            betuk.append(x[i])


    print(betuk)
    y = 0
    for x in betuk:
        if type(x) == string:
            y = 1
    

    print(y)
    if y == 0:
        print("Nem felel meg a paramétereknek.")
    
    else:
        print("Megfelet.")






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
        print("Nincs ilyen opció.")