import csv

with open('example.tsv', 'w', newline='') as fw:
    csv_writer = csv.writer(fw, delimiter='\t', lineterminator='\n\n')

    csv_writer.writerow(['apples', 'oranges', 'grapes'])
    csv_writer.writerow(['eggs', 'bacon', 'ham'])
    csv_writer.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
