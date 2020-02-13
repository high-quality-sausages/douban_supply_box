import string
import ssl
import urllib
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup


def create_url(keyword: str, kind: str) -> str:
    '''
    Create url through keywords
    Args:
        keyword: the keyword you want to search
        kind: a string indicating the kind of search result
            type: 读书; num: 1001
            type: 电影; num: 1002
            type: 音乐; num: 1003
    Returns: url
    '''
    num = ''
    if kind == '读书':
        num = 1001
    elif kind == '电影':
        num = 1002
    elif kind == '音乐':
        num = 1003
    url = 'https://www.douban.com/search?cat=' + \
        str(num) + '&q=' + keyword
    return url


def get_html(url: str) -> str:
    '''send a request'''

    headers = {
        # 'Cookie': 你的cookie,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
        'Connection': 'keep-alive'
    }
    ssl._create_default_https_context = ssl._create_unverified_context

    s = urllib.parse.quote(url, safe=string.printable)  # safe表示可以忽略的部分
    req = urllib.request.Request(url=s, headers=headers)
    req = urllib.request.urlopen(req)
    content = req.read().decode('utf-8')
    return content


def get_content(keyword: str, kind: str) -> str:
    '''
    Create url through keywords
    Args:
        keyword: the keyword you want to search
        kind: a string indicating the kind of search result
            type: 读书; num: 1001
            type: 电影; num: 1002
            type: 音乐; num: 1003
    Returns: url
    '''
    url = create_url(keyword=keyword, kind=kind)
    html = get_html(url)
    # print(html)
    soup_content = BeautifulSoup(html, 'html.parser')
    contents = soup_content.find_all('h3', limit=1)
    result = str(contents[0])
    return result


def find_sid(raw_str: str) -> str:
    '''
        Args:
            raw_str: a html info string contains sid
        Returns:
            sid
    '''
    assert type(raw_str) == str, \
        '''the type of raw_str must be str'''
    start_index = raw_str.find('sid:')
    result = raw_str[start_index + 5: start_index + 13]
    result.strip(',')
    return result


if __name__ == "__main__":
    raw_str = get_content('1001', '看见')
    print(find_sid(raw_str))
