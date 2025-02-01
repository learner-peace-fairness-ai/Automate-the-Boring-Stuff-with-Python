#! python3
# lucky.py - Bing検索結果をいくつか開く

import sys
import webbrowser

from bs4 import BeautifulSoup
import requests

print('Bing...')  # Bingページをダウンロード中にテキストを表示
res = requests.get(f'https://www.bing.com/search?q={' '.join(sys.argv[1:])}')
res.raise_for_status()

# 上位の検索結果のリンクを取得する
soup = BeautifulSoup(res.text, 'html.parser')
link_elems = soup.select('.b_algo a')

# 各結果をブラウザのタブで開く
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open(link_elems[i].get('href'))
