'''
本题的要求很简单，就是求N个数字的和。麻烦的是，这些数字是以有理数分子/分母的形式给出的，你输出的和也必须是有理数的形式。

输入格式：
输入第一行给出一个正整数N（≤100）。随后一行按格式a1/b1 a2/b2 ...给出N个有理数。题目保证所有分子和分母都在长整型范围内。另外，负数的符号一定出现在分子前面。

输出格式：
输出上述数字和的最简形式 —— 即将结果写成整数部分 分数部分，其中分数部分写成分子/分母，要求分子小于分母，且它们没有公因子。如果结果的整数部分为0，则只输出分数部分。

输入样例1：
5
2/5 4/15 1/30 -2/60 8/3
输出样例1：
3 1/3
'''


# 求最大公约数
def gcd(m, n):
    if n == 0:
        return 1
    r = m % n
    while r != 0:
        m, n = n, r
        r = m % n
    return abs(n)


# 求最小公倍数
def lcm(m, n):
    r = m * n / gcd(m, n)
    return abs(r)


# 求两分数的和
def sum2(m, n):
    num_m, den_m, num_n, den_n = int(m[0]), int(m[1]), int(n[0]), int(n[1])
    den = lcm(den_m, den_n)  # 分母
    num = num_m * den / den_m + num_n * den / den_n  # 分子
    # 约分
    g = gcd(den, num)
    den_m = den / g
    num_m = num / g
    return [num_m, den_m]


# 主函数
num = int(input())

if num > 1:
    lst = input().split()
    a = lst[0].split('/')
    for i in range(1, num):
        b = lst[i].split('/')
        c = sum2(a, b)
        a = c
    if a[0] >= 0:
        x = int(a[0] // a[1])
        y = a[0] % a[1]

        if x != 0:
            if y != 0:
                print(x, "%d/%d" % (y, a[1]))
            else:
                print(x)
        else:
            if y != 0:
                print("%d/%d" % (a[0], a[1]))
            else:
                print(0)
    else:
        x = int(abs(a[0]) // a[1])
        y = abs(a[0]) % a[1]
        if x != 0:
            if y != 0:
                print(-x, "%d/%d" % (y, a[1]))
            else:
                print(-x)
        else:
            if y != 0:
                print("%d/%d" % (a[0], a[1]))
            else:
                print(0)


else:
    lst = [int(i) for i in input().split('/')]
    g = gcd(lst[0], lst[1])
    den_m = lst[1] / g
    num_m = lst[0] / g
    x = int(num_m // den_m)
    y = num_m % den_m
    if x != 0:
        if y != 0:
            print(x, "%d/%d" % (y, den_m))
        else:
            print(x)
    else:
        if y != 0:
            print("%d/%d" % (num_m, den_m))
        else:
            print(0)
