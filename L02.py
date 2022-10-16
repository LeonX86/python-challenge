# http://www.pythonchallenge.com/pc/def/equality.html
import urllib.request
import re
from collections import Counter


def get_html_page(url):
    page = None
    resp = urllib.request.urlopen(url)
    if (resp.status == 200):
        page = resp.read().decode('utf-8')
    return page


def get_comments(page):
    rs = re.findall('<!--\s*(.*?)\s*-->', page, re.S)
    print(rs)
    if rs:
        return rs[1]
    return None


"""
def main():
    url = 'http://www.pythonchallenge.com/pc/def/ocr.html'

    page = get_html_page(url)
    comments = get_comments(page)
    print(comments)
    maps = {}
    for c in comments:
        maps[c] = maps.get(c, 0) + 1

    half = len(comments) // len(maps)
    rs = ""
    for k, v in maps.items():
        if v < half:
            rs += k
    print(rs)


main()"""

url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
page = get_html_page(url)
comments = get_comments(page)
print(Counter(comments))
