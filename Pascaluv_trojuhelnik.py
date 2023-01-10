print("Ahoj, umím vytvořit Pascalův trojúhelník.")
print()

def pascaluv_trojudelnik(pocet_radku):
  radek = [1] #typ seznam, který budeme postupně naplňovat a tisknout
  radek_pomocna = [1] #pro výpočet prvků na řádku nemůžeme daný řádek měnit, proto máme pomocnou, která se mění až po výpočtu celého řádku
  n = 6 #chceme, aby všecjna čísla měla n číslic (viz print(f'{k:{pad}{n}}',end=""))
  pad = " " # vycpávka, kterou doplníme počet číslic na n
  
  for i in range(pocet_radku): #vytvoří požadovaný počet řádků
    for j in range(len(radek) - 2): # projde čísla na daném řádku (první a poslední je vždy "1" proto "-2" a taky aby fungovaly první dva řádky pyramidy)
      radek[j + 1] = radek_pomocna[j] + radek_pomocna[j + 1] # číslo v redek na pozici j+1 nahradí součtem j + (j+1) z radek_pomocna
    print(" " * int(n/2) * (pocet_radku - i), end="") # odsazení, aby vznikla pyramida
    for k in radek:  #odsazení, aby byla čísla zarovnána pod sebou, postumně vytiskne všechyn prvky proměnné radek
      print(f'{k:{pad}{n}}',end="") #každé číslo bude mít 6 znaků
    print() #na konci řádku přeskočí na další řádek
    radek.append(1) #do proměnné radek přidá 1 na konec
    radek_pomocna[1:] = radek[1:] # od prvního prvku dál přepíše v radek_pomocna prvky z radek (když se dá radek_pomocna = radek, tak se tyto proměnné propojí a mění se prvky v obou najednou)

pocet_radku = int(input("Zadej požadovaný počet řádků: "))

pascaluv_trojudelnik(pocet_radku)
