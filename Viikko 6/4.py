def laske_summa(lukulista):
    return sum(lukulista)

def main():
    numerot = [5, 10, 15, 20, 25]
    tulos = laske_summa(numerot)
    print(f"Listan {numerot} summa on: {tulos}")

if __name__ == "__main__":
    main()