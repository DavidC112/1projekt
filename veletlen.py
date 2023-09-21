import random
import string

print("Melyik opciót szeretnéd választani:\n1. Számok Generálása\n2. Betűk generálása.\n3. ki.txt ellenőrzése számokkal\n4. ki.txt ellenőrzése betűkkel")







while True:
    valasztas = input("Írd be a választott lehetőség számát: ") 
    if valasztas == "1":
        print("1")        
        break


    elif valasztas == "2":
        print("2")
        break


    elif valasztas == "3":
        print("3")
        break

    elif valasztas == "4":
        print("4")
        break
    
    else:
        print("Nincs ilyen opció.")