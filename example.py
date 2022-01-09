import requests
from bs4 import BeautifulSoup

import csv

headers = {'user-agent': 'Mozilla/5.0 (Macintosh Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}

target_url = 'https://news.cnyes.com/news/cat/headline?exp=a';

result = requests.get(target_url, headers=headers)

bs = BeautifulSoup(result.text,'html.parser')

blocks = bs.findAll("a", {"class" : "_1Zdp"})

content_urls = []
for block in blocks:
    path = block.get('href')
    content_url = 'https://news.cnyes.com' + path
    content_urls.append(content_url)

output_file_name = 'cnyes1.csv'

with open(output_file_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['標題', 'content'])
    
    for url in content_urls:
        result = requests.get(url, headers=headers)
        bs = BeautifulSoup(result.text,'html.parser')
        title = bs.find('h1').text
        content = bs.find("div", {"class" : "_2E8y"}).text
        writer.writerow([title, content])
