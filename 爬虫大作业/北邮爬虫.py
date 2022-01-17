from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv


# 北邮就业信息网
url='https://job.bupt.edu.cn/frontpage/bupt/html/recruitmentinfoList.html?type=1'
job_bupt_page = webdriver.Chrome()
job_bupt_page.get(url)
time.sleep(6)
url_list=[]
title_list=[]
details_list=[]
numbers_list=[]
# 时间标记
date_flag=1
# 存储所有窗口的id
while(date_flag):
    job_list = job_bupt_page.find_elements(By.XPATH, '//*[@id="listPlace"]/div')
    for each in job_list:
        date = each.find_element(By.XPATH, './div[2]/p/span').text
        url = each.find_element(By.XPATH, './div[2]/a').get_attribute('href')
        if date > '2021-08-31':
            url_list.append(url)
            print(date)
        else:
            date_flag = 0
            break
    # 翻页
    next_page = job_bupt_page.find_element_by_link_text('下一页')
    next_page.click()
    time.sleep(5)

for i in range(len(url_list)):
    # 新窗口打开链接
    job_bupt_page.execute_script(f'window.open("{url_list[i]}", "_blank");')
    # 关闭原窗口
    job_bupt_page.close()
    # 切换到新窗口
    job_bupt_page.switch_to.window(job_bupt_page.window_handles[-1])
    time.sleep(4)
    # 抓取数据
    # 招聘主题
    title = job_bupt_page.find_element(By.XPATH, '//*[@id="positionPlace"]/div[2]/div[1]/div[1]').text
    print(title)
    title_list.append(title)

    # 细节：用人单位，发布日期，浏览次数
    details = job_bupt_page.find_element(By.XPATH, '//*[@class="midInfo"]/div').text
    print(details)
    details_list.append(details)

    # 职位数量
    try:
        numbers=job_bupt_page.find_element(By.XPATH, '//*[@id="positionPlace"]/div[2]/div[1]/div[2]/span[1]').text
        print(numbers)
        numbers_list.append(numbers)
    except:
        numbers=1
        print('None')
        numbers_list.append(numbers)

    # 切换回原窗口
    job_bupt_page.switch_to.window(job_bupt_page.window_handles[0])

    # 写入csv文件
    with open('BEIYOU_1.csv', 'a', newline='') as file:
        csv_a = csv.writer(file)
        csv_a.writerow([i + 1, title, details, numbers])

job_bupt_page.close()