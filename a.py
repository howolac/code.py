#!python
#_*_ coding:utf8 _*_
import urllib.request, os, requests
from urllib.error import URLError, HTTPError, ContentTooShortError


#接受url，返回req
#有header
def Download(url, num_retries=2):
    print('Downloading : ', url)
    headers = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50'
    }
    req = requests.get(url, headers=headers)
    req.raise_for_status()
    return req

    # try:
    #     quote()进行编码，解决不合法字符问题（如中文字符）
    #     req = urllib.request.urlopen(url)
    #     req = req.read()

    # #如果是500—600之间的错误码就继续尝试num_retries+1次
    # except (URLError, HTTPError, ContentTooShortError) as e:
    #     print('Download error:', e.reason)
    #     if num_retries > 0:
    #         if hasattr(e, 'code') and 500 <= e.code < 600:
    #             return Download_Urllib(url, num_retries - 1)
    #     req = None
    # return req


#‘切换’并以将urllib的html对象以‘byte’的形式‘保存’到‘桌面’中
#file_name=x
def SaveFile(file_name, data, y='wb'):
    print('Saving...')

    os.chdir('c:\\users\\howolac\\desktop')
    file = open(file_name, y)
    for chunk in data.iter_content(100000):
        file.write(chunk)

    # file = open(file_name, y)
    # file.write(data)
    # file.close()


SaveFile('a.html', Download('https://zhuanlan.zhihu.com/p/35625779'))
