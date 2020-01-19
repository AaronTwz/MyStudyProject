'''
pyq_num = int(input())
pyq_lst = set()
for num in range(pyq_num):
    pyq_lst.add(input())
people_num = int(input())
search_lst = tuple(input().split())
# 分隔字符串，判断k>1，把元素加入set
lst_pyq = []
set_people = set()
for pyq in pyq_lst:
    lst_pyq = pyq.split()
    if int(lst_pyq[0]) > 1:
        set_people.update(lst_pyq[1:])
p = set(search_lst) - set_people
if p != set():
    px_list = [search_lst.index(P) for P in p]
    px_list.sort()
    people_lst = [search_lst[px] for px in px_list]
    print(" ".join(people_lst))
else:
    print("No one is handsome")
'''

ypy = set()
mpy = list()
inputList = list()
search_list = list()
singleList = list()

pyq_num = int(input())

for N in range(pyq_num):
    singleList = input().split()
    num = int(singleList[0])
    if num > 1:
        for n in range(1, num + 1):
            ypy.add(singleList[n])

people_num = int(input())
search_list = tuple(input().split())
for i in range(len(search_list)):
    if search_list[i] not in ypy:
        mpy.append(search_list[i])

mpy2 = list(set(mpy))
mpy2.sort(key=mpy.index)

if len(mpy2) != 0:
    print((" ".join("%s" % i for i in mpy2)))
else:
    print("No one is handsome")
