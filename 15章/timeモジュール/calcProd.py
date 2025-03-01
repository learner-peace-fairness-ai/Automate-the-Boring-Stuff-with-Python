import math
import time


def calc_prod():
    #1～99,999の積を求める
    product = 1
    for i in range(1, 100000):
        product *= i
    return product


def get_digit_count(num):
    if num == 0:
        return 1
    else:
        return math.floor(math.log10(abs(num))) + 1


start_time = time.time()
prod = calc_prod()
end_time = time.time()

print(f'計算結果は{get_digit_count(prod)}桁です。')
print(f'計算時間は{end_time - start_time}秒でした。')
