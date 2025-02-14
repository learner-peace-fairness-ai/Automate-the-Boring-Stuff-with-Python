import openpyxl

book = openpyxl.load_workbook('produceSales.xlsx')
sheet = book.active

sheet.freeze_panes = 'A2'

book.save('freezeExample.xlsx')
