import xlrd
import re

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

# 列表取整
def int_list(a:list):
    return [round(x) for x in a]

# 读取北邮数据
BY_D=xlrd.open_workbook("BY_D.xlsx")
BY_d=BY_D.sheet_by_index(0)
by_title_list=BY_d.col_values(1)[1:]
by_views_list=int_list(BY_d.col_values(4)[1:])
by_jobs_number_list=int_list(BY_d.col_values(5)[1:])

# 读取西电数据
XD_D=xlrd.open_workbook("XD_D.xlsx")
XD_d=XD_D.sheet_by_index(0)
xd_title_list=XD_d.col_values(1)[1:]
xd_views_list=int_list(XD_d.col_values(4)[1:])

# 读取成电数据
CD_D=xlrd.open_workbook("CD_D.xlsx")
CD_d=CD_D.sheet_by_index(0)
cd_title_list=CD_d.col_values(1)[1:]
cd_views_list=int_list(CD_d.col_values(4)[1:])

print("\n")
# A部分
print("A部分：","\n")
# 最受北邮学生关注的招聘TOP20
print("最受北邮学生关注的招聘TOP20(浏览次数)：")
by_jobs_top20_list=[]
# 拷贝
by_title_list1=by_title_list.copy()
by_views_list1=by_views_list.copy()
for i in range(20):

    views_max = max(by_views_list1)
    max_index=by_views_list1.index(views_max)
    by_jobs_top20_list.append([i+1,by_title_list1[max_index], views_max])
    print(i+1, by_title_list1[max_index], views_max,'次')
    del by_title_list1[max_index], by_views_list1[max_index]

# 最受西电学生关注的招聘TOP20
print("\n")
print("最受西电学生关注的招聘TOP20(浏览次数)：")
xd_jobs_top20_list=[]
# 拷贝
xd_title_list1=xd_title_list.copy()
xd_views_list1=xd_views_list.copy()
for i in range(20):

    views_max = max(xd_views_list1)
    max_index=xd_views_list1.index(views_max)
    xd_jobs_top20_list.append([i+1,xd_title_list1[max_index], views_max])
    print(i+1,xd_title_list1[max_index], views_max,'次')
    del xd_title_list1[max_index], xd_views_list1[max_index]

# 最受成电学生关注的招聘TOP20
print("\n")
print("最受成电学生关注的招聘TOP20(浏览次数)：")
cd_jobs_top20_list=[]
# 拷贝
cd_title_list1=cd_title_list.copy()
cd_views_list1=cd_views_list.copy()
for i in range(20):

    views_max = max(cd_views_list1)
    max_index=cd_views_list1.index(views_max)
    cd_jobs_top20_list.append([i+1,cd_title_list1[max_index], views_max])
    print(i+1,cd_title_list1[max_index], views_max,'次')
    del cd_title_list1[max_index], cd_views_list1[max_index]

# B部分
print("\n")
print("B部分：")
# 最受北邮学生关注的雇主类型TOP10
print("\n")
print("最受北邮学生关注的雇主类型TOP10(浏览次数):")
by_employ_type_views_top10=[]
by_it_views=0
by_ct_views=0
by_fin_views=0
by_edu_views=0
by_sci_views=0
by_others_views=0
by_len=len(by_title_list)

for i in range(by_len):
    job_type=get_type(by_title_list[i])
    if job_type== "互联网":
        by_it_views+= by_views_list[i]
    if job_type== "通信":
        by_ct_views+= by_views_list[i]
    if job_type== "金融":
        by_fin_views+= by_views_list[i]
    if job_type== "教育":
        by_edu_views+= by_views_list[i]
    if job_type== "科研":
        by_sci_views+= by_views_list[i]
    if job_type== "其他":
        by_others_views += by_views_list[i]

by_employ_type_views_list=[by_it_views,by_ct_views,by_fin_views,by_edu_views,by_sci_views,by_others_views]
employ_type_name_list=['互联网','通信','金融','教育','科研','其他']
by_employ_type_name_list=employ_type_name_list.copy()
by_employ_type_views_top10=sorted(by_employ_type_views_list)

