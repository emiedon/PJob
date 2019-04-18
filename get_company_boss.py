# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
import time as t


##################
pages = 10
choicestage = 'D轮及以上'
choicetype = '互联网'
##################

company_type = {'分类信息', '通信/网络设备',
                '工程施工', '医疗健康',
                '数据服务', '媒体',
                '其他行业', 'O2O',
                '地产经纪/中介', '汽车生产',
                '酒店', '房地产开发',
                '计算机软件', '医疗/护理/卫生',
                '培训机构', '物流/仓储',
                '人力资源服务', '广告营销',
                '新零售', '食品/饮料/烟酒',
                '在线教育', '企业服务',
                '装修装饰', '旅游',
                '游戏', '移动互联网',
                '智能硬件', '生活服务',
                '电子商务', '互联网',
                '信息安全', '社交网络',
                '院校', '互联网金融'}
stage = {
         '不限':'',
         '未融资':'_zzz_t801',
         '天使轮':'_zzz_t802',
         'A轮':'_zzz_t803',
         'B轮':'_zzz_t804',
         'C轮':'_zzz_t805',
         'D轮及以上':'_zzz_t806',
         '已上市':'_zzz_t807',
         '不需要融资':'_zzz_t806'
         }


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
sleeptime = 2
def url2soup(url):
    t.sleep(sleeptime)
    global headers
    page = requests.get(url,headers=headers)
    page.encoding = 'utf-8'
    return BeautifulSoup(page.text, 'lxml')

company = {}

for i in range(pages):
    bsObj = url2soup('https://www.zhipin.com/gongsi/'+stage[choicestage] + '/' + '?page=' + str(i+1))
    work_list = bsObj.find_all("div",attrs={'class':'sub-li'})
    for _ in work_list:
        company_info = _.find('a',attrs={'class':'company-info'})
        company_url = company_info['href']
        company_text = company_info.find("div",attrs={'class':'conpany-text'})
        company_name = company_text.find("h4").text
        company_type = str(company_text.find("p"))[3:-4].split('<span class="vline"></span>')[1]
        company[company_name] = company_type

if choicetype:
    for i,j in enumerate(company.items()):
        k,l = j
        if l == choicetype:
            print("{}.{}".format(i, k))
else:
    for i,j in enumerate(company.keys()):
        print("{}.{}".format(i,j))



