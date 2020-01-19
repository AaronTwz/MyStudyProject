# from study_数据结构与算法Py.Stack import stack
#
#
# def dailyTemp(T):
#     DayList = []
#     i = 0
#     length = len(T)
#     while i < length - 1:
#         a = stack()
#         j = i + 1
#         while j < length:
#             a.push(T[j])
#             if T[i] < T[j]:
#                 DayList.append(a.size())
#                 break
#             else:
#                 if j == length - 1:
#                     DayList.append(0)
#             j += 1
#         i += 1
#     DayList.append(0)
#     return DayList
#
# t = eval(input())
# print(dailyTemp(t))

def dailyTemp(T):
    lst = []
    for m in range(len(T) - 1):
        for n in range(m + 1, len(T)):
            if T[n] > T[m]:
                lst.append(n - m)
                break
            elif n == len(T)-1:
                lst.append(0)

    lst.append(0)
    return lst

T = eval(input())
print(dailyTemp(T))
