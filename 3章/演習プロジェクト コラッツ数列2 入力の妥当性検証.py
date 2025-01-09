import sys


def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1


try:
    s = input('整数を入力してください: ')
    num = int(s)
except ValueError:
    print(f'{s}は不正な値です。整数を入力してください。')
    sys.exit()

collatz_number = collatz(num)
print(collatz_number)

while collatz_number != 1:
    collatz_number = collatz(collatz_number)
    print(collatz_number)
