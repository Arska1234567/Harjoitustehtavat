luvut =[]

while True:
    vastaus=input("Anna luku")
    if vastaus =="":
        break
    luvut.append(float(vastaus))

luvut.sort(reverse=True)
print("Suurimmat 5 lukua ovat:")
for luku in luvut[:5]:
    print(luku)


