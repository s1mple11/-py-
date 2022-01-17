n=int(input())
list=[]
if(n==2):
    print(2)
else:
    for i in range(2,n+1):
        if(i==2):
            list.append(i)
            continue
        for j in range(2,i+1):
            if (i==j):
                list.append(i)
            if (i%j==0):
                break
    length=len(list)
    for i in range(length-1):
        print(list[i], end=' ')
    print(list[i+1],end='')