# -*- coding: utf-8 -*-
import urllib
import urllib.request
import urllib.parse
import http.cookiejar
import re
class GetItems:
    """get classes from website"""

    def __init__(self):
        """initialize class"""
        self.loginUrl="http://222.194.15.1:7777/pls/wwwbks/bks_login2.login"
        self.openUrl=""
        self.stuid=""
        self.pwd=""
        self.postdata=b''
        self.isAuth=False
        cookies=http.cookiejar.CookieJar()
        opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookies))
        urllib.request.install_opener(opener)   
    def seturl(self, openUrl):
        """set openurl value"""
        self.openUrl=openUrl
    
    def setpost(self, stuid, pwd):
        """set postdata values"""
        self.stuid=stuid
        self.pwd=pwd
        self.postdata=urllib.parse.urlencode({'stuid':self.stuid, 'pwd':self.pwd}).encode('UTF8')
    def getpage(self,code):
        """login website"""
        request=urllib.request.Request(self.loginUrl, self.postdata)
        _response=urllib.request.urlopen(request)
        _response=urllib.request.urlopen(self.openUrl)
        _data=_response.read()
        _data=_data.decode(code)
        return _data
    def getauthstatus(self):
        self.openUrl="http://222.194.15.1:7777/pls/wwwbks/bks_login2.loginmessage"
        page=self.getpage('gbk')
        #正则匹配
        myItems = re.findall('<font.*?>(.*?)</font>',page,re.S) 
        for item in myItems:
            find=item.find('登录成功')
            if find!=-1:
                self.isAuth=True
    def getgrade(self):
        self.openUrl="http://222.194.15.1:7777/pls/wwwbks/bkscjcx.yxkc"
        page=self.getpage('gbk')
        #正则匹配
        myItems = re.findall('<TR>.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?<p.*?>(.*?)</p>.*?<p.*?>.*?<p.*?>(.*?)</p>.*?<p.*?>(.*?)</p>.*?<p.*?>.*?<p.*?>(.*?)</p>.*?<p.*?>(.*?)</p>.*?<p.*?>.*?<p.*?>(.*?)</p>.*?</TR>',page,re.S) 
        return myItems
    
    def getclass(self):
        self.openUrl="http://222.194.15.1:7777/pls/wwwbks/xk.CourseView"
        page=self.getpage('gbk')
        pageclass=re.findall('<td.*?上课周次.*?</td>(.*?)<tr>.*?', page, re.S)
        #将元组转化为字符串，以便进一步利用正则表达式
        pages=""
        for pagesingle in pageclass:
            pages=pages+''.join(pagesingle)
        myItems=re.findall('<TR>.*?<p.*?>(.*?)&nbsp;</p>.*?<p.*?<p.*?<p.*?<p.*?<p.*?<p.*?>(.*?)&nbsp;</p>.*?<p.*?>(.*?)-(.*?)&nbsp;</p>.*?<p.*?>(.*?)-(.*?)周上.*?</TR>', pages, re.S)
        return myItems
"""getitems=GetItems()
getitems.setpost("130420215", "0000")
getitems.getauthstatus()
print(getitems.isAuth)"""

