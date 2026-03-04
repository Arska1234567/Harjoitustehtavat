

oikeatunnus="python"
oikeasalasana="rules"
yritykset=0
maksimiyritykset = 5

while True:
    tunnus = input("Kirjoita kayttajatunnus")
    salasana = input("Kirjoita salasana")
    if tunnus ==oikeatunnus and salasana==oikeasalasana:
        print("Tervetuloa")
    else:
        yritykset+=1
        print("Paasy evatty")
    if yritykset == maksimiyritykset:
        break