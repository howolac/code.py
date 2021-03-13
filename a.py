#!python

import requests


def download(url):
    print('Downloading : ', url)
    html = requests.get(url).text
    #500-600的错误重试:13
    return html


print(download('https://www.baidu.com/s?ie=UTF-8&wd=urllib'))
