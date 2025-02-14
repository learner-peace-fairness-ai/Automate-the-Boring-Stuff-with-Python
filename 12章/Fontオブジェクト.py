from openpyxl import Workbook
from openpyxl.styles import Font

book = Workbook()
sheet = book['Sheet']

font_obj1 = Font(name='Times New Roman', bold=True)
sheet['A1'].font = font_obj1
sheet['A1'] = 'Bold Times New Roman'

font_obj2 = Font(size=24, italic=True)
sheet['B3'].font = font_obj2
sheet['B3'] = '24 pt Italic'

book.save('styles.xlsx')
