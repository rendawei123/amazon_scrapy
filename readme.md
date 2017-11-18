安装

```python
#Windows平台
    1、pip3 install wheel #安装后，便支持通过wheel文件安装软件，wheel文件官网：https://www.lfd.uci.edu/~gohlke/pythonlibs
    3、pip3 install lxml
    4、pip3 install pyopenssl
    5、下载并安装pywin32：https://sourceforge.net/projects/pywin32/files/pywin32/
    6、下载twisted的wheel文件：http://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    7、执行pip3 install 下载目录\Twisted-17.9.0-cp36-cp36m-win_amd64.whl
    8、pip3 install scrapy
  
#Linux平台
    1、pip3 install scrapy
```

命令

```python
scrapy startproject amazon  #  创建一个scrapy项目

cd amazon/   # 切入到项目目录里面
scrapy genspider spider_douban movie.douban.com/top250   # 新建一个爬虫
scrapy runspider 爬虫绝对路径  #  运行爬虫

# 使用shell调试
# 在命令行键入 
scrapy shell
# 使用fetch()获取网页
In [2]: fetch('https://www.baidu.com')

# 查看局部命令
cd 项目名
scrapy
# 带参数的运行spider
scrapy crawl --nolog spider_goods -a keyword=iphone
```

选择器

```python
response.selector.css()
response.selector.xpath()
可简写为
response.css()
response.xpath()

#1 //与/
response.xpath('//body/a/')#
response.css('div a::text')

>>> response.xpath('//body/a') #开头的//代表从整篇文档中寻找,body之后的/代表body的儿子
[]
>>> response.xpath('//body//a') #开头的//代表从整篇文档中寻找,body之后的//代表body的子子孙孙
[<Selector xpath='//body//a' data='<a href="image1.html">Name: My image 1 <'>, <Selector xpath='//body//a' data='<a href="image2.html">Name: My image 2 <'>, <Selector xpath='//body//a' data='<a href="
image3.html">Name: My image 3 <'>, <Selector xpath='//body//a' data='<a href="image4.html">Name: My image 4 <'>, <Selector xpath='//body//a' data='<a href="image5.html">Name: My image 5 <'>]

#2 text
>>> response.xpath('//body//a/text()')
>>> response.css('body a::text')

#3、extract与extract_first:从selector对象中解出内容
>>> response.xpath('//div/a/text()').extract()
['Name: My image 1 ', 'Name: My image 2 ', 'Name: My image 3 ', 'Name: My image 4 ', 'Name: My image 5 ']
>>> response.css('div a::text').extract()
['Name: My image 1 ', 'Name: My image 2 ', 'Name: My image 3 ', 'Name: My image 4 ', 'Name: My image 5 ']

>>> response.xpath('//div/a/text()').extract_first()
'Name: My image 1 '
>>> response.css('div a::text').extract_first()
'Name: My image 1 '

#4、属性：xpath的属性加前缀@
>>> response.xpath('//div/a/@href').extract_first()
'image1.html'
>>> response.css('div a::attr(href)').extract_first()
'image1.html'

#4、嵌套查找
>>> response.xpath('//div').css('a').xpath('@href').extract_first()
'image1.html'

#5、设置默认值
>>> response.xpath('//div[@id="xxx"]').extract_first(default="not found")
'not found'

#4、按照属性查找
response.xpath('//div[@id="images"]/a[@href="image3.html"]/text()').extract()
response.css('#images a[@href="image3.html"]/text()').extract()

#5、按照属性模糊查找
response.xpath('//a[contains(@href,"image")]/@href').extract()
response.css('a[href*="image"]::attr(href)').extract()

response.xpath('//a[contains(@href,"image")]/img/@src').extract()
response.css('a[href*="imag"] img::attr(src)').extract()

response.xpath('//*[@href="image1.html"]')
response.css('*[href="image1.html"]')

#6、正则表达式
response.xpath('//a/text()').re(r'Name: (.*)')
response.xpath('//a/text()').re_first(r'Name: (.*)')

#7、xpath相对路径
>>> res=response.xpath('//a[contains(@href,"3")]')[0]
>>> res.xpath('img')
[<Selector xpath='img' data='<img src="image3_thumb.jpg">'>]
>>> res.xpath('./img')
[<Selector xpath='./img' data='<img src="image3_thumb.jpg">'>]
>>> res.xpath('.//img')
[<Selector xpath='.//img' data='<img src="image3_thumb.jpg">'>]
>>> res.xpath('//img') #这就是从头开始扫描
[<Selector xpath='//img' data='<img src="image1_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image2_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image3_thumb.jpg">'>, <Selector xpa
th='//img' data='<img src="image4_thumb.jpg">'>, <Selector xpath='//img' data='<img src="image5_thumb.jpg">'>]

#8、带变量的xpath
>>> response.xpath('//div[@id=$xxx]/a/text()',xxx='images').extract_first()
'Name: My image 1 '
>>> response.xpath('//div[count(a)=$yyy]/@id',yyy=5).extract_first() #求有5个a标签的div的id
'images'
```

