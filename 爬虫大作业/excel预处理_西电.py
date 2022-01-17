import csv
import re
import xlsxwriter as xw

head = ["序号（数字序号）", "招聘主题", "用人单位", "发布日期", "浏览次数"]
number_list=[]
title_list=[]
companies_list=[]
date_list=[]
views_list=[]

# 用正则表达式分离字段：发布日期，浏览次数
date_re = re.compile("(\d+)[^0-9](\d+)[^0-9](\d+)(.*)")
views_re = re.compile("\d+")
# 打开原始csv
csv_r=csv.reader(open("./XIDIAN_1.csv"))

for line in csv_r:

    number_list.append(line[0])
    # 添加主题
    title_list.append(line[1])
    # 添加用人单位
    companies_list.append(line[2])

    # 添加发布日期
    date_mo = date_re.search(line[3])
    year = date_mo.group(1)
    month = date_mo.group(2)
    day = date_mo.group(3)
    date = year + '-' + month + '-' + day
    date_list.append(date)

    # 添加浏览次数
    views_mo = views_re.search(line[4])
    views_list.append(int(views_mo.group()))

#创建表格
workbook=xw.Workbook("XD_D.xlsx")
worksheet1=workbook.add_worksheet("西电")
worksheet1.activate()
worksheet1.write_row('A1', head)
length=len(number_list)
j=2

for i in range(length):
    # 去除主题两端空格
    title_list[i].strip()
    # 插入数据
    insert_row=[number_list[i],title_list[i],companies_list[i],date_list[i],views_list[i]]
    row='A'+str(j)
    worksheet1.write_row(row, insert_row)
    j+=1

workbook.close()