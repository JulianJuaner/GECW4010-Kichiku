import lxml, lxml.html
from lxml import etree
from multiprocessing import Pool as ThreadPool
from datetime import datetime
import numpy as np
import requests
import time
import sys
import re
import json
import MySQLdb

i=1
urls = []
tD='https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_8285897583458257&rid=22&type=0&pn='+str(i)+'&ps=20'
tooD='https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_20679987710906045&rid=26&type=0&pn='+str(i)+'&ps=20'
VOCALOID='https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_6060373409639355&rid=126&type=0&pn='+str(i)+'&ps=20'
guide='https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_08424519499179617&rid=127&type=0&pn='+str(i)+'&ps=20'
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
}

time1 = time.time()
#video_counter = 547653
#48010
for i in range(0, 58):
    url ='https://api.bilibili.com/x/web-interface/newlist?callback=jqueryCallback_bili_08424519499179617&rid=127&type=0&pn='+str(i)+'&ps=20'
    urls.append(url)
print('url loaded.')
#'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36'
Validtid = [26, 119, 126, 127, 22]
print("sleeping")
#time.sleep(500)
print("over")
retry = False
Validtype = ['2dMAD', 'kichiku', 'VOCALOID', 'guide', '3dMAD']
a = np.empty(0)
def spider(url):
    print(url)
    global retry, a
    try:
        JSON = requests.get(url, headers = head, timeout=(10, 10)).text
    except Exception as e:
        print(e)
        if retry == False:
            spider(url)
            retry = True
            return
        return
    retry = False

    JSON = json.loads(JSON)
    #print(json.dumps(JSON, indent=4, ensure_ascii=False))
    time.sleep(0.13)
    #print(url)
    if JSON["code"] == 0:
        #video_counter += 1
        #print(video_counter, end='')
        content = JSON["data"]["archives"]
        for m in content:
            a = np.append(a, m['aid'])
            #print(a)



#pool = ThreadPool()
# results = pool.map(spider, urls)
#print('here!')
for m in urls:
    spider(m)
np.save("guide.npy",a) 
    #print('here!')

