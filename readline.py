pip install requests
pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup
import openpyxl

# 请求头信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# 创建Excel表格
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = '豆瓣电影Top250'
sheet['A1'] = '电影名'
sheet['B1'] = '评分'

# 爬取每一页的数据
for page in range(0, 250, 25):
    url = 'https://movie.douban.com/top250?start={}'.format(page)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('.grid_view .item')
    for item in items:
        title = item.select('.title')[0].text.strip()
        rating = item.select('.rating_num')[0].text.strip()
        sheet.append([title, rating])

# 保存Excel表格
workbook.save('douban_top250.xlsx')


