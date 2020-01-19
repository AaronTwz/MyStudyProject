import json
import pymysql
import io
import 处理关卡进度数据

accountServer = "123456.com"
accountroot = "123_root"
accountpassword = "123"
db_name = "123"

##开始时间
year = 2019
month = 10
date = 15

##结束时间
end_year = 2019
end_month = 10
end_date = 16

starttime = str(year) + "-" + str(month) + "-" + str(date)
endtime = str(end_year) + "-" + str(end_month) + "-" + str(end_date)

data = []


def update_roleinfo():
    dbcff = pymysql.connect(accountServer, accountroot, accountpassword, db_name, charset='utf8')
    sql = "SELECT roles.id, `logs`.Type, logs.`Arg2`, FROM_UNIXTIME(logs.`Logtime`),`logs`.Arg3 FROM LOGS, roles WHERE logs.`Arg1` = roles.`ID` AND (roles.`CreateTime` >= UNIX_TIMESTAMP('%s') AND roles.`CreateTime` < UNIX_TIMESTAMP('%s')) AND `logs`.Type IN (10,11,19,12,13,23,20,21,22,24); " % (
        starttime, endtime)
    cursor = dbcff.cursor()
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        data.append([row[0], row[1], row[2], row[3], row[4]])

    return data

def wirteData():
    with io.open('copy.json', 'w', encoding='utf-8') as fa:  # 使用.dumps()方法时，要写入
        for i in data:
            json_str = json.dumps(i)
            fa.write(u'{}\n'.format(json_str))


data = update_roleinfo()
处理关卡进度数据.deal(data, starttime)

print("success")
