import os
import requests
import bs4
from pathlib import Path
import send2trash
import threading
import queue
import datetime

# making sure we're in the right dir and cleaning it up before we download all the comics
os.chdir('/Users/ilja/Dropbox/atbs/comics2')
for file in os.listdir():
    send2trash.send2trash(file)

# ==============================================================================
# MY VERSION


def download(num):
    res = requests.get('https://xkcd.com/'+str(num))
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
        print(f'successfully saved image number {num}')
    except:
        print('oops bad image')


# ATBS VERSION
def downloadXkcd(start, end):
    for urlNumber in range(start, end):

        # their version is simpler simply using start and end numbers that's all
        print(f'downloading image number {urlNumber}')
        res = requests.get(f'https://xkcd.com/{urlNumber}')
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


# ==============================================================================
start_time = datetime.datetime.now()

# single threaded
# NOTE: takes 42s for 100, so about 13.3m for the entire thing
# downloadXkcd(1, 100)


# MY VERSION - 3.5-5.5s
ts = []
for num in range(1, 100):
    t = threading.Thread(target=download, args=[num])
    t.start()
    ts.append(t)
for t in ts:
    t.join()
print(f'total threads started: {len(ts)}')  # 99


# ATBS VERSION - 3.5-4ss
# downloadThreads = []
# for i in range(0, 100, 10):
#     start = i
#     end = i + 9
#     if start == 0:
#         start = 1
#     downloadThread = threading.Thread(target=downloadXkcd, args=(start, end))
#     downloadThreads.append(downloadThread)
#     downloadThread.start()
# for t in downloadThreads:
#     t.join()
# print(f'total threads started: {len(downloadThreads)}') #10

# interesting - so conclusion is that theirs is even quicker probably because they don't need to start 100 threads, but just 10

# ==============================================================================
print('done!')
end_time = datetime.datetime.now()
diff = end_time-start_time
print(diff)
