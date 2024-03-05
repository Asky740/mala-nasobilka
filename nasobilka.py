import random

def nasobeni(x,y):
    vysledek = x * y
    return vysledek

def vyhodnoceni(vysledek, porovnani):
    if vysledek == porovnani:
        print("hezky")
        odpoved = True
    else:
        print("no nevim")
    return odpoved

for z in range(10):
    x = random.randint(0,10)
    y = random.randint(0,10)

    porovnani = input(f"{x} * {y} = ")



else:
  print("konec")