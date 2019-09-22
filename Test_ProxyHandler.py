# ProxyHandler技术的学习（代理设置）
# 很多网站会检测某一段时间内谋和ip的访问次数，如果发现异常会禁止此ip的访问。
# 所以可以使用此技术来设置一些代理服务器，每隔一段时间换一个代理，就算ip被禁止
# 可以换另外一个ip继续爬取。
# from urllib import request
# handler = request.ProxyHandler({'': ''})
# opener = request.build_opener(handler)
# req = request.Request('')
# resp = opener.open(req)
# print(resp.read())


from urllib import request

url = 'http://httpbin.org/ip'
# # 没有使用代理
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理的步骤
# 1.使用ProxyHandler，传入代理构建一个handler
handler = request.ProxyHandler({'http': '183.129.244.16:12187'})
# 2.使用上面创建的handler构建一个opener
opener = request.build_opener(handler)
# 3.使用opener去发送一个请求
resp = opener.open('http://www.baidu.com')
# resp = request.urlopen('http://www.baidu.com')
print(resp.read())

