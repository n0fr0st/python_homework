import random
coin = ["решка", "орел"]
reshka = 0
orel = 0
n = int(input('Введите число монет - '))
coinlist = list()
for i in range(n):
    coinlist.append(random.choice(coin))
    print(coinlist[i])
    if coinlist[i] == "решка":
        reshka +=1
    else:
        orel +=1
if reshka >= orel:
    print(f"нужно перевернуть - {orel} монеток")
else:
    print(f"нужно перевернуть - {reshka} монеток")