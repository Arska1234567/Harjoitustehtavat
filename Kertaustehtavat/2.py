tuntipalkka = float(input("Kerro tuntipalkkasi"))
tunnit = float(input("Monta tuntia olet tehnyt"))
päivä = input("Mikä viikonpäivä nyt on?")
päiväpalkka = tunnit * tuntipalkka
if päivä == "sunnuntai":
    päiväpalkka = tunnit*tuntipalkka*2
print(f"Päiväpalkkasin on {päiväpalkka}")
