#codeing:utf-8
import re
import urllib
import urllib.request
import urllib.parse
import http.cookiejar

class GetNews:
    
    def __init__(self):
        """initialize the class"""
        self.openUrl=""
        self.user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64)"
        self.headers={'User-Agent':self.user_agent}
        cookies=http.cookiejar.CookieJar()
        opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookies))
        urllib.request.install_opener(opener)
    def seturl(self, openUrl):
        """set the URL to open website"""
        self.openUrl=openUrl
    def getpage(self):
        """get html content from website"""
        request=urllib.request.Request(self.openUrl, headers=self.headers)
        page=urllib.request.urlopen(request)
        data=page.read()
        data=data.decode('utf-8')
        return data
        
    def getnotices(self):
        """get notices from website"""
        self.seturl('http://today.hitwh.edu.cn/news_more_list.asp?page=1&id=7&nid=')
        page=self.getpage()
        #print(page)
        myItems=re.findall('<span><font.*?>(.*?)</font>.*?<a.*?href=(.*?)>(.*?)</a>.*?&nbsp;&nbsp;(.*?)</font>.*?', page, re.S)
        
        return myItems
        
    def getnews(self):
        """get news from website"""
        self.seturl('http://news.hitwh.edu.cn/news_list.asp?page=1&id=1&nid=')
        page=self.getpage()
        expression=r'<a class="size14".*?href=(.*?)>(.*?)&nbsp;&nbsp;<font.*?</a>&nbsp;&nbsp;(.*?)</li>.*?'
        myItems=re.findall(expression, page, re.S)
        return myItems
    
    def getscience(self):
        """get scientific information """
        self.seturl('http://today.hitwh.edu.cn/news_more_list.asp?page=1&id=10&nid=')
        page=self.getpage()
        #print(page)
        myItems=re.findall('<span><font.*?>(.*?)</font>.*?<a.*?href=(.*?)>(.*?)</a>.*?&nbsp;&nbsp;(.*?)</font>.*?', page, re.S)
        return myItems
