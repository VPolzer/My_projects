import random
import time

def prevod(karta):
  if karta[0] == "A":
    hodnota = 11
  elif karta[0] in "JQK" or (karta[1]) == "0":
    hodnota = 10
  else:
    hodnota = int(karta[0])
  return hodnota

print('Hrajeme "Oko bere". Pokus se získat 21 bodů, ale ani o bod více.')
print()

#print("♥, ♦, ♣, ♠")

balicek = []
cisla = list(range(2, 11))
pismena = list("JQKA")

for barva in "♥", "♦", "♣", "♠":
  for hodnota in cisla + pismena:
    balicek.append(str(hodnota) + " " + barva)
print("Máme tu nový balíček karet. Podívej: ")
print(", ".join(balicek))    

konto = 100


while konto > 0:
  body_hrac = 0
  karty_hrac = []
  body_krupier = 0
  karty_krupier = []
  sazka = -1
  dalsi_hra = "ne"
  i = 0

  print()
  print("Na kontě máš", konto, "mincí.")
  while sazka > konto or sazka <= 0:
    try:
      sazka = int(input("Kolik vsadíš? "))
    except ValueError:
      print("Zadej číslo.")
  
  print()
  print("Zamícháme a rozdáme ...")
  time.sleep(1)
  print()
  random.shuffle(balicek)
  #print(balicek)
    
  print("Tvoje první karta: ",(balicek[i]))
  body_hrac += prevod(balicek[i])
  karty_hrac.append(balicek[i])
  print(body_hrac)
  i +=1
  
  while body_hrac < 21:
    odpoved = input("Chceš další kartu? ")
    if odpoved == "ano" or odpoved == "Ano":
      body_hrac += prevod(balicek[i])
      karty_hrac.append(balicek[i])
      print("Tvoje karty: ",", ".join(karty_hrac))
      print(body_hrac)
      i +=1  
    elif odpoved == "ne":
      break
    else:
      print('Odpověz "ano" nebo "ne"')
  
  if (body_hrac == 21) or (len(karty_hrac) == 2 and body_hrac == 22):
    print("Oko bere")
    konto += sazka
  elif body_hrac > 21:
    print("Prohrál jsi")
    konto -= sazka
    if konto <= 0:
      break
  else:
    print("Uvidíme, co mi padne.")
    time.sleep(1)
    print()
    while body_hrac > body_krupier:
      time.sleep(2)
      body_krupier += prevod(balicek[i])
      karty_krupier.append(balicek[i])
      print("Moje karty: ",", ".join(karty_krupier))
      print(body_krupier)
      i +=1
  
    while body_krupier < 18 and body_hrac == body_krupier:
      time.sleep(2)
      body_krupier += prevod(balicek[i])
      karty_krupier.append(balicek[i])
      print("Moje karty: ",", ".join(karty_krupier))
      print(body_krupier)
      i +=1
      
  if (len(karty_krupier) == 2 and body_krupier == 22):
    print("Prohrál jsi")
    konto -= sazka
    if konto <= 0:
      break
  elif body_krupier > 21:
    print("Vyhrál jsi")
    konto += sazka 
  elif body_hrac == body_krupier:
    print("Remíza")
  elif body_krupier > body_hrac:
    print("Prohrál jsi")
    konto -= sazka
    if konto <= 0:
      break
  while dalsi_hra != "ano":
    dalsi_hra = input("Hrajeme dál? ")
    if dalsi_hra == "ano": 
      print()
    elif dalsi_hra == "ne":
      break
    else:
      print('Odpověz "ano" nebo "ne"')
  if dalsi_hra == "ne":
    break

print()
if konto > 0 and konto < 100:
  print("Prohrál jsi", 100 -konto, "mincí. Na kontě máš", konto, "mincí.")
elif konto == 100:
  print("Šul nul. Na kontě máš", konto, "mincí.")
elif konto > 100:
  print("Gratuluji vyhrál jsi", konto - 100, "mincí. Na kontě máš", konto, "mincí.")
else:
  print("A jsi na nule.")