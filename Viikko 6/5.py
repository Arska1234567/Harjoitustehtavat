def karsi_parittomat(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


def main():
    alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    uusi_lista = karsi_parittomat(alkuperainen)

    print(f"Alkuperäinen lista: {alkuperainen}")
    print(f"Karsittu lista (vain parilliset): {uusi_lista}")


if __name__ == "__main__":
    main()