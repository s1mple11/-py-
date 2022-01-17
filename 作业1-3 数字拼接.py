a,b=map(int,input().split())
a,b=str(a),str(b)
lenA,lenB=len(a),len(b)
c=str()
if(lenA>=lenB):
    for i in range(lenB):
        c+=a[i]+b[i]
    for i in range(lenB,lenA):
        c+=a[i]
else:
    for i in range(lenA):
        c+=a[i]+b[i]
    for i in range(lenA,lenB):
        c+=b[i]
print(c)