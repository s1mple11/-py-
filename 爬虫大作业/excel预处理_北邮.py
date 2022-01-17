import csv
import re
import xlsxwriter as xw

head = ["序号（数字序号）", "招聘主题", "用人单位", "发布日期", "浏览次数","职位个数"]
number_list=[]
title_list=[]
companies_list=[]
date_list=[]
views_list=[]
jobs_number_list=[]
# 用正则表达式分离字段：用人单位，发布日期，浏览次数，职位个数
details_re = re.compile("发布企业：(.*)   日期：(.*)   浏览次数：(.*)")
jobs_number_re = re.compile("\d+")
# 打开原始csv
csv_r=csv.reader(open("./BEIYOU_1.csv"))

for line in csv_r:

    number_list.append(line[0])
    # 添加主题
    title_list.append(line[1])

    details_mo = details_re.search(line[2])
    # 添加用人单位，发布日期，浏览次数
    companies_list.append(details_mo.group(1))
    date_list.append(details_mo.group(2))
    views_list.append(int(details_mo.group(3)))
    # 添加职位个数
    jobs_number_mo = jobs_number_re.search(line[3])
    jobs_number_list.append(int(jobs_number_mo.group()))

#创建表格
workbook=xw.Workbook("BY_D.xlsx")
worksheet1=workbook.add_worksheet("北邮")
worksheet1.activate()
worksheet1.write_row('A1', head)
length=len(number_list)
j=2

for i in range(length):
    # 去除主题两端空格
    title_list[i].strip()
    # 插入数据
    insert_row=[number_list[i],title_list[i],companies_list[i],date_list[i],views_list[i],jobs_number_list[i]]
    row='A'+str(j)
    worksheet1.write_row(row, insert_row)
    j+=1

workbook.close()