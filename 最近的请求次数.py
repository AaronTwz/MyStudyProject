def func(mylist):
    output = []
    for i in range(len(mylist)):
        j = i // 2
        while True:
            ch = sim(mylist, i, j, mylist[i] - 10000)
            if ch == 1:
                output.append(i - j + 1)
                break
            elif ch == 0:
                j = j // 2
            elif ch == 2:
                j = (i + j) // 2
            elif ch == 3:
                output.append(i - j)
                break

    return output


def sim(lst, i, k, m):
    if k == 0:
        return 1
    elif lst[k] >= m > lst[k - 1]:
        return 1
    elif m <= lst[k - 1]:
        return 0
    elif m > lst[k] and k == i - 1:
        return 3
    else:
        return 2


mylist = eval(input())
print(func(mylist))
