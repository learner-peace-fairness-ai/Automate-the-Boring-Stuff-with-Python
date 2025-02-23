#! python3
# removeCsvHeader.py - カレントディレクトリの全CSVファイルから見出しを削除する

import csv
from pathlib import Path

OUTPUT_FOLDER = Path('headerRemoved')

OUTPUT_FOLDER.mkdir(exist_ok=True)

# カレントディレクトリの全ファイルをループする
for csv_filename in [item for item in Path.cwd().iterdir() if item.is_file() and item.suffix == '.csv']:
    print(f'見出し削除中 {csv_filename.name}...')

    # CSVファイルを読み込む（最初の行をスキップする）
    csv_rows = []
    with open(csv_filename, encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if csv_reader.line_num == 1:
                continue  # 最初の行をスキップする
            csv_rows.append(row)

    # CSVファイルを書き出す
    with open(OUTPUT_FOLDER / csv_filename.name, 'w', newline='') as header_removed_csv_file:
        csv_writer = csv.writer(header_removed_csv_file)
        csv_writer.writerows(csv_rows)
