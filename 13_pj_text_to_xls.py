import openpyxl

with open('rando_text.txt', 'r') as f:
    txt = f.readlines()

for line in txt:
    if line == 'A\n':
        print(True)

for line in txt:
    if len(line) == 2:
        print(True)

wb = openpyxl.Workbook()
sheet = wb.active

# the simple one
for i in range(1, len(txt)+1):
    line = txt[i-1]
    sheet['A'+str(i)] = line

wb.save('text_converted_to_xls.xlsx')

# the more complex one - this one detects if a line says "A" or "B" and treats that as column name, so everything after that line gets put into a column
wb.create_sheet(title='complex')
complex = wb['complex']

for i in range(1, len(txt)+1):
    line = txt[i-1]
    if len(line) == 2:
        print('detected a break')
        col_name = line[:1]
        j = 1
        continue
    complex[str(col_name)+str(j)] = line
    j += 1

wb.save('text_converted_to_xls.xlsx')
