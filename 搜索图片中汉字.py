from PIL import Image
import pytesseract
import os
import xlsxwriter


def findfile(dir, fileList):
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for d in os.listdir(dir):
            newDir = os.path.join(dir, d)
            findfile(newDir, fileList)

    return fileList


def isPic(filetype):
    filetype = filetype.lower()
    if filetype in ['.jgp', '.png', '.jpeg', '.bmp', '.jpg']:
        return True
    else:
        return False


path = r'C:\Users\Administrator\Desktop\_UITextures'
fileList = findfile(path, [])  # 得到目录下所有文件名称
wordList = []  # 文件名对应汉字的列表的列表

fileNum = len(fileList)
j = 0
for f in fileList:
    j += 1
    filetype = os.path.splitext(f)[1]
    if isPic(filetype):
        img = Image.open(f)
        text = pytesseract.image_to_string(img, lang='chi_sim')
        wordList.append([f, ','.join(text.split())])
    print("第 %d/%d 个文件识别完成" % (j, fileNum))

outfile = r'C:\Users\Administrator\Desktop\图片中的汉字.xls'
workbook = xlsxwriter.Workbook(outfile)
sheet = workbook.add_worksheet("Sheet1")

picNum = len(wordList)
for i in range(picNum):
    sheet.write(i, 0, i + 1)
    sheet.write(i, 1, wordList[i][0])
    sheet.write(i, 2, wordList[i][1])
    if len(wordList[i][1]) != 0:
        sheet.set_row(i, height=75)  # 75行高为100像素
        im = Image.open(wordList[i][0])
        w = im.width
        h = im.height
        sheet.insert_image(i, 3, wordList[i][0], {'x_scale': 100 / h, 'y_scale': 100 / h})
    print("第 %d/%d 张图片数据导入完成" % (i, picNum))

workbook.close()

print("转换完毕")
