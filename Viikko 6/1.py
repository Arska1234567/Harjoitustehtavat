import random

def heita_noppaa():
    return random.randint(1, 6)

def main():
    tulos = 0
    while tulos != 6:
        tulos = heita_noppaa()
        print(f"Heitit: {tulos}")

if __name__ == "__main__":
    main()