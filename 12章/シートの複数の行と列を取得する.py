import openpyxl

book = openpyxl.load_workbook('example.xlsx')
sheet = book['Sheet1']

print(tuple(sheet['A1':'C3']))

for row_of_cell_objects in sheet['A1':'C3']:
    for cell_obj in row_of_cell_objects:
        print(cell_obj.coordinate, cell_obj.value)
    print('--- END OF ROW ---')
