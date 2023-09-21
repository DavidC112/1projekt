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
    b_db = int(input("Mennyi betűt generáljon: "))
    with open("ki.txt", "w", encoding="UTF-8") as f:
            for i in range(b_db):
                for i in range(random.randint(1, 20)):
                    y = random.choice(string.ascii_letters)
                    f.write(f"{y}")
                
                f.write(f";")





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
        break

    elif valasztas == "4":
        print("4")
        break
    
    else:
        print("Nincs ilyen opció.")