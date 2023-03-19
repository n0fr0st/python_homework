summa = int(input())
diva = int(input())
for x in range(summa):
    for y in range(diva):
        if x + y == summa and x * y == diva:
            numx = x
            numy = y
print(f"ответ - числа {numy} и {numx}")
            

