# printTable - 文字列のリストのリストを入力すると、各列を右揃えに整形された表形式で表示する
#              リストのリストは列のデータを表す

def print_table(columns):
    col_widths = get_column_widths(columns)

    num_datas_of_column = len(columns[0])
    for c in range(num_datas_of_column):
        for r in range(len(columns)):
            width = col_widths[r]

            print(columns[r][c].rjust(width), end='')

        print()


# 列幅を　最大幅+1　として列幅のリストを返す
def get_column_widths(columns):
    col_widths = [0] * len(columns)

    for i in range(len(columns)):
        max_width = 0
        for s in columns[i]:
            if len(s) > max_width:
                max_width = len(s)

        col_widths[i] = max_width + 1

    return col_widths


table_data = [['apples', 'oranges', 'cherries', 'banana'],  # 各リストは列のデータ
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
