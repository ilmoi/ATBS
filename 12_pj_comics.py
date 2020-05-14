"""simple script downloads all comics from a particular website"""

import requests
import bs4
import subprocess
from pathlib import Path

# ==============================================================================
# Option 1: using curl

# DO IT ONCE
res = requests.get('https://xkcd.com/')
res.raise_for_status()

# scrape
soup = bs4.BeautifulSoup(res.text, 'lxml')

# save the image
img = soup.select('#comic > img')
url = 'https://'+img[0].attrs['src'].strip('/')
subprocess.run(f'curl {url} -o comics/file1.jpg', shell=True)

# get the prev link
prev = soup.select('#middleContainer > ul:nth-child(4) > li:nth-child(2) > a')
href = prev[0].attrs['href']
href_num = int(href.strip('/'))
href_full = 'https://xkcd.com'+href

# DO IT MANY TIMES
while href_num > 0:
    res = requests.get(href_full)
    res.raise_for_status()

    # scrape
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    # save the image
    try:
        img = soup.select('#comic > img')
        url = 'https://'+img[0].attrs['src'].strip('/')
        subprocess.run(f'curl {url} -o comics/joke_{href_num}.jpg', shell=True)
    except:
        pass

    # get the prev link
    prev = soup.select('#middleContainer > ul:nth-child(4) > li:nth-child(2) > a')
    href = prev[0].attrs['href']
    href_num = int(href.strip('/'))
    href_full = 'https://xkcd.com'+href

# ==============================================================================
# Option 2: saving direcly using requests

res = requests.get('https://xkcd.com/')
res.raise_for_status()

# scrape
soup = bs4.BeautifulSoup(res.text, 'lxml')

# save the image
img = soup.select('#comic > img')
url = 'https://'+img[0].attrs['src'].strip('/')
# THIS IS THE PART THAT'S DIFFERENT
# subprocess.run(f'curl {url} -o comics/file1.jpg', shell=True)
res = requests.get(url)
with open(f'{Path(url).name}', 'wb') as f:
    for chunk in res.iter_content(100_000):
        f.write(chunk)

# REST IS THE SAME
