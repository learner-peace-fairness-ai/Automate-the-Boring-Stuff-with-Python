#! python3
# multidownloadXkcd.py - XKCDコミックをマルチスレッドでダウンロードする

import math
from pathlib import Path
from threading import Thread
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

DOWNLOAD_FOLDER = Path('xkcd')  # コミックを保存するフォルダ
START_COMIC_PAGE = 1
END_COMIC_PAGE   = 6
THREAD_NUM = 2  # スレッドの総数


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        url = f'https://xkcd.com/{url_number}'
        # ページをダウンロードする
        print(f'ページをダウンロード中 {url} ...')
        res = requests.get(url)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, 'html.parser')
        
        # コミック画像のURLを見つける
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('コミック画像が見つかりませんでした。')
            continue

        comic_url = 'https:' + comic_elem[0].get('src')
        # 画像をダウンロードする
        print(f'画像をダウンロード中 {comic_url} ...')
        res = requests.get(comic_url)
        res.raise_for_status()

        # 画像をDOWNLOAD_FOLDERに保存する
        path = Path(urlparse(comic_url).path)
        new_file = DOWNLOAD_FOLDER / path.name
        with open(new_file, 'wb') as fw:
            for chunk in res.iter_content(100000):
                fw.write(chunk)


DOWNLOAD_FOLDER.mkdir(exist_ok=True)

# Threadオブジェクトを生成して開始する
download_threads = []  # 全Threadオブジェクトのリスト
step = math.ceil((END_COMIC_PAGE - START_COMIC_PAGE + 1) / THREAD_NUM)  # THREAD_NUM個のスレッドでページを等分割する
for i in range(START_COMIC_PAGE, END_COMIC_PAGE + 1, step):
    thread = Thread(target=download_xkcd, args=(i, i + step))
    download_threads.append(thread)
    thread.start()

# すべてのスレッドが終了するのを待つ
for thread in download_threads:
    thread.join()
print('完了')
