from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


# 西电就业信息网
url='https://job.xidian.edu.cn/job/search?domain=xidian&d_category%5B0%5D=0&d_category%5B1%5D=100&d_category%5B2%5D=101&d_category%5B3%5D=102'
job_xidian_page = webdriver.Chrome()
job_xidian_page.get(url)
time.sleep(10)
url_list=[]
title_list=[]
companies_list=[]
date_list=[]
views_list=[]

# 时间标记
date_flag=1
# 存储所有窗口的id
while(date_flag):
    job_list = job_xidian_page.find_elements(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div[2]/div/div/div[2]/ul/li')
    for each in job_list:
        date = each.find_element(By.XPATH, './div[2]/div/div[2]/span').text
        url = each.find_element(By.XPATH, './div[2]/div/div[2]/a').get_attribute('href')
        # 当时间晚于2021年8月31日时
        if date > '2021-09-01发布':
            url_list.append(url)
            date_list.append(date)
            print(date)
        else:
            date_flag = 0
            break
    # 翻页
    try:
        next_page = job_xidian_page.find_element_by_link_text('下一页')
        next_page.click()
        time.sleep(8)
    except:
        break

for i in range(len(url_list)):
    # 新窗口打开链接
    job_xidian_page.execute_script(f'window.open("{url_list[i]}", "_blank");')
    # 关闭原窗口
    job_xidian_page.close()
    # 切换到新窗口
    job_xidian_page.switch_to.window(job_xidian_page.window_handles[-1])
    time.sleep(4)
    # 抓取数据
    # 招聘主题
    title = job_xidian_page.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[1]/h5/span').text
    title_list.append(title)

    # 用人单位
    company = job_xidian_page.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[2]/div/div[4]/div/div[1]/a').text
    companies_list.append(company)

    # 浏览次数
    try:
        views = job_xidian_page.find_element(By.XPATH,
                                         '/html/body/div[1]/div[3]/div[2]/div/div[1]/div/div[2]/div/ul/li[1]').text
        views_list.append(views)
    except:
        views= 0
        views_list.append(views)

    print(title)
    print(company)
    print(views)
    # 切换回原窗口
    job_xidian_page.switch_to.window(job_xidian_page.window_handles[0])
job_xidian_page.close()
# 写入csv文件

for i in range(len(title_list)):
    with open('XIDIAN_1.csv', 'a', newline='', errors='ignore') as file:
        csv_a = csv.writer(file)
        csv_a.writerow([i + 1, title_list[i], companies_list[i], date_list[i], views_list[i]])