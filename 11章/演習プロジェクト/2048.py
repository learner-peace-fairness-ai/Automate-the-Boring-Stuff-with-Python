import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = 'https://play2048.co/'
MAX_WAIT_SECONDS      = 10
KEY_INPU_WAIT_SECONDS = 1
DIRECTION = (Keys.UP, Keys.DOWN, Keys.LEFT, Keys.RIGHT)
NUMBER_MOVES = 10
BOARD_XPATH = '//div[@data-touch-input]'
SCORE_XPATH = '//span[text()="Score"]/following-sibling::span[2]'

driver = webdriver.Edge()
wait = WebDriverWait(driver, MAX_WAIT_SECONDS)

driver.get(URL)
wait.until(EC.visibility_of_all_elements_located((By.XPATH, BOARD_XPATH)))

page = driver.find_element(By.TAG_NAME, 'html')
for _ in range(NUMBER_MOVES):
    key = random.choice(DIRECTION)
    page.send_keys(key)
    
    time.sleep(KEY_INPU_WAIT_SECONDS)

wait.until(EC.visibility_of_element_located((By.XPATH, SCORE_XPATH)))
score = driver.find_element(By.XPATH, SCORE_XPATH)
print(f'Score: {score.text}')

driver.quit()
