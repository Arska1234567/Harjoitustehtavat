import random
arpakuutiot= int(input("Kerro arpakuutioiden lukumäärä"))
summa=0
for i in range(arpakuutiot):
    luku=random.randint(1,6)
    summa+=luku
print(f"Silmälukujen summa on {summa}")





