import random

heads = 0
for i in range(1, 1001):
    if random.randint(0, 1) == 1:
        heads += 1
    
    if i == 500:
        print('半分完了！')

print(f'表は{heads}回出ました。')
