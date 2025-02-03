from pathlib import Path
import sys
from urllib.parse import urlparse

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://www.flickr.com'
MAX_WAIT_SECONDS = 10


def search_image(keyword, driver, wait):
    SEARCH_ICON_CLASS_NAME = 'search-icon'
    SEARCH_BOX_ID = 'text-2'

    # 検索アイコンをクリック
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, SEARCH_ICON_CLASS_NAME)))
    search_icon = driver.find_element(By.CLASS_NAME, SEARCH_ICON_CLASS_NAME)
    search_icon.click()

    # 検索ボックスにキーワードを入力
    wait.until(EC.visibility_of_element_located((By.ID, SEARCH_BOX_ID)))
    search_box = driver.find_element(By.ID, SEARCH_BOX_ID)
    search_box.send_keys(keyword)

    # フォームを送信
    search_box.submit()


def get_images(driver, wait):
    IMAGES_CSS_SELECTOR = '.search-photos-results img'

    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, IMAGES_CSS_SELECTOR)))
    return driver.find_elements(By.CSS_SELECTOR, IMAGES_CSS_SELECTOR)


keyword = sys.argv[1]

driver = webdriver.Edge()
wait = WebDriverWait(driver, MAX_WAIT_SECONDS)

driver.get(URL)

search_image(keyword, driver, wait)

image_list = get_images(driver, wait)

for i, image in enumerate(image_list):
    src_url = image.get_attribute('src')
    file_extension = Path(urlparse(src_url).path).suffix

    response = requests.get(src_url)
    if response.status_code == 200:
        new_file = Path(f'img{i}{file_extension}')
        with open(new_file, 'wb') as fw:
            for chunk in response.iter_content(chunk_size=100000):
                fw.write(chunk)

        print(f'{src_url} のダウンロードが成功しました')
    else:
        print(f'{src_url} のダウンロードに失敗しました (ステータスコード: {response.status_code})')

driver.quit()
