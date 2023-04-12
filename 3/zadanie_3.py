def search_premax():
    search_list = []
    flag = True
    while flag == True:
        x = int(input())
        if x == 0:
            flag = False
        search_list.append(x)
    tuple_list = tuple(search_list)
    print(search_list)
    maxof = tuple_list[0]
    for i in tuple_list:
        if i > maxof:
            mid = maxof
            maxof = i
    print(mid)
        


search_premax()
    
    

