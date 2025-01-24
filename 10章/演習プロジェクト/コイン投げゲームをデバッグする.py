import random

guess = ''
while guess not in ('表', '裏'):
    print('コインの表裏を当ててください。表か裏を入力してください：')
    guess = input()
# ---------------変更 始---------------
# toss = random.randint(0, 1)  # 0 は裏、1 は表
if random.randint(0, 1):  # 0 は裏、1 は表
    toss = '表'
else:
    toss = '裏'
# ---------------変更 終---------------
if toss == guess:
    print('当たり！')
else:
    print('はずれ！もう一回当てて！')
    guess = input()
    if toss == guess:
        print('当たり！')
    else:
        print('はずれ。このゲームは苦手ですね。')
