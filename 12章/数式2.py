import openpyxl

book_formulas = openpyxl.load_workbook('writeFormula.xlsx')
sheet = book_formulas.active
print(sheet['A3'].value)

book_data_only = openpyxl.load_workbook('writeFormula.xlsx', data_only=True)
sheet = book_data_only.active
print(sheet['A3'].value)
