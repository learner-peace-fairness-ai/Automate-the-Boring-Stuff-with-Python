import csv

with open('example.csv', encoding='utf-8') as  fr:
    csv_reader = csv.reader(fr)

    for row in csv_reader:
        print(f'Row #{csv_reader.line_num} {row}')
