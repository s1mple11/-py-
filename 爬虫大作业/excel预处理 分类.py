import csv
import re
import xlsxwriter as xw

# 雇主类型分类
it_re = re.compile("互联网|搜索|数据|信息|算法|AI|智能|网络|开发|研发|软件|前端|后端|JAVA|运维|系统|测试|java")
ct_re = re.compile("射频|嵌入|FPGA|信号|IC|硬件|数字|芯片|通信")
fin_re = re.compile("贸|管理|证券|金融|基金|银行")
edu_re = re.compile("教师")
sci_re = re.compile("学院|研究|科研|信号|IC|硬件开发")

# 雇主类型分类函数
def get_type(a: str):
    if it_re.search(a):
        return '互联网'
    elif ct_re.search(a):
        return '通信'
    elif fin_re.search(a):
        return '金融'
    elif edu_re.search(a):
        return '教育'
    elif sci_re.search(a):
        return '科研'
    else:
        return '其他'


head = ["序号（数字序号）", "招聘主题", "雇主类型"]
number_list=[]
title_list=[]
employ_type_list=[]

# 读取北邮
csv_r=csv.reader(open("./BEIYOU_1.csv"))
for line in csv_r:
    # 添加主题
    title_list.append(line[1])

# 读取西电
csv_r=csv.reader(open("./XIDIAN_1.csv"))
for line in csv_r:
    # 添加主题
    title_list.append(line[1])

# 读取成电
csv_r=csv.reader(open("./CHENGDIAN_1.csv"))
for line in csv_r:
    # 添加主题
    title_list.append(line[1])

#创建表格
workbook=xw.Workbook("CAT_A.xlsx")
worksheet1=workbook.add_worksheet("分类")
worksheet1.activate()
worksheet1.write_row('A1', head)

#去除主题两端空格
length=len(title_list)
for i in range(length):
    title_list[i].strip()

#主题去重
title_list=list(set(title_list))
length=len(title_list)
j=2

for i in range(length):
    # 插入数据
    insert_row=[str(i+1),title_list[i],get_type(title_list[i])]
    row='A'+str(j)
    worksheet1.write_row(row, insert_row)
    j+=1

workbook.close()