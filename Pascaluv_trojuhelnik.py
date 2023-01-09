print("Ahoj, umím vytvořit Pascalův trojúhelník")
print()

def pascaluv_trojudelnik(pocet_radku):
  radek = [1]
  radek_pomocna = [1]
  
  for i in range(pocet_radku + 1):
    for j in range(len(radek) - 2):
      radek[j + 1] = radek_pomocna[j] + radek_pomocna[j + 1]
    print(" " * 3 * (pocet_radku - i),end="")
    for k in radek:  
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
    print()
    radek.append(1)
    radek_pomocna[1:] = radek[1:]

pocet_radku = int(input("Zadej požadovaný počet řádků: "))

pascaluv_trojudelnik(pocet_radku)