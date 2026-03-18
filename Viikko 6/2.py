import random

def heita_muokattua_noppaa(tahkot):
    return random.randint(1, tahkot)

def main():
    maksimi = int(input("Kuinka monta tahkoa nopassa on? "))
    tulos = 0
    while tulos != maksimi:
        tulos = heita_muokattua_noppaa(maksimi)
        print(f"Heitit: {tulos}")

if __name__ == "__main__":
    main()