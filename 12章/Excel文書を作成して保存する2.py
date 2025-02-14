import openpyxl

book = openpyxl.load_workbook('example.xlsx')
sheet = book.active

sheet.title = 'Spam Spam Spam'
book.save('example_copy.xlsx')
