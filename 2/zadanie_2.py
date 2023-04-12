def summ_func(n, m, res):
    if m == 0 & n == 0:
        return res
    elif n == 0:
        return summ_func(n, m-1, res+1)
    else:
        return summ_func(n-1,m, res+1)

n = int(input())
m = int(input())
res = 0
print(summ_func(n, m, res))