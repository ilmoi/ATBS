import openpyxl

N = 2
M = 3

wb = openpyxl.load_workbook('multiplication copy.xlsx')
sheet = wb.active

sheet.insert_rows(N, M)
wb.save('multiplication copy added rows.xlsx')
