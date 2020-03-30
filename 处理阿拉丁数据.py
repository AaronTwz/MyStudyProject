import xlrd
import xlsxwriter
import csv


# csv转xlsx
def csv_to_xlsx(csvFile):
    with open(csvFile, 'r', encoding='gbk') as f:
        read = csv.reader(f)
        workbook = xlsxwriter.Workbook(filePath + fileName + '.xlsx')
        sheet = workbook.add_worksheet('sheet1')  # 创建一个sheet表格
        l = 0
        for line in read:
            r = 0
            for i in line:
                print(i)
                sheet.write(l, r, i)
                r = r + 1
            l = l + 1
        workbook.close()
        print('转excel完毕！')


# 读取文件
event = []  # 触发事件名称
UserNum = []  # 触发人数
triggerTimes = []  # 总触发次数
triggerTimesPU = []  # 人均触发次数


def getDataFromCsv(csvFile):
    with open(csvFile, 'r', encoding='gbk') as f:
        read = csv.reader(f)
        for line in read:
            if (line[1] == '事件名称'):
                continue
            event.append(line[1])
            UserNum.append(line[3])
            triggerTimes.append(line[4])
            triggerTimesPU.append(line[5])


# 处理数据
buyFood = []  # '成功购买餐品'
buyFoodAD = []  # '成功看广告购买餐品'
buyFacility = []  # '成功购买设施'
buyFacilityAD = []  # '成功看广告购买设施'
turnTableOpen = []  # 大转盘打开
turnTableClose = []  # 大转盘关闭
turnTableFree = []  # 大转盘免费
turnTableShare = []  # 大转盘分享
turnTableAD = []  # 大转盘广告
turnTableSingleReward = []  # 大转盘单份奖励
turnTableDoubleReward = []  # 大转盘双倍奖励
gotoLeft = []  # 点击 前台_向左切场景
gotoRight = []  # 点击 后厨_向右切场景
upgradeOpen = []  # 点击餐厅升级
upgradeClose = []  # 点击餐厅升级-关闭
upgradeFac = []  # 点击餐厅升级-设施
upgradeFood = []  # 点击餐厅升级-食品
achieveOpen = []  # 点击成就界面
fireCatClick = []  # 点击后厨_解雇
buyCatFromStore = []  # 点击后厨_商店购买:10级猫咪
buyCatFromStoreSuccess = []  # 点击后厨_商店购买:10级猫咪成功
buyCatFromRecruit = []  # 点击后厨_招聘:10级猫咪
buyCatFromRecruitSuccess = []  # 点击后厨_招聘:10级猫咪成功
buyCatFromRecruitFailed = []  # 点击后厨_招聘:10级猫咪鱼干不足
catStoreClose = []  # 点击猫咪商店_关闭
dailyTaskClick = []  # 点击每日任务界面
getBarGold = []  # 点击前台_吧台金币
getPianoGold = []  # 点击前台_钢琴金币
getCashGold = []  # 点击前台_收银台金币
piggyBankClick = []  # 点击前台-储蓄罐
propagandaUpgradeClick = []  # 点击前台_宣传升级
propagandaADClick = []  # 点击前台-顶级流量宣传
propagandaClick = []  # 点击前台-宣传
facDetailsClose = []  # 点击设施详情弹窗-关闭
foodDetailsClose = []  # 点击食品详情弹窗-关闭
handbookClick = []  # 点击图鉴
handbookClose = []  # 点击图鉴-关闭
handbookCus = []  # 点击图鉴-客人界面
handbookOrn = []  # 点击图鉴-饰品界面
catLvUp = []  # 合出猫咪：10级
fireCat = []  # 解雇猫咪：9级
getCusFromSeniorProp = []  # 看广告获得20名客人
getDailyTaskID = []  # 每日任务任务id:1
compliteDailyTaskID = []  # 每日任务完成任务id:1
getCusFromAD = []  # 双倍领取 广告宣传 奖励
offlineFishSingleReward = []  # 直接领取 上线的离线鱼干奖励 奖励
offlineFishDoubleReward = []  # 双倍领取 上线的离线鱼干奖励 奖励
getFishFromAD = []  # 双倍领取 鱼干不足 奖励
commonSingleReward = []  # 直接领取 双倍奖励 奖励
commonDoubleReward = []  # 双倍领取 双倍奖励 奖励


