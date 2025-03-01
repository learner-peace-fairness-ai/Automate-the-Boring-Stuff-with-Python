from threading import Thread
import time


def take_a_nap():
    time.sleep(5)
    print('起きた！')


print('プログラム開始')

thread = Thread(target=take_a_nap)
thread.start()

print('プログラム終了')
