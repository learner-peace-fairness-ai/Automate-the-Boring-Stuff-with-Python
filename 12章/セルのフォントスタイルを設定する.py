from openpyxl import Workbook
from openpyxl.styles import Font

book = Workbook()
sheet = book['Sheet']

italic24_font = Font(size=24, italic=True)
sheet['A1'].font = italic24_font
sheet['A1'] = 'Hello world!'

book.save('styled.xlsx')
