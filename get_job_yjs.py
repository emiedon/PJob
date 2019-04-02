# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

def url2soup(url):
    page = requests.get(url)
    page.encoding = 'gbk'
    return BeautifulSoup(page.text, 'lxml')

bsObj=url2soup('http://www.yingjiesheng.com/beijing/ptjob.html')

work_list = ['深度学习','机器学习','pytorch','Tensorflow','目标检测','AI']



for raw_row in bsObj.find_all("tr",attrs={'class':'tr_list'}):
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

    job_text = str(job_Intro)
    for middle in work_list:
        if middle in job_text:
            print("{}---{}---{}".format(time, name, href))
            break