for i in range(6):
    type_views_max = max(by_employ_type_views_list)
    max_index=by_employ_type_views_list.index(type_views_max)
    by_jobs_top20_list.append([i+1,by_employ_type_name_list[max_index], type_views_max])
    print(i+1,by_employ_type_name_list[max_index], type_views_max,'次')
    del by_employ_type_views_list[max_index], by_employ_type_name_list[max_index]

# 最受西电学生关注的雇主类型TOP10
print("\n")
print("最受西电学生关注的雇主类型TOP10(浏览次数):")
xd_employ_type_top10=[]
xd_it_views=0
xd_ct_views=0
xd_fin_views=0
xd_edu_views=0
xd_sci_views=0
xd_others_views=0
xd_len=len(xd_title_list)

for i in range(xd_len):
    job_type=get_type(xd_title_list[i])
    if job_type== "互联网":
        xd_it_views+= xd_views_list[i]
    if job_type== "通信":
        xd_ct_views+= xd_views_list[i]
    if job_type== "金融":
        xd_fin_views+= xd_views_list[i]
    if job_type== "教育":
        xd_edu_views+= xd_views_list[i]
    if job_type== "科研":
        xd_sci_views+= xd_views_list[i]
    if job_type== "其他":
        xd_others_views += xd_views_list[i]

xd_employ_type_views_list=[xd_it_views,xd_ct_views,xd_fin_views,xd_edu_views,xd_sci_views,xd_others_views]
employ_type_name_list=['互联网','通信','金融','教育','科研','其他']
xd_employ_type_name_list=employ_type_name_list.copy()
xd_employ_type_top10=sorted(xd_employ_type_views_list)

for i in range(6):
    type_views_max = max(xd_employ_type_views_list)
    max_index=xd_employ_type_views_list.index(type_views_max)
    xd_jobs_top20_list.append([i+1,xd_employ_type_name_list[max_index], type_views_max])
    print(i+1,xd_employ_type_name_list[max_index], type_views_max,'次')
    del xd_employ_type_views_list[max_index], xd_employ_type_name_list[max_index]

# 最受成电学生关注的雇主类型TOP10
print("\n")
print("最受成电学生关注的雇主类型TOP10(浏览次数):")
cd_employ_type_top10=[]
cd_it_views=0
cd_ct_views=0
cd_fin_views=0
cd_edu_views=0
cd_sci_views=0
cd_others_views=0
cd_len=len(cd_title_list)

for i in range(cd_len):
    job_type=get_type(cd_title_list[i])
    if job_type== "互联网":
        cd_it_views+= cd_views_list[i]
    if job_type== "通信":
        cd_ct_views+=cd_views_list[i]
    if job_type== "金融":
        cd_fin_views+= cd_views_list[i]
    if job_type== "教育":
        cd_edu_views+= cd_views_list[i]
    if job_type== "科研":
        cd_sci_views+= cd_views_list[i]
    if job_type== "其他":
        cd_others_views += cd_views_list[i]

cd_employ_type_views_list=[cd_it_views,cd_ct_views,cd_fin_views,cd_edu_views,cd_sci_views,cd_others_views]
employ_type_name_list=['互联网','通信','金融','教育','科研','其他']
cd_employ_type_name_list=employ_type_name_list.copy()
cd_employ_type_top10=sorted(cd_employ_type_views_list)

for i in range(6):
    type_views_max = max(cd_employ_type_views_list)
    max_index=cd_employ_type_views_list.index(type_views_max)
    cd_jobs_top20_list.append([i+1,cd_employ_type_name_list[max_index], type_views_max])
    print(i+1,cd_employ_type_name_list[max_index], type_views_max,'次')
    del cd_employ_type_views_list[max_index], cd_employ_type_name_list[max_index]


# C部分
print("\n")
print("C部分：")

# 北邮招聘职位数量TOP10
print("\n")
print("北邮招聘职位数量TOP10：")
by_jobs_number_top10_list=[]
# 拷贝
by_title_list2=by_title_list.copy()
by_jobs_number_list1=by_jobs_number_list.copy()

