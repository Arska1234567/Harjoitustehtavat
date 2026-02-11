sukupuoli=input("Mikä on sukupuolesi?")
hemo=int(input("Mikä on hemoglobiiniarvosi(g/l)?"))

if sukupuoli == "nainen":
    if hemo < 117:
        print("Hemoglobiinisi on alhainen")
    if hemo > 175:
        print("Hemoglobiinisi on korkea")
    else:
        print("Hemoglobiinisi on normaali")
if sukupuoli == "mies":
    if hemo < 134:
         print("Hemoglobiinisi on alhainen")
    if hemo > 195:
        print("Hemoglobiinisi on korkea")
    else:
        print("Hemoglobiinisi on normaali")
