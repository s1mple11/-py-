n=int(input())
if n==0:
    print('average = 0.0')
    print('count = 0')
else:
    list=input().split()
    sum=0
    count=0
    for i in range(n):
        f=int(list[i])
        sum+=f
        if f>=60:
            count+=1
    average=sum/n
    print("average = %.1f" % average)
    print("count =", count)