import csv

with open('example.csv', encoding='utf-8') as  fr:
    csv_reader = csv.reader(fr)

    rows = list(csv_reader)
    print(rows)

print(rows[0][0])
print(rows[0][1])
print(rows[0][2])
print(rows[1][1])
print(rows[6][1])
