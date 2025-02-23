# カレントディレクトリにある全てのExcelファイルをCSVに変換する

import csv
from pathlib import Path

import openpyxl

# カレントディレクトリのxlsxファイルをループ
for excel_file in [item for item in Path.cwd().iterdir() if item.is_file() and item.suffix == '.xlsx']:
    wb = openpyxl.load_workbook(excel_file, data_only=True)
    for ws in wb.worksheets:
        csv_file_name = f'{excel_file.stem}_{ws.title}.csv'
        with open(csv_file_name, 'w', newline='') as fw:
            csv_writer = csv.writer(fw)
            for row in ws.iter_rows():
                row_data = []
                for cell in row:
                    row_data.append(cell.value)
                    csv_writer.writerow(row_data)

    wb.close()
