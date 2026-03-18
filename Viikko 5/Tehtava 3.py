luku=int(input("Kirjoita kokonaisluku"))
alkuluku= True
if luku <=1:
    alkuluku=False
else:
    for i in range(2,luku):
        if luku % i ==0:
            alkuluku= False
            break
if alkuluku:
    print(f" {luku}on alkuluku")




