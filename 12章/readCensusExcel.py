#! python3
# readCensusExcel.py - 群ごとに人口と人口調査標準地域の数を集計する

from collections import defaultdict
import pprint

import openpyxl

CENSUS_TRACT = 'tracts'
POPULATION   = 'pop'


def convert_defaultdict_to_dict(nested_dict):
    nested_dict = dict(nested_dict)
    return {k: dict(v) for k, v in nested_dict.items()}


print('ワークブックを開いています...')
book = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = book['Population by Census Tract']

# 州と群のキーが確実に存在するようにする
county_data = defaultdict(lambda: defaultdict(lambda: {CENSUS_TRACT: 0, POPULATION: 0}))

# county_dataに群の人口と地域数を格納する
print('行を読み込んでいます...')
for row in range(2, sheet.max_row + 1):
    # スプレッドシートの1行に、ひとつの人口調査標準地域のデータがある
    state = sheet[f'B{row}'].value
    county = sheet[f'C{row}'].value
    population = sheet[f'D{row}'].value

    # 各行が人口調査標準地域を表すので、数を1つ増やす
    county_data[state][county][CENSUS_TRACT] += 1
    # この人口調査標準地域の人口だけ群の人口を増やす
    county_data[state][county][POPULATION] += int(population)

county_data = convert_defaultdict_to_dict(county_data)

# 新しいテキストファイルを開き、county_dataの内容を書き込む
print('結果を書き込み中...')
with open('census2010.py', 'w', encoding='utf-8') as result_file:
    result_file.write(f'all_data = {pprint.pformat(county_data)}')
print('完了')
