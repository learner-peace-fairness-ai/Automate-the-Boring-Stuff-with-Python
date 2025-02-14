import openpyxl

book = openpyxl.load_workbook('example.xlsx')
print(type(book))
