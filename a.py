#!python
#项目:从xkcd抓取漫画

#usage:输入url，输入要保存的路径

import os, requests, bs4

#切换,并创建文件夹
os.chdir('c:\\users\\howolac\\desktop')
os.makedirs('xkcd', exist_ok=True)

url = 'https://xkcd.com/15/'

while not url.endswith('#'):
    #请求网页
    res = requests.get(url)
    res.raise_for_status()

    #找到对应图片的链接
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    image_total = soup.select('#comic img')

    if image_total == []:
        print('comic image not find')
    else:
        image_solo_url = 'http:' + image_total[0].get('src')
        res = requests.get(image_solo_url)
        res.raise_for_status()

    #写入图片链接的数据到某个文件夹
    image_file = open(os.path.join('./xkcd', os.path.basename(image_solo_url)),
                      'wb')
    for i in res.iter_content(100000):
        image_file.write(i)
    image_file.close()

    #找到并打开前面的页面
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')

print('Done')
