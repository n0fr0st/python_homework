summZhur = int(input("Введите общее число журавлей - "))
zhurByBoys = int(summZhur/6)
kateNum = int((zhurByBoys*2)*2)

if kateNum + zhurByBoys*2 != summZhur:
    print(f"Некорректное число, сумма всех сделаных журавлей ребятами, по условию задачи - {kateNum + zhurByBoys*2}, не соответсвует данному числу - {summZhur}")
else :
    print(f"Сережа и Петя сделали по {zhurByBoys}, а Катя - {kateNum} журавлей")
