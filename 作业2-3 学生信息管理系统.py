student_list = {}
output=[]
class Student:
    def __init__(self,id,name,maths,english,python):
        #初始化学生的学号，姓名，数学成绩，英语成绩，python成绩
        self.id=id
        self.name=name
        self.maths=maths
        self.english=english
        self.python=python
        self.sum=maths+english+python

def add(id,name,maths,english,python):
        #print("add")
        #添加学生信息
        if id in student_list:
            print("Students already exist")
            
        else:
            student_list[id] = Student(id,name,maths,english,python)
            print("Add success")
            
def delete(id):
        #print("delete")
        #删除学生信息
        if id in student_list:
            del student_list[id]
            print("Delete success")
            
        else:
            print("Students do not exist")
            
def editscore(id,maths,english,python):
        #print("delete")
        #更改学生成绩信息
        if id in student_list:
            student_list[id].maths=maths
            student_list[id].english=english
            student_list[id].python=python
            student_list[id].sum=maths+english+python
            print("Update success")
            
        else:
            print("Students do not exist")
            
def printscore(id):
        #print("printscore")
        #显示学生平均分成绩
        if id in student_list:
            print("Student ID:",student_list[id].id,sep='')
            print("Name:",student_list[id].name,sep='')
            average=student_list[id].sum/3
            
            print("Average Score:%.1f" % average)
        else:
            print("Students do not exist")
            

n=input()
n=int(n)
#输入n行，执行n次循环
arr = [[0]*6 for i in range(130)]        
for i in range(n):
    arr[i]= list(input ().split())
for i in range(n):
    if arr[i][0]=='1':
        arr[i][3]=int(arr[i][3])
        arr[i][4]=int(arr[i][4])   
        arr[i][5]=int(arr[i][5])
        add(arr[i][1],arr[i][2],arr[i][3],arr[i][4],arr[i][5])

    if arr[i][0]=='2':
        #删除
        delete(arr[i][1])
    
    if arr[i][0]=='3':
        #编辑
        arr[i][2]=int(arr[i][2])
        arr[i][3]=int(arr[i][3])
        arr[i][4]=int(arr[i][4])
        editscore(arr[i][1],arr[i][2],arr[i][3],arr[i][4])
        
    if arr[i][0]=='4':
        #打印
        printscore(arr[i][1])