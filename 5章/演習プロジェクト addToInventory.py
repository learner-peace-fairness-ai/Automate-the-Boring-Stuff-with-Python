# add_to_inventory.py
def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


def display_inventory(inventory):
    print('持ち物リスト：')

    total_number = 0
    for item, num in inventory.items():
        print(f'{num} {item}')
        total_number += num

    print(f'アイテムの総数: {total_number}')


inv = {'金貨': 42, 'ロープ': 1}
dragon_loot = ['金貨', '手裏剣', '金貨', '金貨', 'ルビー']

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)
