import math


def laske_yksikkohinta(halkaisija_cm, hinta_euro):
    sade_m = (halkaisija_cm / 100) / 2
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    return hinta_euro / pinta_ala_m2


def main():

    h1 = float(input("Anna 1. pizzan halkaisija (cm): "))
    p1 = float(input("Anna 1. pizzan hinta (€): "))
    h2 = float(input("Anna 2. pizzan halkaisija (cm): "))
    p2 = float(input("Anna 2. pizzan hinta (€): "))

    yksikko1 = laske_yksikkohinta(h1, p1)
    yksikko2 = laske_yksikkohinta(h2, p2)

    print(f"\n1. pizzan yksikköhinta: {yksikko1:.2f} €/m²")
    print(f"2. pizzan yksikköhinta: {yksikko2:.2f} €/m²")

    if yksikko1 < yksikko2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikko2 < yksikko1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Pizzat ovat samanarvoisia.")


if __name__ == "__main__":
    main()