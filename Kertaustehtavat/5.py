while True:
    print("Valitse laskutoimitus:")
    print("1: Yhteenlasku ")
    print("2: Vähennyslasku")
    print("3: Kertolasku")
    print("4: Jakolasku")
    print("0: Lopeta ohjelma")

    valinta = int(input("Mika on valintasi?"))
    if valinta == 0:
        break
    if valinta in(1,2,3,4):
        luku1= float(input("Anna eka luku"))
        luku2= float(input("Anna toka luku"))
        if valinta == 1:
            tulos = luku1 + luku2
            print(f"Tulos: {luku1} + {luku2} = {tulos}")

        elif valinta == 2:
            tulos = luku1 - luku2
            print(f"Tulos: {luku1} - {luku2} = {tulos}")

        elif valinta == 3:
            tulos = luku1 * luku2
            print(f"Tulos: {luku1} * {luku2} = {tulos}")

        elif valinta == 4:

            if luku2 != 0:
                tulos = luku1 / luku2
                print(f"Tulos: {luku1} / {luku2} = {tulos}")







