n = int(input("Введите число - "))
i = 1
while 2**i < n:
    print(f'{2**i}', end=" ")
    i+=1