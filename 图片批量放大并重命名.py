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
    if filetype in ['.jgp', '.png', '.jpeg', '.bmp', '.jpg']:
        return True
    else:
        return False

path = r'C:\Users\Administrator\Desktop\15件'
filelst = findfile(path, [])

for file in filelst:
    if isPic(file) and os.path.splitext(file)[0][-2:].endswith('01'):
        img = Image.open(file)
        h, w = img.size
        outimgName = os.path.splitext(file)[0][:-2] + '02.png'
        outimg = img.resize((int(h*0.9), int(w*0.9)), Image.ANTIALIAS).convert('P')
        outimg.save("%s" % outimgName)

        outimgName = os.path.splitext(file)[0][:-2] + '03.png'
        outimg = img.resize((int(h * 0.8), int(w * 0.8)), Image.ANTIALIAS).convert('P')
        outimg.save("%s" % outimgName)

        outimgName = os.path.splitext(file)[0][:-2] + '04.png'
        outimg = img.resize((int(h * 0.7), int(w * 0.7)), Image.ANTIALIAS).convert('P')
        outimg.save("%s" % outimgName)

        outimgName = os.path.splitext(file)[0][:-2] + '01.png'
        outimg = img.convert('P')
        outimg.save("%s" % outimgName)


