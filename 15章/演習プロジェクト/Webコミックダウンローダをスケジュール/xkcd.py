# XKCDコミックをダウンロードする

from pathlib import Path
import shelve
import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

WAIT_TIME_SEC = 1

def exists_page(response):
    try:
        response.raise_for_status()
        return True
    except:
        return False


def download_comic(latest_comic_number_db, comic_site_key, download_folder):
    # 最新のcomic_numを取得する
    with shelve.open(latest_comic_number_db) as shelf:
        lastest_comic = shelf.get(comic_site_key, 0)
    
    # 前回の続きのページから探し始める
    while True:
        new_comic = lastest_comic + 1
        url = f'https://xkcd.com/{new_comic}'
    
        print(f'ページをダウンロード中 {url} ...')
        res = requests.get(url)
        if not exists_page(res):
            print('ページが見つかりませんでした。')
            return
        
        time.sleep(WAIT_TIME_SEC)
        
        # ページをダウンロードする
        soup = BeautifulSoup(res.text, 'html.parser')
        # コミック画像のURLを見つける
        comic_elem = soup.select('#comic img')
        if comic_elem == []:
            print('コミック画像が見つかりませんでした。')
            return

        comic_url = 'https:' + comic_elem[0].get('src')
        # 画像をダウンロードする
        print(f'画像をダウンロード中 {comic_url} ...')
        res = requests.get(comic_url)
        res.raise_for_status()

        # 画像をDOWNLOAD_FOLDERに保存する
        path = Path(urlparse(comic_url).path)
        new_file = download_folder / path.name
        with open(new_file, 'wb') as fw:
            for chunk in res.iter_content(100000):
                fw.write(chunk)
        
        lastest_comic = new_comic

        # 最新のcomic_numを保存
        with shelve.open(latest_comic_number_db) as shelf:
            shelf[comic_site_key] = lastest_comic
        
        time.sleep(WAIT_TIME_SEC)
