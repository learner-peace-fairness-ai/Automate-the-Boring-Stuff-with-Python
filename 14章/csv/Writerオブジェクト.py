import csv

with open('output.csv', 'w', newline='') as fw:
    csv_writer = csv.writer(fw)

    csv_writer.writerow(['spam', 'eggs', 'bacon', 'ham'])
    csv_writer.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
    csv_writer.writerow([1, 2, 3.141592, 4])
