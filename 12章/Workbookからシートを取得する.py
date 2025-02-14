import openpyxl

book = openpyxl.load_workbook('example.xlsx')
print(book.sheetnames)

sheet = book['Sheet3']
print(sheet)
print(type(sheet))
print(sheet.title)

another_sheet = book.active
print(another_sheet)
