import urllib.request

response = urllib.request.urlopen("http://www.htouhui.com")
print(response.read())
