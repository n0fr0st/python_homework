import random

def create_tuple(x):
    if len(str(x))==1:
        return (x, 10000)
    return (int(str(x)[0]), int(str(x)[1]))
k=1
n = int(input())
numlist = list()
res_list = list()
res_list1 = list()
for i in range(n):
    numlist.append(random.randrange(1, 100))
for x in numlist:
    res_list.append(create_tuple(x))
res_list.sort(key=lambda a: (a[0],a[1]), reverse=True)

for tuplee in res_list:
    for number in tuplee:
        if number!=10000:
            res_list1.append(str(number))

print(numlist)
print("".join(res_list1))
    

