from urllib import request

url = 'http://www.budejie.com/'
head = {'user-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}
req = request.Request(url, headers=head)
resp = request.urlopen(req)
request.urlretrieve(url, 'neihanduanzi.html')
#print(resp.read())
