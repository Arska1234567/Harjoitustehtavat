#Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti. Tehtävässä on käytettävä if/elif/else-toistorakennetta.



luokka=input("Mikä on hyttiluokkasi(LUX,A,B,C)?")
if luokka == "LUX" :
    print("LUX on parvekkeelline hytti yläkannella")
if luokka == "A" :
    print("A on ikkunallinen hytti autookannen yläpuolella.")
if luokka == "B" :
    print("B on ikkunaton hytti autokannen yläpuolella.")
if luokka == "C" :
    print("C on ikkunaton hytti autokannen alapuolella.")
else :
    print("Virheellinen hyttiluokka")