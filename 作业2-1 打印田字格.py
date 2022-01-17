n=int(input())
list1=[]
def tianzige(h,l):
     a,b,c,d = "+","-","|"," "
     hang = 2*b + a 
     ch = 2*d + c 
     cs = 2*b + c
     for i in range(h): 
        print(a + hang*2*l) 
        print(c + ch*2*l)        
        print(c + (hang+cs)*l) 
        print(c + ch*2*l)
     print(a + hang*2*l)
for i in range(n):
    list=input().split()
    list1+=list
for j in range(0,n):
    tianzige(int(list1[2*j]),int(list1[2*j+1]))