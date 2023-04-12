def div_func(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n*div_func(n, m-1) 

n = int(input("Введите число - "))
m = int(input("Введите степень - "))
print(div_func(n,m))

