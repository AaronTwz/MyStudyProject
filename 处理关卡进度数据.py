import xlrd, datetime, xlwt, json


# 需要比对的玩家id列表
def GetIdList(data, index):
    id_list = set()
    for i in data:
        id_list.add(i[index])

    # print(id_list)
    return id_list


def GetDataFromTable_Common(file_name):
    xlFile = xlrd.open_workbook(file_name)
    sheet1 = xlFile.sheets()[0]
    DateMode = xlFile.datemode

    # 获取行列数
    rowNum = sheet1.nrows
    colNum = sheet1.ncols
    print("表格：%s   行数：%d   列数：%d" % (file_name, rowNum, colNum))

    # 获取字段名
    ArgName_list = []
    for perCol in range(colNum):
        ArgName = sheet1.cell(0, perCol).value
        ArgName_list.append(ArgName)

    # 获取全页信息
    row_list = list()

    for perRow in range(1, rowNum, 1):
        perRow_dict = dict()
        for perCol in range(colNum):
            perRow_dict[ArgName_list[perCol]] = sheet1.cell(perRow, perCol).value
        row_list.append(perRow_dict)

    return row_list


def WrtieExcelSheet(workbook, sheet_name, data, title_list):
    sheet1 = workbook.add_sheet(sheet_name, cell_overwrite_ok=True)
    for k in range(len(title_list)):
        sheet1.write(0, k, title_list[k])

    for i in range(1, len(data), 1):
        for j in range(len(data[i])):
            sheet1.write(i, j, data[i][j])


def GetDataFromTable(file_name):
    # 读取excel
    loginFile = xlrd.open_workbook(file_name)
    sheet1 = loginFile.sheets()[0]
    datemode = loginFile.datemode

    # 获取行数
    row_list = []
    rowNum = sheet1.nrows
    print(rowNum)

    # 获取每行内容
    for row in range(1, rowNum, 1):
        PlayerID = str(int(sheet1.cell(row, 0).value))
        MissionType = int(sheet1.cell(row, 1).value)
        MissionID = int(sheet1.cell(row, 2).value)
        if sheet1.cell(row, 3).ctype == 3:
            BattleTime = TimeTranslator(sheet1.cell(row, 3).value, datemode)
        IsPass = int(sheet1.cell(row, 4).value)

        row_list.append([PlayerID, MissionType, MissionID, BattleTime, IsPass])
    return row_list


def TimeTranslator(timeNum, datemode):
    year, month, day, hour, minute, second = xlrd.xldate_as_tuple(timeNum, datemode)
    Time = datetime.datetime(year, month, day, hour, minute, second)
    return Time


def GetOnLineTime(lst):
    Time = datetime.datetime.strptime("1900/01/01 00:00:00", '%Y/%m/%d %H:%M:%S')
    for i in range(1, len(lst), 2):
        time = lst[i] - lst[i - 1]
        Time += time

    # print(Time.time())
    return Time

# 从InPut导入data的list，和str类型的日期
def deal(Data, date):
    # date = "1019"
    # day = 04
    # inputfile = r'C:\Users\Administrator\Desktop\数据\%s关卡数据.xlsx' % (date)
    outfile = r'C:\Users\Administrator\Desktop\数据\关卡输出%s.xls' % date

    # Data = GetDataFromTable(inputfile)

    # 加载所有玩家列表
    PlayerID_list = GetIdList(Data, 0)

    # 加载所有关卡列表
    MissionID_list = []
    MissionID_List = GetDataFromTable_Common(r'C:\Users\Administrator\Desktop\数据\level.xlsx')
    for MissionID_dict in MissionID_List:
        MissionID = int(MissionID_dict["ID"])
        MissionID_list.append(MissionID)

    out_list = list()

    # 最后停留在此关的人数
    Player_content_list = []
    for PlayerID in PlayerID_list:
        Player_LastMission = 0
        LastTime = datetime.datetime.strptime("1900/01/01 00:00:00", '%Y/%m/%d %H:%M:%S')
        for data in Data:
            if data[0] == PlayerID:
                if data[3] > LastTime:
                    LastTime = data[3]
                    Player_LastMission = data[2]
        Player_content_list.append([PlayerID, Player_LastMission])

    for MissionID in MissionID_list:
        # 参与次数、通关次数、通关率、参与人数、最后停留在此关的人数
        join_times = 0
        pass_times = 0
        join_people = 0
        end_people = 0

        PlayerID_set = []
        for data in Data:
            # 参与次数
            if data[2] == MissionID:
                join_times += 1
                # 通过次数
                if data[4] == 1:
                    pass_times += 1
                # 参与人数
                if data[0] not in PlayerID_set:
                    PlayerID_set.append(data[0])
                    join_people += 1

        for Player_content in Player_content_list:
            if Player_content[1] == MissionID:
                end_people += 1

        if join_times == 0:
            passRate = 0
        else:
            passRate = float(pass_times / join_times)

        out_list.append([MissionID, join_times, pass_times, passRate, join_people, end_people])

    workbook = xlwt.Workbook()
    title_list = ["关卡ID", "参与次数", "通关次数", "通关率", "参与人数", "最后停留在此关的人数"]
    WrtieExcelSheet(workbook, "sheet1", out_list, title_list)
    workbook.save(outfile)

    print("输出完成")

