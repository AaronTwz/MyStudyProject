import cv2
import numpy as np

pathbig = r'C:\Users\Administrator\Desktop\newfile\sanhua.png'
pathsmall = r'C:\Users\Administrator\Desktop\newfile\jewelry_sanhua_1.png'
iviewbig = cv2.imread(pathbig, -1)  # 大图
iviewsmall = cv2.imread(pathsmall, -1)  # 小图
# flags = -1：imread按解码得到的方式读入图像
# flags = 0：imread按单通道的方式读入图像，即灰白图像
# flags = 1：imread按三通道方式读入图像，即彩色图像

height, weight = iviewsmall.shape[:2]  # 获取小图的高和宽

cv2.namedWindow('watch')

# 模板匹配
methods = [cv2.TM_SQDIFF,
           cv2.TM_CCORR,
           cv2.TM_CCOEFF,
           cv2.TM_SQDIFF_NORMED,
           cv2.TM_CCORR_NORMED,
           cv2.TM_CCOEFF_NORMED]
num = 3
matchResult = cv2.matchTemplate(iviewbig, iviewsmall, methods[num])

min_v, max_v, min_xy, max_xy = cv2.minMaxLoc(matchResult)
print(min_v, max_v, min_xy, max_xy)

cv2.circle(iviewbig, min_xy, 5, (0, 0, 255))
# cv2.circle(iviewbig, max_xy, 5, (0, 0, 255))
cv2.rectangle(iviewbig,min_xy[0]+weight,min_xy[1]+height,(0,0,255))

# 显示图片
cv2.imshow('watch', iviewbig)

cv2.waitKey(0)
cv2.destroyAllWindows()
