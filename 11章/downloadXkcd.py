#! python3
# downloadXkcd.py - XKCDコミックをひとつずつダウンロードする

from pathlib import Path

from bs4 import BeautifulSoup
import requests

url = 'https://xkcd.com'  # 開始URL
folder = Path('xkcd')
folder.mkdir(exist_ok=True)  # ./xkcdに保存する

while not url.endswith('#'):
    # ページをダウンロードする
    print(f'ページをダウンロード中 {url}...')
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')

    # コミック画像のURLを見つける
    comic_elems = soup.select('#comic img')
    if comic_elems:
        comic_url = f'https:{comic_elems[0].get('src')}'
        
        # 画像をダウンロードする
        print(f'画像をダウンロード中 {comic_url}')
        res = requests.get(comic_url)
        res.raise_for_status()
        
        # 画像を.xkcdに保存する
        filename = Path(comic_url).name
        with open(folder/filename, 'wb') as image_file:
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
    else:
        print('コミック画像がみつかりませんでした。')

    # PrevボタンのURLを取得する
    prev_link = soup.find('a', {'rel': 'prev'})
    url = f'https://xkcd.com{prev_link.get('href')}'

print('完了')
