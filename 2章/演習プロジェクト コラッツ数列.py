def collatz(number):
    if number % 2 == 0:
        return int(number / 2)
    else:
        return 3 * number + 1


num = int(input('整数を入力してください: '))
collatz_number = collatz(num)
print(collatz_number)

while collatz_number != 1:
    collatz_number = collatz(collatz_number)
    print(collatz_number)
