import urllib.parse

url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username': 'cqc',  'password': 'XXXX'}
headers = {'User-Agent': user_agent}
data = urllib.parse.urlencode(values)
request = urllib.request.Request(url, data, headers)
response = urllib.request.urlopen(request)
page = response.read()