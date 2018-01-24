from urllib import parse, request, response

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc',  'password': 'XXXX'}
headers = {'User-Agent': user_agent}
data = parse.urlencode(values)
print(data)
req = request.Request(url, data, headers)