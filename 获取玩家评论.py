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
        'email': '123456789@qq.com',
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


def 解析玩家信息的html文本(html文本, 创建文件):
    etree = lxml.html.etree
    text = etree.HTML(html文本.encode('utf-8'))
    玩家id列表 = text.xpath('//div[@class="taptap-review-section"]/ul[@id="reviewsList"]/li/@id')
    # 用户名列表 = text.xpath('//div[@class="taptap-review-section"]/ul[@id="reviewsList"]/li/@data-user')

    for 玩家id in 玩家id列表:
        评价节点 = '//div[@class="review-item-text "]/div[@data-%s="contents"]/p/text()' % 玩家id
        评价内容 = text.xpath(评价节点)

        写入内容 = "%s,%s" % (玩家id, 评价内容)
        创建文件.write(json.dumps(写入内容, ensure_ascii=False) + "\n")


def 主流程():
    连接 = requests.session()
    头文件 = {
        'User-Agent': 'Mozilla/5.0(Macintosh;Inter Mac OS X 10_13_3)AppleWebKit/537.36(KHTML,like Gecko)Chrome/65.0.3325.162 Safari/537.36'
    }
    登录账号(连接, 头文件)
    评价星级 = [2, 3]

    for 星级 in 评价星级:
        创建文件 = open('%d星的玩家评论.txt' % 星级, 'a', encoding='utf-8')
        创建文件.seek(0)
        创建文件.truncate()

        计数器 = 0

        # 获取X星的评论总数
        链接 = 'https://www.taptap.com/app/31074/review?score=%d#review-list' % 星级
        N星的评论首页 = 获取一个网页(连接, 链接, 头文件)

        etree = lxml.html.etree
        评论首页 = etree.HTML(N星的评论首页.encode('utf-8'))
        评论数 = int(评论首页.xpath('//a[@data-taptap-tab="review"]/small/text()')[0])
        print("评价星级：%d, 评论数:%d" % (星级, 评论数))
        PageNum = max(min(int(评论数 / 20), 500), 1)

        # 导出每页的信息
        for page in range(1, PageNum + 1, 1):
            startTime = time.time()
            计数器 += 1
            评价网页 = 获取一个网页(连接, 'https://www.taptap.com/app/31074/review?score=%d&order=default&page=%d#review-list' % (星级, page), 头文件)
            if 评价网页 != None:
                解析玩家信息的html文本(评价网页, 创建文件)
                print('第[%d/%d]页写入完毕……%d星评价' % (page, PageNum, 星级))
            seconds = (time.time() - startTime) * ( PageNum - 计数器)
            m, s = divmod(seconds, 60)
            h, m = divmod(m, 60)
            print("预计剩余完成时间：%02d:%02d:%02d" % (h, m, s))

        创建文件.close()
    print('完成！')


主流程()
结束 = input('按任意键关闭程序……')
