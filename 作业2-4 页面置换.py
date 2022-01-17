n, m = map(int,input ().split())
loading = 0
dict = {}
list = list(map(int, input ().split()))
print(list)
for i in range(0, m) : 
    page = list[i]
    flag = False
    for j, k in dict.items():      
        """遍历字典，如已有则设1无则0 """
        if j == page:
            flag = True
    if flag is False:
        loading += 1
        if loading <= n:
            for j,k in dict.items():
                dict[j]+=1
            dict[page] = 0
        else:
            maxnum= -1
            pos= -1
            for j,k in dict. items () :
                if k > maxnum:
                    pos =j
                    maxnum=k
            del dict[pos]
            dict[page] = 0
    else:
        for j, k in dict.items():
            if j == page:
                dict[j] = 0
            else:
                dict[j] += 1
print (loading)
list1=sorted(dict)
len=len(list1)
for i in range(len):
    print (list1[i], end=" ")