def importData():
    for i in range(len(event)):
        text = event[i]
        keyword = '成功购买餐品'
        if text.startswith(keyword):
            try:
                endindex = text.index('-')
            except:
                endindex = None
            buyFood.append([event[i][len(keyword) + 1:endindex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '成功看广告购买餐品'
        if text.startswith(keyword):
            try:
                endindex = text.index('-')
            except:
                endindex = None
            buyFoodAD.append(
                [event[i][(len(keyword) + 1):endindex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '成功购买设施'
        if text.startswith(keyword):
            try:
                endindex = text.index('-')
            except:
                endindex = None
            buyFacility.append(
                [event[i][len(keyword) + 1:endindex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '成功看广告购买设施'
        if text.startswith(keyword):
            try:
                endindex = text.index('-')
            except:
                endindex = None
            buyFacilityAD.append(
                [event[i][len(keyword) + 1:endindex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '大转盘-打开'
        if text == keyword:
            turnTableOpen.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '大转盘-关闭'
        if text == keyword:
            turnTableClose.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '大转盘-免费触发'
        if text == keyword:
            turnTableFree.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '大转盘-分享后触发'
        if text == keyword:
            turnTableShare.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '大转盘-广告后触发'
        if text == keyword:
            turnTableAD.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '大转盘-直接领奖'
        if text == keyword:
            turnTableSingleReward.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '大转盘-翻倍奖励'
        if text == keyword:
            turnTableDoubleReward.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击 前台_向左切场景'
        if text == keyword:
            gotoLeft.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击 后厨_向右切场景'
        if text == keyword:
            gotoRight.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击餐厅升级'
        if text == keyword:
            upgradeOpen.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击餐厅升级-关闭'
        if text == keyword:
            upgradeClose.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击餐厅升级-设施'
        if text == keyword:
            upgradeFac.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击餐厅升级-食品'
        if text == keyword:
            upgradeFood.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击成就界面'
        if text == keyword:
            achieveOpen.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击后厨_解雇'
        if text == keyword:
            fireCatClick.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击后厨_商店购买'
        startIndex = len(keyword) + 1
        if text.startswith(keyword):
            endIndex = text.index('级')
            if text.endswith('成功'):
                buyCatFromStoreSuccess.append(
                    [text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            else:
                buyCatFromStore.append([text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击后厨_招聘'
        startIndex = len(keyword) + 1
        if text.startswith(keyword):
            endIndex = text.index("级")
            if text.endswith('成功'):
                buyCatFromRecruitSuccess.append(
                    [text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            elif text.endswith('不足'):
                buyCatFromRecruitFailed.append(
                    [text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            else:
                buyCatFromRecruit.append(
                    [text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击猫咪商店_关闭'
        if text == keyword:
            catStoreClose.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击每日任务界面'
        if text == keyword:
            dailyTaskClick.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击前台_吧台金币'
        if text == keyword:
            getBarGold.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击前台_钢琴金币'
        if text == keyword:
            getPianoGold.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击前台_收银台金币'
        if text == keyword:
            getCashGold.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击前台-储蓄罐'
        if text == keyword:
            piggyBankClick.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击前台_宣传升级'
        if text == keyword:
            propagandaUpgradeClick.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击前台-顶级流量宣传'
        if text == keyword:
            propagandaADClick.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击前台-宣传'
        if text == keyword:
            propagandaClick.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击设施详情弹窗-关闭'
        if text == keyword:
            facDetailsClose.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击食品详情弹窗-关闭'
        if text == keyword:
            foodDetailsClose.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击图鉴'
        if text == keyword:
            handbookClick.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击图鉴-关闭'
        if text == keyword:
            handbookClose.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击图鉴-客人界面'
        if text == keyword:
            handbookCus.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '点击图鉴-饰品界面'
        if text == keyword:
            handbookOrn.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '合出猫咪'
        startIndex = len(keyword) + 1
        if text.startswith(keyword):
            catLvUp.append([text[startIndex:-1], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '解雇猫咪'
        startIndex = len(keyword) + 1
        if text.startswith(keyword):
            fireCat.append([text[startIndex:-1], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '每日任务任务id'
        startIndex = len(keyword) + 1
        if text.startswith(keyword):
            if text[startIndex] == '4':
                endIndex = text.index('特殊')
                j = 0
                for task in getDailyTaskID:
                    if text[startIndex:endIndex] == task[0]:
                        task[1] = int(task[1]) + int(UserNum[i])
                        task[2] = int(task[2]) + int(triggerTimes[i])
                        task[3] = float(task[3]) + float(triggerTimesPU[i])
                        break
                    j += 1
                if j >= len(getDailyTaskID):
                    getDailyTaskID.append([text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            elif text[startIndex] == '8':
                endIndex = text.index('猫咪')
                j = 0
                for task in getDailyTaskID:
                    if text[startIndex:endIndex] == task[0]:
                        task[1] = int(task[1]) + int(UserNum[i])
                        task[2] = int(task[2]) + int(triggerTimes[i])
                        task[3] = float(task[3]) + float(triggerTimesPU[i])
                        break
                    j += 1
                if j >= len(getDailyTaskID):
                    getDailyTaskID.append([text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            else:
                getDailyTaskID.append([text[startIndex:], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '每日任务完成任务id'
        startIndex = len(keyword) + 1
        if text.startswith(keyword):
            if text[startIndex] == '4':
                endIndex = text.index('特殊')
                j = 0
                for task in compliteDailyTaskID:
                    if text[startIndex:endIndex] == task[0]:
                        task[1] = int(task[1]) + int(UserNum[i])
                        task[2] = int(task[2]) + int(triggerTimes[i])
                        task[3] = float(task[3]) + float(triggerTimesPU[i])
                        break
                    j += 1
                if j >= len(compliteDailyTaskID):
                    compliteDailyTaskID.append(
                        [text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            elif text[startIndex] == '8':
                endIndex = text.index('猫咪')
                j = 0
                for task in compliteDailyTaskID:
                    if text[startIndex:endIndex] == task[0]:
                        task[1] = int(task[1]) + int(UserNum[i])
                        task[2] = int(task[2]) + int(triggerTimes[i])
                        task[3] = float(task[3]) + float(triggerTimesPU[i])
                        break
                    j += 1
                if j >= len(compliteDailyTaskID):
                    compliteDailyTaskID.append(
                        [text[startIndex:endIndex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            else:
                compliteDailyTaskID.append([text[startIndex:], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '看广告获得20名客人'
        if text == keyword:
            getCusFromSeniorProp.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '双倍领取 广告宣传 奖励'
        if text == keyword:
            getCusFromAD.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '直接领取 上线的离线鱼干奖励 奖励'
        if text == keyword:
            offlineFishSingleReward.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '双倍领取 上线的离线鱼干奖励 奖励'
        if text == keyword:
            offlineFishDoubleReward.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '双倍领取 鱼干不足 奖励'
        if text == keyword:
            getFishFromAD.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '直接领取 双倍奖励 奖励'
        if text == keyword:
            commonSingleReward.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue

        keyword = '双倍领取 双倍奖励 奖励'
        if text == keyword:
            commonDoubleReward.append([keyword, UserNum[i], triggerTimes[i], triggerTimesPU[i]])
            continue


# 根据映射表读取ID
def getMap(fName):
    fPath = 'C:/Users/Administrator/Desktop/Aladdin/'
    excelfile = fPath + fName + '.xlsx'
    workbook = xlrd.open_workbook(excelfile)
    sheet1 = workbook.sheet_by_index(0)
    NameList = sheet1.col_values(1, 3)
    return NameList


# 比对替换
def replaceByID(NameList, searchList):
    for unit in searchList:
        for Name in NameList:
            if unit[0] == Name:
                unit[0] = NameList.index(Name) + 1
                break


# 通用数据导出
def outputDataCommon(workbook):
    commonDataList = [turnTableOpen, turnTableClose, turnTableFree, turnTableShare, turnTableAD, turnTableSingleReward,
                      turnTableDoubleReward, gotoLeft, gotoRight, upgradeOpen, upgradeClose, upgradeFac, upgradeFood,
                      achieveOpen, fireCatClick, catStoreClose, dailyTaskClick, getBarGold, getPianoGold, getCashGold,
                      piggyBankClick, propagandaUpgradeClick, propagandaADClick, propagandaClick, facDetailsClose,
                      foodDetailsClose, handbookClick, handbookClose, handbookCus, handbookOrn, getCusFromSeniorProp,
                      getCusFromAD, offlineFishSingleReward, offlineFishDoubleReward, getFishFromAD, commonSingleReward,
                      commonDoubleReward]
    sheetData = workbook.add_worksheet('通用数据')
    titleList = ['触发事件名称', '触发人数', '总触发次数', '人均触发次数']
    sheetData.write_row(0, 0, titleList)
    for title in titleList:
        sheetData.set_column(titleList.index(title), titleList.index(title), len(title) * 2.075)
    sheetData.set_column(0, 0, 34)
    rowNum = 0
    for commonData in commonDataList:
        rowNum += 1
        sheetData.write(rowNum, 0, commonData[0][0])
        sheetData.write(rowNum, 1, int(commonData[0][1]))
        sheetData.write(rowNum, 2, int(commonData[0][2]))
        sheetData.write(rowNum, 3, float(commonData[0][3]))


# 分析数据
def analayseFoodData(workbook):
    sheetData = workbook.add_worksheet('购买食物')
    titleList = ['购买ID', '购买触发人数', '看广告购买触发人数', '购买人均次数', '看广告购买人均次数']
    sheetData.write_row(0, 0, titleList)
    for title in titleList:
        sheetData.set_column(titleList.index(title), titleList.index(title), len(title) * 2.075)
    for i in range(len(foodNameList)):
        i += 1
        sheetData.write(i, 0, i)
        buyFood.sort()
        for food in buyFood:
            if int(food[0]) == i:
                sheetData.write(i, 1, int(food[1]))
                sheetData.write(i, 3, float(food[3]))
                break
        buyFoodAD.sort()
        for food in buyFoodAD:
            if int(food[0]) == i:
                sheetData.write(i, 2, int(food[1]))
                sheetData.write(i, 4, float(food[3]))
                break


def analayseFacilityData(workbook):
    sheetData = workbook.add_worksheet('购买设施')
    titleList = ['购买ID', '购买触发人数', '看广告购买触发人数', '购买人均次数', '看广告购买人均次数']
    sheetData.write_row(0, 0, titleList)
    for title in titleList:
        sheetData.set_column(titleList.index(title), titleList.index(title), len(title) * 2.075)
    for i in range(len(facNameList)):
        i += 1
        sheetData.write(i, 0, i)
        buyFacility.sort()
        for fac in buyFacility:
            if int(fac[0]) == i:
                sheetData.write(i, 1, int(fac[1]))
                sheetData.write(i, 3, float(fac[3]))
                break
        buyFacilityAD.sort()
        for fac in buyFacilityAD:
            if int(fac[0]) == i:
                sheetData.write(i, 2, int(fac[1]))
                sheetData.write(i, 4, float(fac[3]))
                break


def analayseCatFromRecruitData(workbook):
    sheetData = workbook.add_worksheet('购买猫咪')
    titleList = ['购买ID', '购买人数', '购买成功人数', '鱼干不足人数', '购买人均次数', '购买成功人均次数', '鱼干不足人均次数', '', '商店购买人数', '商店购买成功人数',
                 '商店购买人均人数', '商店购买成功人均人数']
    sheetData.write_row(0, 0, titleList)
    for title in titleList:
        sheetData.set_column(titleList.index(title), titleList.index(title), len(title) * 2.075)
    for i in range(50):
        i += 1
        sheetData.write(i, 0, i)
        buyCatFromRecruit.sort()
        for j in buyCatFromRecruit:
            if int(j[0]) == i:
                sheetData.write(i, 1, int(j[1]))
                sheetData.write(i, 4, float(j[3]))
                break
        buyCatFromRecruitSuccess.sort()
        for j in buyCatFromRecruitSuccess:
            if int(j[0]) == i:
                sheetData.write(i, 2, int(j[1]))
                sheetData.write(i, 5, float(j[3]))
                break
        buyCatFromRecruitFailed.sort()
        for j in buyCatFromRecruitFailed:
            if int(j[0]) == i:
                sheetData.write(i, 3, int(j[1]))
                sheetData.write(i, 6, float(j[3]))
                break
        buyCatFromStore.sort()
        for j in buyCatFromStore:
            if int(j[0]) == i:
                sheetData.write(i, 8, int(j[1]))
                sheetData.write(i, 10, float(j[3]))
                break
        buyCatFromStoreSuccess.sort()
        for j in buyCatFromStoreSuccess:
            if int(j[0]) == i:
                sheetData.write(i, 9, int(j[1]))
                sheetData.write(i, 11, float(j[3]))
                break


def analaysecatLvUpData(workbook):
    sheetData = workbook.add_worksheet('合出猫咪')
    titleList = ['ID', '合出人数', '合出总次数', '合出人均次数']
    sheetData.write_row(0, 0, titleList)
    for title in titleList:
        sheetData.set_column(titleList.index(title), titleList.index(title), len(title) * 2.075)
    for i in range(50):
        i += 1
        sheetData.write(i, 0, i)
        catLvUp.sort()
        for j in catLvUp:
            if int(j[0]) == i:
                sheetData.write(i, 1, int(j[1]))
                sheetData.write(i, 2, int(j[2]))
                sheetData.write(i, 3, float(j[3]))
                break


def analaysefireCatData(workbook):
    sheetData = workbook.add_worksheet('解雇猫咪')
    titleList = ['ID', '解雇人数', '解雇总次数', '解雇人均次数']
    sheetData.write_row(0, 0, titleList)
    for title in titleList:
        sheetData.set_column(titleList.index(title), titleList.index(title), len(title) * 2.075)
    for i in range(50):
        i += 1
        sheetData.write(i, 0, i)
        fireCat.sort()
        for j in fireCat:
            if int(j[0]) == i:
                sheetData.write(i, 1, int(j[1]))
                sheetData.write(i, 2, int(j[2]))
                sheetData.write(i, 3, float(j[3]))
                break


def analayseDailyTaskData(workbook):
    sheetData = workbook.add_worksheet('每日任务')
    titleList = ['ID', '触发人数', '完成人数', '触发人均次数', '完成人均次数']
    sheetData.write_row(0, 0, titleList)
    for title in titleList:
        sheetData.set_column(titleList.index(title), titleList.index(title), len(title) * 2.075)

    # 添加文本备注
    fPath = 'C:/Users/Administrator/Desktop/Aladdin/'
    excelfile = fPath + 'DailyTask' + '.xlsx'
    workbook = xlrd.open_workbook(excelfile)
    sheet1 = workbook.sheet_by_index(0)
    NameList = sheet1.col_values(3, 3)

    for i in range(len(facNameList)):
        i += 1
        sheetData.write(i, 0, i)
        getDailyTaskID.sort()
        for j in getDailyTaskID:
            if int(j[0]) == i:
                sheetData.write(i, 1, int(j[1]))
                sheetData.write(i, 3, float(j[3]))
                sheetData.write(i, 5, NameList[i - 1])
                break
        compliteDailyTaskID.sort()
        for j in compliteDailyTaskID:
            if int(j[0]) == i:
                sheetData.write(i, 2, int(j[1]))
                sheetData.write(i, 4, float(j[3]))
                break


def analayseData(workbook):
    analayseFoodData(workbook)
    analayseFacilityData(workbook)
    analayseCatFromRecruitData(workbook)
    analaysecatLvUpData(workbook)
    analaysefireCatData(workbook)
    analayseDailyTaskData(workbook)
    outputDataCommon(workbook)


# 处理单个数据表
def makeExcel(file, outfile):
    # 从后台得到csv文件
    getDataFromCsv(file)
    # 将文件数据以模块的形式导入内存
    importData()
    replaceByID(foodNameList, buyFood)
    replaceByID(foodNameList, buyFoodAD)
    replaceByID(facNameList, buyFacility)
    replaceByID(facNameList, buyFacilityAD)
    # 将分类好的数据导出
    workbook = xlsxwriter.Workbook(outfile)
    analayseData(workbook)
    workbook.close()


if __name__ == '__main__':
    # 将道具名称转换为ID
    foodNameList = getMap('Food')
    facNameList = getMap('Facilities')
    # 文件列表
    filePath = 'C:/Users/Administrator/Desktop/Aladdin/'
    fileNameList = ['事件分析-2020-03-26_2020-03-26', '事件分析-2020-03-27_2020-03-27', '事件分析-2020-03-28_2020-03-28',
                    '事件分析-2020-03-29_2020-03-29']
    for fileName in fileNameList:
        file = filePath + fileName + '.csv'
        outfile = filePath + fileName + '.xlsx'
        makeExcel(file, outfile)
    print('处理完成！')
