luvut = []

while True:
    syote= input("Kirjoita luku")
    if syote == "":
        break
    luku = float(syote)
    luvut.append(luku)
    if luvut:
        print(f"Pienin luku: {min(luvut)}")
        print(f"Suurin luku: {max(luvut)}")
