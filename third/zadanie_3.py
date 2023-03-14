biletNum = input("Введите номер билета и программа покажет, счастливый ли он - ")
summRight = 0
summLeft = 0
for i in range(int(len(biletNum)/2)):
    summLeft += int(biletNum[i])
    summRight += int(biletNum[(len(biletNum)-1) - i])
if len(biletNum)%2 != 0:
    print(f"Вы ввели некорректное число - {biletNum}.")
elif summLeft == summRight:
    print(f"Поздравляем ваш билет - СЧАСТЛИВЫЙ!!!(сумма правой и левой части - {summLeft})")
else:
    print(f"Сумма левой части билета - {summLeft}, а правой - {summRight}.")
