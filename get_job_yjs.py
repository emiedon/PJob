# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time as t
from tqdm import tqdm

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
sleeptime = 2

def url2soup(url):
    t.sleep(sleeptime)
    global headers
    page = requests.get(url,headers=headers)
    page.encoding = 'gbk'
    return BeautifulSoup(page.text, 'lxml')

bsObj=url2soup('http://www.yingjiesheng.com/beijing/ptjob.html')

keyword_list = ['深度学习','机器学习','pytorch','tensorflow','caffe','cnn','rnn','lstm','计算机视觉']

work_list = bsObj.find_all("tr",attrs={'class':'tr_list'})

print("上线岗位个数：", len(work_list))
checkout_word = []

for raw_row in tqdm(work_list):

    a1 = raw_row.find('a')
    a2 = raw_row.find("td",attrs={'class' :'date center'})
    href = a1.get("href")
    name = a1.string
    time = a2.string
    if 'http' not in href:
        href = 'http://www.yingjiesheng.com' + href
        min_bsObj = url2soup(href)
        job_Intro = min_bsObj.find("div",attrs={'class' :'jobIntro'})
    else:
        min_bsObj = url2soup(href)
        job_Intro = min_bsObj.find("div",attrs={'class' :'j_i'})

    job_text = str(job_Intro).lower()
    for middle in keyword_list:
        if middle in job_text:
            checkout_word.append(str(time)+"---"+str(name)+"---"+str(href))
            break

for i in checkout_word:
    print(i)


