import re, requests, json, time
import lxml.html


def 登录账号(连接, 头文件):
    登录链接 = 'https://www.taptap.com/auth/email/login'
    获取登录信息 = 连接.get(登录链接, headers=头文件)
    token正则表达式 = r'<meta name="csrf-token" content="(.*?)">'
    token正则表达式对象 = re.compile(token正则表达式, re.S)
    token = re.findall(token正则表达式对象, 获取登录信息.text)

    账号密码 = {
        '_token': token[0],
        'email': '1234567@qq.com',
        'password': '123'
    }
    连接.post(登录链接, data=账号密码)
    print('登录完成……')


def 获取一个网页(连接, 链接, 头文件):
    响应 = 连接.get(链接, headers=头文件)
    if 响应.status_code == 200:
        # print('网页 %s 信息获取成功……' % 链接)
        return 响应.text
    print('获取网页 %s 失败！' % 链接)
    return None


def 解析玩家信息的html文本(html文本, 玩家id, 创建文件):
    etree = lxml.html.etree
    text = etree.HTML(html文本.encode('utf-8'))
    玩家玩过最多的游戏 = text.xpath('//div[contains(@id,"most-played")]//li/@id')

    for 每款游戏 in 玩家玩过最多的游戏:
        游戏id = int(str(每款游戏).replace('\\\"', '')[7:])

        游戏名称 = text.xpath('//div[contains(@id,"most-played")]//li[@id="played-%d"]/div/h2/a/text()' % 游戏id)
        if 游戏名称 != []:
            游戏名称 = 游戏名称[0]
        else:
            游戏名称 = text.xpath('//div[contains(@id,"most-played")]//li[@id="played-%d"]/div/h2/text()' % 游戏id)[
                0]

        # 游戏评分 = text.xpath(
        #     '//div[contains(@id,"most-played")]//li[contains(@id,"played-%d")]/div/span[contains(@class,"app-score")]/text()' % 游戏id)
        # if 游戏评分 != []:
        #     游戏评分 = 游戏评分[0]
        # else:
        #     游戏评分 = 0

        游戏时长 = text.xpath(
            '//div[contains(@id,"most-played")]//li[@id="played-%d"]/div/span[contains(@class,"play_time")]/text()' % 游戏id)
        if 游戏时长 != []:
            游戏时长 = 游戏时长[0][4:]
        else:
            游戏时长 = 0

        写入内容 = "%d,%s,%s,%s" % (玩家id, 游戏id, 游戏名称, 游戏时长)
        创建文件.write(json.dumps(写入内容, ensure_ascii=False) + "\n")


def 获取玩家id列表(游戏id, 连接, 头文件):
    创建文件 = open('游戏id：%d的玩家id.txt' % 游戏id, 'a', encoding='utf-8')
    创建文件1 = open('游戏id：%d的玩家手机型号.txt' % 游戏id, 'a', encoding='utf-8')
    创建文件.seek(0)
    创建文件.truncate()
    创建文件1.seek(0)
    创建文件1.truncate()

    链接 = 'https://www.taptap.com/app/%d/review?order=default&page=1#review-list' % 游戏id
    html文本 = 获取一个网页(连接, 链接, 头文件)
    etree = lxml.html.etree
    游戏首页 = etree.HTML(html文本.encode('utf-8'))
    评论数 = int(游戏首页.xpath('//a[@data-taptap-tab="review"]/small/text()')[0])
    社区贴数 = int(游戏首页.xpath('//a[@data-taptap-tab="topic"]/small/text()')[0])
    print("游戏id：%d,评论数:%d,社区贴数:%d" % (游戏id, 评论数, 社区贴数))
    page = max(min(int(评论数 / 20), 500), 1)

    玩家id列表 = []
    for 页码 in range(page):
        startTime = time.time()
        print('获取第%d/%d页玩家列表……' % ((页码 + 1), page))
        链接 = 'https://www.taptap.com/app/%d/review?order=default&page=%d#review-list' % (游戏id, (页码 + 1))
        html = 获取一个网页(连接, 链接, 头文件)
        if html != None:
            评论网页 = etree.HTML(html.encode('utf-8'))
            单页玩家id列表 = 评论网页.xpath(
                '//ul[@id="reviewsList"]/li[@class="taptap-review-item collapse in"]/div[@class="review-item-text "]/div[@class="item-text-header"]/span/@data-user-id')
            单页手机型号列表 = 评论网页.xpath(
                '//ul[@id="reviewsList"]/li[@class="taptap-review-item collapse in"]/div[@class="review-item-text "]/div[@class="item-text-footer"]/span[@class="text-footer-device"]/text()')

            for 玩家id in 单页玩家id列表:
                _玩家id = int(玩家id)
                玩家id列表.append(_玩家id)

            创建文件.write(json.dumps(单页玩家id列表, ensure_ascii=False) + "\n")
            创建文件1.write(json.dumps(单页手机型号列表, ensure_ascii=False) + "\n")

            seconds = (time.time() - startTime) * (page - 页码 - 1)
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            print("预计 获取玩家列表 剩余时间：%02d:%02d:%02d" % (h, m, s))

    去重复后的玩家id列表 = sorted(set(玩家id列表), key=玩家id列表.index)
    print('获取玩家列表完成……')

    return 去重复后的玩家id列表


def 主流程():
    连接 = requests.session()
    头文件 = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Inter Mac OS X 10_13_3)AppleWebKit/537.36(KHTML,like Gecko)Chrome/65.0.3325.162 Safari/537.36'
    }
    登录账号(连接, 头文件)
    游戏id = int(input('输入游戏id：'))
    创建文件 = open('游戏id：%d的玩家玩过的游戏.txt' % 游戏id, 'a', encoding='utf-8')
    创建文件.seek(0)
    创建文件.truncate()

    玩家id列表 = 获取玩家id列表(游戏id, 连接, 头文件)
    玩家人数 = len(玩家id列表)
    计数器 = 0
    for 玩家id in 玩家id列表:
        startTime = time.time()
        计数器 += 1
        print('开始获取id为 %d 的玩家数据[%d/%d]' % (玩家id, 计数器, 玩家人数))
        for page in range(1, 6, 1):
            html文本 = 获取一个网页(连接, 'https://www.taptap.com/user/%d/most-played?page=%d' % (玩家id, page), 头文件)
            if html文本 != None:
                解析玩家信息的html文本(html文本, 玩家id, 创建文件)
                print('第[%d/5]页写入完毕[%d/%d]……' % (page, 计数器, 玩家人数))
        seconds = (time.time() - startTime) * (玩家人数 - 计数器)
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        print("预计剩余完成时间：%02d:%02d:%02d" % (h, m, s))

    创建文件.close()
    print('完成！')


主流程()
结束 = input('按任意键关闭程序……')
