"""This doesn't use multithreading - I just want to see how long it takes."""

import os
import requests
import bs4
from pathlib import Path
import send2trash
import threading
import queue
import datetime

# making sure we're in the right dir and cleaning it up before we download all the comics
os.chdir('comics3')
for file in os.listdir():
    send2trash.send2trash(file)


# SINGLE THREAD
def download(href_full):
    res = requests.get(href_full)
    res.raise_for_status()

    # scrape
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # save the image
    try:
        img = soup.select('#comic > img')
        url = 'https://'+img[0].attrs['src'].strip('/')
        res = requests.get(url)
        with open(f'{Path(url).name}', 'wb') as f:
            for chunk in res.iter_content(100_000):
                f.write(chunk)
    except:
        print('oops bad image')

    # get the prev link
    prev = soup.select('#middleContainer > ul:nth-child(4) > li:nth-child(2) > a')
    href = prev[0].attrs['href']
    href_num = int(href.strip('/'))
    href_full = 'https://xkcd.com'+href
    # print(f'inside {href_num}')
    return href_full, href_num


start = datetime.datetime.now()
href_full = 'https://xkcd.com/'
href_num = 1  # needs to be above 0 to start

while href_num > 0:
    href_full, href_num = download(href_full)
    if href_num % 100 == 0:
        print(f'currently on {href_num}')
end = datetime.datetime.now()
diff = end-start
print(diff)
