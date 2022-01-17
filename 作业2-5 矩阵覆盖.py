n,m=map(int,input().split())
zeronum=n*m
matrix=[[m+1]*n]
matrix=[[0 for i in range(m+1)] for i in range(n+1)]
Q=int(input())
for it in range(Q):
    x1,y1,x2,y2=map(int,input().split())
    for row in range(x1,x2+1):
        for col in range(y1,y2+1):
            if matrix[row][col]==0:
                zeronum-=1
            matrix[row][col]=1
print(zeronum)