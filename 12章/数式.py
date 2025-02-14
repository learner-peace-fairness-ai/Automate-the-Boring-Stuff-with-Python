from openpyxl import Workbook

book = Workbook()
sheet = book.active

sheet['A1'] = 200
sheet['A2'] = 300
sheet['A3'] = '=SUM(A1:A2)'

book.save('writeFormula.xlsx')
