#program generuje nahodne cislo, uzivatel hada podle pokynu

import random
#print(random.randint(1,10))
cislo=random.randint(1,10)  #nahodne cislo z intervalu
pokus=0

while pokus!=cislo:  #!= v pythonu znamena nerovna se
    pokus=int(input("hadej:"))
    if(pokus<cislo):
        print("vetsi")
    elif(pokus>cislo):
        print("mensi")
    else:
        print("uhodl jsi cislo!")

if (pokus<1 or pokus>10):
    print("hadej cislo 1 az 10")   #pokud uzivatel nehada cislo z zadaneho intervalu, neni nakonec potreba!


# https://youtu.be/B2tviDGFq84?si=aw5Zl2-dKc3WNEqw navod