for i in range(10):
    jobs_number_max = max(by_jobs_number_list1)
    max_index = by_jobs_number_list1.index(jobs_number_max)
    by_jobs_number_top10_list.append([i + 1, by_title_list2[max_index], jobs_number_max])
    print(i + 1, by_title_list2[max_index], jobs_number_max,"个职位")
    del by_title_list2[max_index], by_jobs_number_list1[max_index]

# 北邮招聘职位总数，北邮招聘职位所属雇主类型TOP10

by_employ_type_job_numbers_stop10=[]
by_it_job_numbers=0
by_ct_job_numbers=0
by_fin_job_numbers=0
by_edu_job_numbers=0
by_sci_job_numbers=0
by_others_job_numbers=0
by_total_job_numbers=0

for i in range(by_len):
    by_total_job_numbers+=by_jobs_number_list[i]
    job_type=get_type(by_title_list[i])
    if job_type== "互联网":
        by_it_job_numbers+= by_jobs_number_list[i]
    if job_type== "通信":
        by_ct_job_numbers+= by_jobs_number_list[i]
    if job_type== "金融":
        by_fin_job_numbers+= by_jobs_number_list[i]
    if job_type== "教育":
        by_edu_job_numbers+= by_jobs_number_list[i]
    if job_type== "科研":
        by_sci_job_numbers+= by_jobs_number_list[i]
    if job_type== "其他":
        by_others_job_numbers += by_jobs_number_list[i]

print("\n")
print("北邮招聘职位总数:",by_total_job_numbers,'个')

by_employ_type_job_numbers_list=[by_it_job_numbers,by_ct_job_numbers,by_fin_job_numbers,by_edu_job_numbers,
                                 by_sci_job_numbers,by_others_job_numbers]
by_employ_type_name_list1=employ_type_name_list.copy()
by_employ_type_job_numbers_stop10=sorted(by_employ_type_views_list)

print("\n")
print("北邮招聘职位所属雇主类型TOP10:")
for i in range(6):
    type_job_numbers_max = max(by_employ_type_job_numbers_list)
    max_index=by_employ_type_job_numbers_list.index(type_job_numbers_max)
    by_jobs_top20_list.append([i+1,by_employ_type_name_list1[max_index], type_job_numbers_max])
    print(i+1,by_employ_type_name_list1[max_index], type_job_numbers_max,'个职位')
    del by_employ_type_job_numbers_list[max_index], by_employ_type_name_list1[max_index]

# D部分
print("\n")
print("D部分")
# 三个高校中最受关注的ICT行业招聘主题TOP10
print("\n")
print("三个高校中最受关注的ICT行业招聘主题(浏览次数)TOP10：")
ict_title_list=[]
ict_views_list=[]

for i in range(len(by_title_list)):
    job_type=get_type(by_title_list[i])
    if job_type == "互联网" or job_type == "通信":
        ict_title_list.append(by_title_list[i])
        ict_views_list.append(by_views_list[i])

for i in range(len(xd_title_list)):
    job_type=get_type(xd_title_list[i])
    if job_type == "互联网" or job_type == "通信":
        ict_title_list.append(xd_title_list[i])
        ict_views_list.append(xd_views_list[i])

for i in range(len(cd_title_list)):
    job_type=get_type(cd_title_list[i])
    if job_type == "互联网" or job_type == "通信":
        ict_title_list.append(cd_title_list[i])
        ict_views_list.append(cd_views_list[i])


ict_jobs_top10_list=[]
# 拷贝
ict_title_list1=ict_title_list.copy()
ict_views_list1=ict_views_list.copy()
for i in range(10):
    views_max = max(ict_views_list1)
    max_index=ict_views_list1.index(views_max)
    ict_jobs_top10_list.append([i+1,ict_title_list1[max_index], views_max])
    print(i+1, ict_title_list1[max_index], views_max,'次')
    del ict_title_list1[max_index], ict_views_list1[max_index]