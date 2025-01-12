# inventory.py

def display_inventory(inventory):
    print('持ち物リスト：')

    total_number = 0
    for k, v in inventory.items():
        print(f'{v} {k}')
        total_number += v

    print(f'アイテムの総数: {total_number}')


stuff = {'ロープ': 1,
         'たいまつ': 6,
         '金貨': 42,
         '手裏剣': 1,
         '矢': 12}

display_inventory(stuff)
