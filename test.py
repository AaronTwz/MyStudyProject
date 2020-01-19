import xlrd

fileName = r'C:\Users\Administrator\Desktop\品阶1\111.xlsx'
sheetInput = xlrd.open_workbook(fileName)
sheet1 = sheetInput.sheet_by_index(0)
# a = eval(sheet1.cell_value(0, 0))
b = eval(str(sheet1.cell_value(1, 0)))
c = eval(str(sheet1.cell_value(2, 0)))
d = eval(sheet1.cell_value(3, 0))
e = eval(sheet1.cell_value(4, 0))

at = sheet1.cell_type(0, 0)
bt = sheet1.cell_type(1, 0)
ct = sheet1.cell_type(2, 0)
dt = sheet1.cell_type(1, 0)
et = sheet1.cell_type(2, 0)

print( c, d, e)
print( type(c), type(d), type(e))
