num = str(input("Введите число и программа выдаст сумму всех циффр этого числа - "))
summa = 0
for i in range(len(num)):
    summa += int(num[i])
print(f"Сума цифр числа - {num}, равняется - {summa}")
