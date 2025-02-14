from openpyxl import Workbook

book = Workbook()
sheet = book['Sheet']

sheet['A1'] = 'Hello world!'
print(sheet['A1'].value)
