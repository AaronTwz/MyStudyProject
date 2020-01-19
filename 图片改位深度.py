from PIL import Image
import os


def findfile(dir, fileList):
    if os.path.isfile(dir):
        fileList.append(dir)
    elif os.path.isdir(dir):
        for d in os.listdir(dir):
            newDir = os.path.join(dir, d)
            findfile(newDir, fileList)

    return fileList

def isPic(file):
    filetype = os.path.splitext(file)[1].lower()
    if filetype == '.png':
        return True
    else:
        return False

path = r'C:\Users\Administrator\Desktop\品阶1'
outpath = r'C:\Users\Administrator\Desktop\品阶2'
filelst = findfile(path, [])

imgNametxt = open(outpath + "/imgName.txt", mode='w')

for file in filelst:
    if isPic(file):
        imgName = os.path.basename(file)
        img = Image.open(file)
        imgNametxt.write('%s\n' % imgName[:-4])
        outimg = img.convert('P')
        outimg.save(outpath + '/' + imgName)

imgNametxt.close()
print("转换完毕")
