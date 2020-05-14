"""Simple script that takes an argument > searched google with it > opens the first 10 tabs automatically for the user."""

import webbrowser
import bs4
import requests
from sys import argv

if len(argv) < 2:
    print('please enter your search term "in quotes" as an argument.')
    exit()


search_term = argv[1]
search_term.replace(' ', '+')
print(f'search term: {search_term}')


res = requests.get(f'https://pypi.org/search/?q={search_term}')
res.raise_for_status()
# print(res.text)


googleSoup = bs4.BeautifulSoup(res.text, 'lxml')
for i in range(1, 5):
    elems = googleSoup.select(
        f'#content > div > div > div.left-layout__main > form > div:nth-child(3) > ul > li:nth-child({i}) > a')
    # print(len(elems))
    # print(str(elems[0]))
    # print(elems[0].getText())
    href = elems[0].attrs['href']
    url = f'https://pypi.org{href}'
    webbrowser.open(url)
    # print(url)
