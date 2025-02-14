from openpyxl import Workbook
from openpyxl.chart import BarChart
from openpyxl.chart import Reference

book = Workbook()
sheet = book.active

for i in range(1, 11):  # 列Aに適当にデータを作成する
    sheet[f'A{i}'] = i

ref_obj = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
chart_obj = BarChart()
chart_obj.add_data(ref_obj)

chart_obj.title = 'First series'
chart_obj.anchor = 'B4'  # 位置を設定
chart_obj.width = 15     # サイズを設定
chart_obj.height = 10

sheet.add_chart(chart_obj)

book.save('sampleChart.xlsx')
