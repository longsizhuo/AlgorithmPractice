# ```
# Excel地址
#
# 题目描述
# Excel 单元格的地址表示很有趣，它使用字母来表示列号。
#
# 比如，
#
# A 表示第 1 列，
#
# B 表示第 2 列，
#
# Z 表示第 26 列，
#
# AA 表示第 27 列，
#
# AB 表示第 28 列，
#
# BA 表示第 53 列，
#
# ⋯
# ⋯
# 当然 Excel 的最大列号是有限度的，所以转换起来不难。
#
# 如果我们想把这种表示法一般化，可以把很大的数字转换为很长的字母序列呢？
#
# 本题目即是要求对输入的数字, 输出其对应的 Excel 地址表示方式。
#
# 输入描述
# 输入一个整数
# �
# n，其范围 [1,2147483647]。
# ```
n = int(input())


def convertToTitle(n):
    result = ""
    while n > 0:
        n -= 1
        result = chr(n % 26 + ord('A')) + result
        n //= 26
    return result


print(convertToTitle(n))
