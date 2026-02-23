vuosi=int(input("Mikä vuosi on nyt?"))
if vuosi %4 == 0:
    print(f"{vuosi} on karkausvuosi")
else:
    print(f"{vuosi} ei ole karkausvuosi")
