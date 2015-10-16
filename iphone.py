import urllib
import urllib.request
import urllib.parse

url='http://172.29.152.231/php/da2405610ea8059981af53be1038ef8b/'
user_agent='Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13A452 Safari/601.1.46'
headers={'User-Agent':user_agent}

request=urllib.request.Request(url, headers=headers)
response=urllib.request.urlopen(request)
page=response.read()
page=page.decode('gbk')
print(page)
