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


path = r'C:\Users\Administrator\Desktop\猫咪项目\食物'
filelst = findfile(path, [])

for file in filelst:
    oldname = '/'.join(os.path.split(file))
    newname = path + '/food_' + os.path.basename(file)
    os.rename(oldname, newname)
