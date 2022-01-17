from selenium import webdriver
import datetime
import time
import csv

print("请输入北邮人论坛用户名")
user_id=input()
print("请输入密码")
user_pw=input()
today=datetime.date.today() #今天
yesterday=today - datetime.timedelta(days=1) #昨天
byr_driver=webdriver.Firefox()
byr_driver.get("https://bbs.byr.cn/index")
user_input=byr_driver.find_element('css selector','input[name="id"]')
user_input.send_keys(user_id)
time.sleep(1)
pw_input=byr_driver.find_element('css selector','input[name="passwd"]')
pw_input.send_keys(user_pw)
time.sleep(1)
login_button=byr_driver.find_element('css selector','input[id="b_login"]')
login_button.submit()
time.sleep(5)
job_title=byr_driver.find_element('css selector','li[id="job"]>div[class="widget-head"]>span[class="widget-title"]')
job_title.click() #界面跳转，进入招聘模块
time.sleep(2)
list0=[]
job_list0=[]
joblist=[] #帖子标题
time_list0=[]
page=1
for a in range(5): #从最多五页帖子中爬取昨天的帖子
    job_list1=[]
    time_list1=[]
    list0=byr_driver.find_elements('css selector','table[class="board-list tiz"]>tbody>tr')
    c=len(list0)
    for i in range(1,c+1):
        job_list0=byr_driver.find_elements('css selector','table[class="board-list tiz"]>tbody>tr>td:nth-child(2)')
        time_list0=byr_driver.find_elements('css selector','table[class="board-list tiz"]>tbody>tr>td:nth-child(3)')
    for n in job_list0:
        job_list1.append(n.text)
    for m in time_list0:
        time_list1.append(m.text)
    for x in range(c):#判断该帖子时间，若时间为昨天，则在job_list列表中加入该标题
        if(time_list1[x]==str(yesterday)):
            joblist.append(job_list1[x])
    #跳转至下一页
    if(a==0):
        page_tag=byr_driver.find_element('css selector','ul[class="pagination"]>li:nth-child(2)>ol[class="page-main"]>li:nth-child(11)')
        page_tag.click()
    else:
        page_tag=byr_driver.find_element('css selector','ul[class="pagination"]>li:nth-child(2)>ol[class="page-main"]>li:nth-child(12)')
        page_tag.click()
    time.sleep(5)

with open('BYR-JOB-YYYY-MM-DD.csv', 'w', newline='') as file:
    csv_w = csv.writer(file)
    for i in range(len(joblist)):
        csv_w.writerow([i+1,joblist[i]])