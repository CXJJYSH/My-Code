import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self,site):
        self.site=site
        
    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html=r.read()
        parser="html.parser"
        sp=BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url=tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n"+url)
        with open("20.1","a") as f:
            for tag in sp.find_all("a"):
                url=tag.get("href")
                if url is None:
                    continue
                if "html" in url:
                    f.write(url+"\n")

news="https://news.sina.com.cn/"
#news="https://news.google.com/"
Scraper(news).scrape()
#不知道是不是探索者梯子还是不够牛逼还是别的原因，我想要去爬Google新闻页面的头条链接会出现网络超时的报错。
#沃趣，这爬虫爬新浪新闻爬得也太快了。
