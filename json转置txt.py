import json
import os


def json2txt(path):
    with open(path) as f:
        dataList = json.load(f)
        f.close()

    cdkList = []
    for data in dataList:
        cdkList.append(data['code'])

    print(str(list(cdkList)))
    outfile1 = path[0:path.index('.json')] + '_1.txt'
    outfile2 = path[0:path.index('.json')] + '_2.txt'
    with open(outfile1, 'w') as outf:
        for i in range(int(len(cdkList) / 2)):
            outf.write(cdkList[i] + '\n')
            i += 1
        outf.close()
    with open(outfile2, 'w') as outf:
        for i in range(int(len(cdkList) / 2), len(cdkList)):
            outf.write(cdkList[i] + '\n')
        outf.close()
    print('处理完毕！')


def findfile(dir, fileList):
    if os.path.isfile(dir):
        if dir.endswith('json'):
            fileList.append(dir)
    elif os.path.isdir(dir):
        for d in os.listdir(dir):
            newDir = os.path.join(dir, d)
            findfile(newDir, fileList)

    return fileList


filepath = 'C:/Users/Administrator/Desktop/1111'
fileList = []
fileList = findfile(filepath, fileList)
print(fileList)
for file in fileList:
    json2txt(file)
