import random

body = 0
body = int(body)

def nasobeni(x,y):
    vysledek = x * y
    return vysledek

def vyhodnoceni(vysledek, porovnani):

    global body #kdyz je ve funkci, musi byt global
    if vysledek == porovnani:
        print("hezky")
        body +=1
    else:
        print("no nevim")

for z in range(10):
    x = random.randint(0,10)
    y = random.randint(0,10)
    vysledek = int(nasobeni(x ,y))

    porovnani = input(f"{x} * {y} = ")
    porovnani = int(porovnani)

    vyhodnoceni(vysledek, porovnani)

else:
  print("Vaše body:", body)