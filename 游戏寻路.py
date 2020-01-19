import pygame
import sys
import random
from PIL import Image, ImageDraw


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Vector(object):
    def __init__(self, start_Point, end_Point):
        self.start_Point = start_Point
        self.end_Point = end_Point
        self.x = end_Point.x - start_Point.x
        self.y = end_Point.y - start_Point.y


class Rect(object):
    def __init__(self, x0, y0, add_x, add_y):  # (左上角x，左上角y，w，h)【左上角是0,0点】
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + add_x
        self.y1 = y0 + add_y
        self.leftup = Point(self.x0, self.y0)  # 左上角点
        self.rightup = Point(self.x1, self.y0)  # 右上角点
        self.rightdown = Point(self.x1, self.y1)  # 右下角点
        self.leftdown = Point(self.x0, self.y1)  # 左下角点

    def isinRect(self, point):
        if point.x < self.x0 or point.x > self.x1 or point.y < self.y0 or point.y > self.y1:
            return False
        else:
            return True


# 判断2个点是否在一个向量（直线、线段）的两边
def cross(vec1, vec2):  # 叉积，
    k = vec1.x * vec2.y - vec1.y * vec2.x
    return k


# 判断2条线段是否相交
def iscross(start_line1, end_line1, start_line2, end_line2):  # 判断叉积的值是否为非正数，如果是，就相交
    line1_vec = Vector(start_line1, end_line1)
    s2_vec = Vector(start_line1, start_line2)
    e2_vec = Vector(start_line1, end_line2)
    K1 = cross(line1_vec, s2_vec) * cross(line1_vec, e2_vec)
    if K1 > 0:
        return False

    line2_vec = Vector(start_line2, end_line2)
    s1_vec = Vector(start_line2, start_line1)
    e1_vec = Vector(start_line2, end_line1)
    K2 = cross(line2_vec, s1_vec) * cross(line2_vec, e1_vec)
    if K2 > 0:
        return False
    else:
        return True


# 定义碰撞体的宽度的一半
w = 115


# 判断目标点是否可以走过去（不在碰撞范围内，并且不与碰撞范围相交）
def canmove(start_point, target_point):
    # 初始化：碰撞矩形
    rect1 = Rect(0 - w, 668, 178 + w, 900)
    rect2 = Rect(178 - w, 668, 436 + w, 808)
    rect3 = Rect(614 - w, 668, 167 + w, 714)
    # rect4 = Rect(781-w, 0, 299+w, 668)   668以上都不可以走，所以取x直接取x>668即可
    rect5 = Rect(202 - w, 1119, 473 + w, 184)
    rect6 = Rect(0 - w, 1533, 403 + w, 295)
    rect7 = Rect(611 - w, 1450, 469 + w, 181)
    rect_list = [rect1, rect2, rect3, rect5, rect6, rect7]
    # 1. 先判断目标点是否在矩形内，在就返回False
    for rect in rect_list:
        if rect.isinRect(target_point):
            return False

    # 2. 再判断目标向量是否与这些矩形相交
    for rect in rect_list:
        # 两个对角线都要判断：如果目标向量与两条对角线都不相交，则目标点有效，可以移动
        if iscross(start_point, target_point, rect.leftup, rect.rightdown) or iscross(start_point, target_point,
                                                                                      rect.leftdown, rect.rightup):
            return False
        else:
            return True


def move(start_point):
    targetpoint = Point(random.randrange(w, 1080 - w, 4),
                        random.randrange(668, 1920, 4))  # 668以上是墙体（左上角0,0），w是碰撞体宽度的一半，每4个像素取一个值
    while not canmove(start_point, targetpoint):
        targetpoint = Point(random.randrange(w, 1080 - w, 4), random.randrange(668, 1920, 4))

    return targetpoint


startpoint = Point(1011, 670)

for i in range(100):
    targetpoint = move(startpoint)
    print()
    startpoint = targetpoint


'''上面是路径检索的方法，下面是游戏的定义与方法'''


class Customer(object):
    def __init__(self):
        self.img = r'C:\Users\Administrator\Desktop\猫咪项目\猫咪8位图\cat_dongniqi.png'
        self.speed = 100
        self.posx = 1011
        self.posy = 670


def main():
    pygame.init()  # 初始化pygame
    pygame.font.init()  # 初始化字体
    font = pygame.font.SysFont("Arial", 50)  # 设置字体和大小
    size = width, height = 1080, 1920  # 设置窗口
    screen = pygame.display.set_mode(size)  # 显示窗口
    clock = pygame.time.Clock()  # 设置时钟
    background = pygame.image.load(r"C:\Users\Administrator\Desktop\猫咪项目\ditu.jpg")  # 加载背景图片
    screen.fill((255, 255, 255))  # 填充颜色
    screen.blit(background, (0, 0))  # 填入到背景
    cus = Customer()  # 定义个客人
    start_point = Point(cus.posx, cus.posy)  # 起始点
    while True:
        clock.tick(144)  # 每秒执行次数 60
        for event in pygame.event.get():  # 检测是否是退出时间
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                target_point = move(start_point)
                screen.blit(cus.img, (target_point.x, target_point.y))  # 设置客人的坐标
                start_point = target_point

        # 更新界面
        pygame.display.flip()
        # 延迟10 毫秒
        pygame.time.delay(10)
