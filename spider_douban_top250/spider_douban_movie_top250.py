# 爬取豆瓣电影top250
# 获取网页源码
# 使用正则表达式匹配源码中的有效信息
# 把匹配到的信息保存到文件里面

import requests
import re
import time
import threading


# 获取网页字符串中的有效信息
def get_message(url, p):
    response_string = requests.get(url).text
    message = p.findall(response_string)

    return message


# 爬取豆瓣电影top250某一页页信息
def spider_douban_movie_top250(pages):
    n = (pages - 1) * 25
    u1 = 'https://movie.douban.com/top250?start=' + str(n) + '&filter='

    p1 = re.compile(r'<li>.*?<div class="item">.*?'
                    r'<em class.*?>(\d+)</em>.*?'
                    r'</div>.*?<span class="title">(.*?)</span>', re.S)

    msg = get_message(u1, p1)

    for i in msg:
        with open('movie.txt', 'a+', encoding='utf-8') as f:
            f.write('排名：%s；电影：%s\n' % (i[0], i[1]))


if __name__ == '__main__':
    # spider_douban_movie_top250(2)
    t = time.time()
    l = []

    for j in range(1, 11):

        th = threading.Thread(target=spider_douban_movie_top250, args=(j,))
        l.append(th)
        th.start()

        # spider_douban_movie_top250(j)

    for k in l:
        k.join()

    print(time.time() - t)
