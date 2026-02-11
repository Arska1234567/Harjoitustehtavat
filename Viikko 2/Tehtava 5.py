leiviskat= int(input("Anna lieviskät"))
naulat=int(input("Anna naulat"))
luodit=int(input("Anna luodit"))

#1 leiviska = 20 naulaa
#1 naula = 32 luotia
#1 luoti = 13,3 grammaa

kokonaisluodit=(leiviskat*20*32+naulat*32+luodit)
massa_grammoina=kokonaisluodit*13,3

kilot=int (massa_grammoina // 1000)

loputgrammat = massa_grammoina % 1000

print(f"Massa nykymittojen mukaan:")
print(f"{kilot} kilogrammaa ja {loputgrammat} grammmaa")
