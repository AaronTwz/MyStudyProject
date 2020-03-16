import xlrd
import xlsxwriter
import csv

# 文件列表
filePath = 'C:/Users/Administrator/Desktop/Aladdin/'
fileName = '事件分析-2020-03-06_2020-03-12'
file = filePath + fileName + '.csv'


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
                [event[i][len(keyword + 1) + 1:endindex], UserNum[i], triggerTimes[i], triggerTimesPU[i]])
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
def outputDataCommon(wookbook):
    commonDataList = [turnTableOpen, turnTableClose, turnTableFree, turnTableShare, turnTableAD, turnTableSingleReward,
                      turnTableDoubleReward, gotoLeft, gotoRight, upgradeOpen, upgradeClose, upgradeFac, upgradeFood,
                      achieveOpen, fireCatClick, catStoreClose, dailyTaskClick, getBarGold, getPianoGold, getCashGold,
                      piggyBankClick, propagandaUpgradeClick, propagandaADClick, propagandaClick, facDetailsClose,
                      foodDetailsClose, handbookClick, handbookClose, handbookCus, handbookOrn, getCusFromSeniorProp,
                      getCusFromAD, offlineFishSingleReward, offlineFishDoubleReward, getFishFromAD, commonSingleReward,
                      commonDoubleReward]
    sheet_commonData = wookbook.add_sheet('通用数据')


# 分析数据
def analayseData():
    return 1


# 主函数
if __name__ == '__main__':
    # 从后台得到csv文件
    getDataFromCsv(file)
    # 将文件数据以模块的形式导入内存
    importData()
    # 将道具名称转换为ID
    foodNameList = getMap('Food')
    facNameList = getMap('Facilities')
    replaceByID(foodNameList, buyFood)
    replaceByID(foodNameList, buyFoodAD)
    replaceByID(facNameList, buyFacility)
    replaceByID(facNameList, buyFacilityAD)
    # 将分类好的数据导出

    print('处理完成！')
