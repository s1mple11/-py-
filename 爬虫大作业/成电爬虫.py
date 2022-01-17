from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

# 电子科技大学研究生就业网
url='https://yjsjob.uestc.edu.cn/coread/more-eminfo.jsp'
job_chengdian_page = webdriver.Chrome()
job_chengdian_page.get(url)
time.sleep(6)
title_list=[]
date_list=[]
views_list=[]

# 时间标记
date_flag=1
# 当时间晚于2021年8月31日时
while(date_flag):
    job_list = job_chengdian_page.find_elements(By.XPATH, '//*[@id="view-target"]/li')
    for each in job_list:
        # 抓取时间
        date = each.find_element(By.XPATH, './div[2]/ul/li[2]').text
        # 判断日期
        if date > '发布时间:2021年08月31日':
            date_list.append(date)
        else:
            date_flag = 0
            break

        # 抓取主题
        title = each.find_element(By.XPATH, './div[2]/h6/a').text
        title_list.append(title)
        # 抓取浏览次数
        views = each.find_element(By.XPATH, './div[2]/ul/li[1]').text
        views_list.append(views)

        print(title)
        print(date)
        print(views)
    # 翻页
    next_page = job_chengdian_page.find_element_by_link_text('下一页')
    next_page.click()
    time.sleep(5)

# 写入csv文件

for i in range(len(title_list)):
    with open('CHENGDIAN_1.csv', 'a', newline='', errors='ignore') as file:
        csv_a = csv.writer(file)
        csv_a.writerow([i + 1, title_list[i], date_list[i], views_list[i]])