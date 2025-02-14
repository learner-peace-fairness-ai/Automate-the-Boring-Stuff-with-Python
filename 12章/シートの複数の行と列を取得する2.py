import openpyxl

book = openpyxl.load_workbook('example.xlsx')
sheet = book.active

print(sheet['B'])

for cell_obj in sheet['B']:
    print(cell_obj.value)
