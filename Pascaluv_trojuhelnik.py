print("Ahoj, umím vytvořit Pascalův trojúhelník")
print()

def pascaluv_trojudelnik(pocet_radku):
  radek = [1] #typ seznam, který budeme postupně naplňovat a tisknout
  radek_pomocna = [1] #pro výpočet prvků na řádku nemůžeme daný řádek měnit, proto máme pomocnou, která se mění až po výpočtu celého řádku
  
  for i in range(pocet_radku + 1): #vytvoří požadovaný počet řádků
    for j in range(len(radek) - 2): # projde čísla na daném řádku (první a poslední je vždy "1" proto "-2" a taky aby fungovaly první dva řádky pyramidy)
      radek[j + 1] = radek_pomocna[j] + radek_pomocna[j + 1] # číslo v redek na pozici j+1 nahradí součtem j + (j+1) z radek_pomocna
    print(" " * 3 * (pocet_radku - i),end="") # odsazení, aby vznikla pyramida
    for k in radek:  #odsazení, aby byla čísla zarovnána pod sebou, postumně vytiskne všechyn prvky proměnné radek
      if k < 10:
        print(k,"    ", end="")
      elif k < 100:
        print(k, end="    ")
      elif k < 1000:
        print(k, end="   ")
      elif k < 10000:
        print(k, end="  ")
      elif k < 100000:
        print(k, end=" ")
      else:
        print(k, end="")
    print() #na konci řádku přeskočí na další řádek
    radek.append(1) #do proměnné radek přidá 1 na konec
    radek_pomocna[1:] = radek[1:] # od prvního prvku dál přepíše v radek_pomocna prvky z radek (když se dá radek_pomocna = radek, tak se tyto proměnné propojí a mění se prvky v obou najednou)

pocet_radku = int(input("Zadej požadovaný počet řádků: "))

pascaluv_trojudelnik(pocet_radku)
