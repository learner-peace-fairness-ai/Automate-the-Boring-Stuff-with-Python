# コミックサイトが更新されていたらデスクトップにダウンロードする

from pathlib import Path
from threading import Thread

import xkcd

DESKTOP = Path.home() / 'Desktop'
LATEST_COMIC_NUMBER_DB  = 'latest_comic_number_db'
COMIC_SITE_KEY = 'xkcd'

# xkcd
download_folder = DESKTOP / 'xkcd'
download_folder.mkdir(exist_ok=True)
xkcd_thread = Thread(target=xkcd.download_comic, args=[LATEST_COMIC_NUMBER_DB, COMIC_SITE_KEY, download_folder])
xkcd_thread.start()

# 他のコミックサイトのスレッドの作成とスタート

threads = [xkcd_thread]
for thread in threads:
    thread.join()
    print('更新の確認を完了しました。')
