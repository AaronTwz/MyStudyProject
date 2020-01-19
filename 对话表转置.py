import xlwt, xlrd


def GetDataFromTable_Common(file_name, index=0, startline=1):
    xlFile = xlrd.open_workbook(file_name)
    sheet = xlFile.sheets()[index]

    # 获取行列数
    rowNum = sheet.nrows
    colNum = sheet.ncols
    print("表格：%s   行数：%d   列数：%d" % (file_name, rowNum, colNum))

    # 获取全页信息（注意从第1行获取还是第0行获取！！！）
    row_list = list()
    for perRow in range(startline, rowNum, 1):
        perRowList = []
        for perCol in range(colNum):
            perRowList.append(sheet.cell(perRow, perCol).value)
        row_list.append(perRowList)
    return row_list


def writeChoice(sheet, row, col, seqID):
    diaList_1 = indexDict[seqDict[seqID][0]]
    sheet.write(row, col, seqDict[seqID][2])
    diaList_2 = indexDict[seqDict[seqID][1]]
    sheet.write(row, col + 1, seqDict[seqID][3])

    leng = max(len(diaList_1), len(diaList_2))
    global line
    line += leng

    for d_1 in range(len(diaList_1) - 1):
        sheet.write(row + d_1 + 1, col, dialogDict[diaList_1[d_1]])
        sheet.write(row + d_1 + 1, colline + 2, personDict[diaList_1[d_1]])  # 对应姓名
    for d_2 in range(len(diaList_2) - 1):
        sheet.write(row + d_2 + 1, col + 1, dialogDict[diaList_2[d_2]])
        sheet.write(row + d_2 + 1, colline + 3, personDict[diaList_2[d_2]])  # 对应姓名
    if diaList_1[-1] == 'E':
        sheet.write(row + len(diaList_1), col, 'E')
        sheet.write(row + len(diaList_2), col + 1, 'E')
    else:
        writeChoice(sheet, line, col, diaList_1[-1])


workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet1", cell_overwrite_ok=True)

inFile = r'C:\Users\Administrator\Desktop\1.xlsx'
outFile = r'C:\Users\Administrator\Desktop\2.xls'
data0 = GetDataFromTable_Common(inFile, 0)  # 对白内容
data1 = GetDataFromTable_Common(inFile, 1)  # 有选项对白ID对应对白内容id
data2 = GetDataFromTable_Common(inFile, 2)  # 索引id（来自关卡）对应对白内容id
data3 = GetDataFromTable_Common(inFile, 3)  # 关卡id对应索引id
data4 = GetDataFromTable_Common(inFile, 4)  # 对白id对应说话的人id
data5 = GetDataFromTable_Common(inFile, 5)  # 说话人的名字

# 对白字典
dialogDict = dict()
for i in range(len(data0)):
    a = data0[i][0]
    if type(a) == float:
        a = str(int(a))
    dialogDict[a] = data0[i][1]

# ID到Seq对应成字典:key=ID ,val = [选项一ID，选项二ID]
seqDict = {}
for j in range(len(data1)):
    seqDict[data1[j][0]] = [data1[j][1], data1[j][2], data1[j][3], data1[j][4]]

# 索引字典
indexDict = dict()
for k in range(len(data2)):
    indexDict[data2[k][0]] = data2[k][1].split(',')

# 说话的人是谁
nameDict = dict()
for i in range(len(data5)):
    nameDict[data5[i][0]] = data5[i][1]

personDict = dict()
for i in range(len(data4)):
    personName = ''
    if data4[i][2] == 1:
        personName = nameDict[data4[i][1]]
    elif data4[i][4] == 1:
        personName = nameDict[data4[i][3]]
    elif data4[i][6] == 1:
        personName = nameDict[data4[i][5]]

    a = data4[i][0]
    if type(a) == float:
        a = str(int(a))
    personDict[a] = personName

line = 1  # 累积行数
for i in range(len(data3)):
    colline = 2  # 累积列数
    sheet.write(line, 0, data3[i][0])
    sheet.write(line, 1, data3[i][1])
    if data3[i][2] == 0:
        sheet.write(line, 2, "无剧情对白")
    else:
        diaList = indexDict[data3[i][2]]
        leng = len(diaList)  # 本次增加的长度
        for idx in range(leng - 1):
            sheet.write(line + idx + 1, colline, dialogDict[diaList[idx]])  # 写链式剧情
            sheet.write(line + idx + 1, colline + 2, personDict[diaList[idx]])  # 对应姓名
        line += leng
        # 写结尾符或者分支剧情
        if diaList[-1] == 'E':
            sheet.write(line, 2, 'E')
        else:
            writeChoice(sheet, line, colline, diaList[-1])

    if data3[i][3] == 0:
        sheet.write(line + 1, 2, "无胜利对白")
    else:
        diaList = indexDict[data3[i][3]]
        leng = len(diaList)  # 本次增加的长度
        for idx in range(leng - 1):
            sheet.write(line + idx + 1, colline, dialogDict[diaList[idx]])  # 写链式剧情
            sheet.write(line + idx + 1, colline + 2, personDict[diaList[idx]])  # 对应姓名
        line += leng
        # 写结尾符或者分支剧情
        if diaList[-1] == 'E':
            sheet.write(line, 2, 'E')
        else:
            writeChoice(sheet, line, colline, diaList[-1])
    line += 2

workbook.save(outFile)
