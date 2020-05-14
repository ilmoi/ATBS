# 1. What does the openpyxl.load_workbook() function return?
# load a workbook
# NOTE to create a new one you would write openpyxl.Workbook(), not load_workbook()

# 2. What does the wb.sheetnames workbook attribute contain?
# print all sheets

# 3. How would you retrieve the Worksheet object for a sheet named 'Sheet1'?
# sheet = wb['Sheet1']

# 4. How would you retrieve the Worksheet object for the workbook’s active sheet?
# sheet = wb.active

# 5. How would you retrieve the value in the cell C5?
# cell = sheet['C5']

# 6. How would you set the value in the cell C5 to "Hello"?
# sheet['C5'] = 'Hello'

# 7. How would you retrieve the cell’s row and column as integers?
# print(cell.row, cell.colums)

# 8. What do the sheet.max_column and sheet.max_row sheet attributes hold, and what is the data type of these attributes?
# int

# 9. If you needed to get the integer index for column 'M', what function would you need to call?
# from openpyxl.utils import column_index_from_string('M')
# column_index_from_string('M')

# 10. If you needed to get the string name for column 14, what function would you need to call?
# from openpyxl.utils import get_column_letter(14)

# 11. How can you retrieve a tuple of all the Cell objects from A1 to F1?
# slice = tuple(sheet['A1:F1'])

# 12. How would you save the workbook to the filename example.xlsx?
# wb.save('example.xlsx')

# 13. How do you set a formula in a cell?
# sheet['A1'] = '=A2+A3'

# 14. If you want to retrieve the result of a cell’s formula instead of the cell’s formula itself, what must you do first?
# wb.load_workbook(filename, data_only=True)

# 15. How would you set the height of row 5 to 100?
# sheet.row_dimensions[5].height = 100

# 16. How would you hide column C?
#

# 17. What is a freeze pane?
#

# 18. What five functions and methods do you have to call to create a bar chart?
# refObj = openpyxl.chart.Reference(1234)
# seriesObj = openpyxl.chart.Series(refObj, name)
# chartObj = openpyxl.chart.BarChart()
# chartObj.append(seriesObj)
# sheet.add_chart(chartObj, 'starting cell')
