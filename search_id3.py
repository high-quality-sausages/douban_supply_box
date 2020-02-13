import string
import urllib
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def creat_url(name, num):
    #    movie_url = 'https://search.douban.com/movie/subject_search?search_text=%'+name+'&cat=1002'
    book_url = 'https://www.douban.com/search?cat='+num+'&q='+name+''
    return book_url
    # 电影 1002
    # 读书 1001
    # 音乐 1003


def get_html(url):
    headers = {
        # 'Cookie': 你的cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Connection': 'keep-alive'
    }

    s = urllib.parse.quote(url, safe=string.printable)  # safe表示可以忽略的部分
    req = urllib.request.Request(url=s, headers=headers)
    req = urllib.request.urlopen(req)
    content = req.read().decode('utf-8')
    return content


def get_content(num, name):
    url = creat_url(num, name)
    html = get_html(url)
    # print(html)
    soupContent = BeautifulSoup(html, 'html.parser')
    contents = soupContent.find_all('h3 ', limit=1)
    print(contents)


def main():
    get_content('1001', '看见')


main()
