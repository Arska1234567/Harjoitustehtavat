while True:
    luku = int(input("Anna luku 1-10"))
    if luku == 7:
        break
    elif luku in (1,2,3,4,5,6):
        print("Liian pieni arvaus")
    elif luku in (7,8,9,10,11,12):
        print("Liian suuri arvaus")
print("arvasit oikein")
