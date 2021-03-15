from urllib.request import urlopen
from bs4 import BeautifulSoup

#获取
req = urlopen('http://www.pythonscraping.com/pages/page1.html')

#beautifulsoup
bs = BeautifulSoup(req.read(),"html.parser")
#。h1
print(bs.nones)
