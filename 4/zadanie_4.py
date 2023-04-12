k = int(input('Кол-во знаков - '))
s = int(input('Искомая сумма знаков числа - '))

def myfunc(k, s):
    i = 10**(k-1)
    res_num = 0
    while i < 10**(k):
        res = 0
        numstr = str(i)
        list_Res = list(numstr)
        for j in list_Res:
            res += int(j)
        if res == s:
            res_num += 1
        i += 1
    return res_num

print(f"Ответ - {myfunc(k, s)}")


