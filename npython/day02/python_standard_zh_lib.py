from urllib import request
import re

# 打开并保存hmtl


def save_html(urlname):
    main_url = r'https://docs.python.org/2/library/'
    main_dir = r'E:'

    url = main_url + urlname + '.html'
    file_name = main_dir + urlname + '.html'
    try:
        req = request.urlopen(url)

        urlfile = open(file_name, 'w')
        urlfile.write(req.read())
    except Exception as e:
        print(e)

    finally:
        urlfile.close()

    # 保存主页
    save_html('index')


# 正则表达式查找链接并保存对应文件
req = request.urlopen(r'https://docs.python.org/2/library/')
p = re.compile(r'''''<li class="toctree-.+?"><a class="reference internal" href="(.+?).html">.+?</a></li>''')
matchs = p.findall(str(req.read()))


for row in matchs:
    save_html(row)
