# 对于urllib库的学习
# urllib可以模拟浏览器的行为,向指定的服务器发送一个请求，并可以保存服务器返回的数据


from urllib import request
from urllib import parse

# urlopen()函数的使用
resp = request.urlopen('http://www.baidu.com')
data_line = resp.readlines()
print(data_line, end='\n')
print(resp.getcode())

# urlretrieve()函数的使用
# 此函数可以讲网站上的一个文件保存到本地
request.urlretrieve("http://www.baidu.com","baidu.html")
request.urlretrieve("https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=29996277,1226987297&fm=26&gp=0.jpg","suoda.jpg")

# urlencode()函数的使用
# 当使用代码发送请求时，此函数可以把字典数据转换为URL编码的数据
data = dict(name="爬虫基础", greet="hello world", age="100")
qs = parse.urlencode(data)
print(qs)

# parse_qs()函数可以讲编码后的数据进行解码
web_data = parse.parse_qs(qs)
print(web_data)

params = {'wd': '索隆'}
# qs = parse.urlencode(params)
# url = 'https://www.baidu.com/baidu'
# url = url + "?" + qs
# resp = request.urlopen(url)
# web_data = resp.readlines()
# print(web_data)

# urlparse()函数和urlsplit()函数的使用
url = 'http://www.baidu.com/s?username=zhiliao'
result = parse.urlsplit(url)
# result = parse.urlparse(url)

print('scheme:', result.scheme)
print('netloc:', result.netloc)
print('path', result.path)
print('query', result.query)

# request.Request类，如果想要在请求的时候增加一些请求头，那么就必须使用request.Request类来实现
# 例如下面的爬取代码，如果不做任何处理会被返回一串莫名其妙没有任何意义的代码
url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
# resp = request.urlopen(url)
# print(resp.readlines())
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
req = request.Request(url, headers=headers)
request.urlretrieve(url, "lagou.html")


