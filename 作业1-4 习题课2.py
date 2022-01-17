classNum=int(input())
c=input()
list=c.split()
MinC=0
for i in range(len(list)):
    list[i]=int(list[i])
if (classNum%2==0):
    MinC=classNum//2
else:
    MinC=(classNum+1)//2
list.sort()
b=0
for i in range(MinC):
    if (list[i]%2==0):
        list[i]=list[i]//2
    else:
        list[i]=(list[i]+1)//2
    b+=list[i]
print(b)