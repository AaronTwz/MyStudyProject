import xlrd, xlwt


def GetDataFromTable(file_name):
    # 读取excel
    loginFile = xlrd.open_workbook(file_name)
    sheet1 = loginFile.sheets()[0]
    # 获取行数
    row_list = []
    rowNum = sheet1.nrows
    global count
    count = rowNum

    # 获取每行内容
    for row in range(0, rowNum, 1):
        index = int(sheet1.cell(row, 0).value)
        id = str(sheet1.cell(row, 1).value)
        des = str(sheet1.cell(row, 2).value)
        followID = [i for i in sheet1.row_values(row)[3:] if i != '']
        row_list.append([index, id, des, followID])

    return row_list


def WrtieExcelSheet(workbook, sheet_name, a, count):
    sheet = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
    leng = 0  # 每段对话的起始行号
    for i in range(0, count, 2):
        leng1 = len(a[i][3])  # 选项1后续行号
        leng2 = len(a[i + 1][3])  # 选项2后续行号
        length = max(leng1, leng2)
        sheet.write(leng, 0, a[i][1])
        sheet.write(leng, 1, a[i][2])
        sheet.write(leng, 2, a[i + 1][2])
        for j in range(leng1):
            sheet.write(leng + j + 1, 1, a[i][3][j])
        for k in range(leng2):
            sheet.write(leng + k + 1, 2, a[i+1][3][k])
        leng += length + 1


count = 1
data = GetDataFromTable(r'C:\Users\Administrator\Desktop\1.xlsx')
workbook = xlwt.Workbook()
WrtieExcelSheet(workbook, 'Sheet1', data, count)
workbook.save(r'2.xls')
