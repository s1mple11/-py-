import re
m,n=map(int,input().split())
#矩阵行数m，列数n
arr1=input()
#输入矩阵1
arr2=input()
#输入矩阵2

list1=[]
list2=[]
list=re.compile(r'-?\d+')
list1=list.findall(arr1)
list2=list.findall(arr2)

a=[[0]*n for i in range(m)]
for i in range(m):
  for j in range(n):
   a[i][j]=int(list1[i*n+j])+int(list2[i*n+j])
  
if(m>1):
  print('[',end='')
  for i in range(m):
    print('[',end='')
    for j in range(n):
      print(a[i][j],end='')
      if(j<n-1):
        print(',',end='')
    if(i<m-1):
      print(']',end=',')
    if(i==m-1):
      print(']',end='')
  print(']',end='')

if(m==1):
  print('[',end='')
  for j in range(n):
    print(a[0][j],end='')
    if(j<n-1):
      print(',',end='')
  print(']',end='')