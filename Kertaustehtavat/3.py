from math import sqrt

while True:
     luku = int(input("Anna numero"))
     if luku == 0:
         break
     if luku < 0:
        print("Virheellinen luku")
     else:
         print( sqrt(luku))
