import requests
import bs4
from lxml import etree
import re

search_term = 'hacker'

res = requests.get(f"https://www.flickr.com/search/?text={search_term}")
res.raise_for_status()
# print(res.text)

soup = bs4.BeautifulSoup(res.text, 'lxml')
# elems = soup.select("//a[@class='overlay']") #cant use xpath

# >>>>> etree approach - not doing
# html_parser = etree.HTMLParser()
# tree = etree.parse(res.text, html_parser)
# a = tree.xpath("//a[@class='overlay']")
# with open('parsed_flickr.txt', 'w') as f:
#     f.write(a)

# here's the correct way
r = re.compile(r'live.*')
all_pics = soup.findAll('div', class_="view photo-list-photo-view requiredToShowOnServer awake")
print(len(all_pics))
i = 0
for pic in all_pics:
    i += 1
    # the url is hidden inside of the style attribute. we can open up the file as a dictionary
    pic = str(pic['style'])
    # print(pic)
    mo = r.search(pic)
    link = 'http://'+str(mo.group())[:-1]
    # print(link)

    res = requests.get(link)
    res.raise_for_status()
    with open(f'doge/doge_{i}.jpg', 'wb') as f:
        for chunk in res.iter_content(100_000):
            f.write(chunk)

# alternative
# all_pics = soup.select('div[class="view photo-list-photo-view requiredToShowOnServer awake"]')
# print(len(all_pics))
# for pic in all_pics:
#     print(pic)
