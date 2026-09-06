# Tehtävä 1 opintolaskuri
# Nimi: Artturi Kinnunen
# Opiskelijanumero:2524517

# alusta tarvittavat muuttujat, kuten esim. opintopisteiden summa
kurssitulostus = ""
kurssien_määrä = 0
pisteiden_summa = 0
yhteensä_arvosanat=0
# ... ja mahdolliset muut alustukset

# tulosta alkutervehdys

# toistorakenne, josta poistutaan break-lauseella ja joka aloitetaan
# tarvittaessa uudestaan continue-lauseella
while True:
    pass
    print("Anna kurssin nimi (lopeta lopettaa)")
    nimi=input("Kurssin nimi")
    if nimi=="lopeta":
        break

    opintopisteet=int(input("Kurssin opintopistemäärä"))
    if opintopisteet < 0 or opintopisteet >20:
        continue
    Arvosana=int(input("Kurssin Arvosana"))
    if Arvosana < 0 or Arvosana > 6:
        continue

    pisteiden_summa += opintopisteet
    kurssitulostus += nimi
    kurssien_määrä += 1
    yhteensä_arvosanat+=Arvosana

    kurssitulostus +=f"{kurssien_määrä}. {nimi}({opintopisteet}op): {Arvosana}\n"



# pass ei tee mitään, mutta tekee ohjelmasta laillisen Python-ohjelman
# lue käyttäjän syöttämä kurssin nimi ja käytä if-lausetta, jotta voit päätellä, halutaanko ohjelman suoritus lopettaa
# lue käyttäjän syöttämät opintopisteet ja arvosana (muista tarkistaa syötteen laillisuus)
# tarkista if-lauseella, että käyttäjän syötteet ovat sallituissa rajoissa

# vihje: toistorakenteen suorituksen voi aloittaa alusta continue-lauseella
# päivitä muuttujat, joihin keräät opintopisteiden summan ja muut tarvittavat tiedot
# kurssitulostuksen sisällön voit muodostaa merkkijonoon käyttämällä f-merkkijonoja ja + -operaatiota.
# \n -merkki tuottaa rivinvaihdon tulostaessa merkkijonon

# laske halutut tunnusluvut, ota huomioon myös tapaus jossa käyttäjä ei ole syöttänyt mitään

# tulosta tunnusluvut, f-merkkijonon voi muotoilla siten, että tulostetaan vain haluttu määrä desimaaleja

print("Opintopisteet yhteensä", pisteiden_summa)
# lisää tulostusta



if kurssien_määrä > 0:
    keskiarvo = yhteensä_arvosanat/kurssien_määrä
    print("Suoritetut kurssit:")
    print(kurssitulostus,end="")
    print(f"Arvosanojen keskiarvo: {keskiarvo:.1f}")