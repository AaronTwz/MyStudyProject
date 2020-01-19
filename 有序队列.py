from study_数据结构与算法Py.Queue import Queue

# def func(S):
#     q = list(S)
#     minStr = list(S)
#     for i in range(len(q)):
#         a = q.pop(0)
#         q.append(a)
#         if q < minStr:
#             minStr = q.copy()
#     return ''.join(minStr)
#
#
# S = eval(input())
# print(func(S))

from collections import deque

s = eval(input())
min_queue = None
queue = deque(s)
for i in range(len(s)):
    char = queue.pop()
    queue.appendleft(char)
    if min_queue is None or min_queue > queue:
        min_queue = deque(queue)
print(''.join(min_queue))
