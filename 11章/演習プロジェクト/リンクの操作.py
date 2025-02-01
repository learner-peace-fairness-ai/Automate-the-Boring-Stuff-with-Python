# 指定したURLのページからリンクを取得し、リンク先のページをダウンロードする
# Usage: リンクの操作.py URL
from pathlib import Path
import sys
import time
from urllib.parse import urlparse

from bs4 import BeautifulSoup
import requests

START_URL = sys.argv[1]
DOWNLOAD_FOLDER = Path('download')
WAIT_SECONDS = 1
NOT_FOUND_HTTP_STATUS_CODE = 404

DOWNLOAD_FOLDER.mkdir(exist_ok=True)

parsed_url = urlparse(START_URL)
start_url_domain = f'{parsed_url.scheme}://{parsed_url.netloc}'

response = requests.get(START_URL)
soup = BeautifulSoup(response.text, 'html.parser')
link_list = soup.select('a[href]')
for i, link in enumerate(link_list):
    url = link.get('href')
    if url.startswith('/'):
        url = f'{start_url_domain}{url}'
    elif not url.startswith('http'):
        url = f'{start_url_domain}/{url}'
    
    response = requests.get(url)
    if response.status_code == NOT_FOUND_HTTP_STATUS_CODE:
        print(f'リンク切れ: {url}')
    else:
        new_file = DOWNLOAD_FOLDER / f'link{i}.html'
        with open(new_file, 'w', encoding='utf-8') as fw:
            fw.write(response.text)
    
    time.sleep(WAIT_SECONDS)
