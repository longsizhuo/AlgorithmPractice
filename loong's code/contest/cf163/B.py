t = int(input().strip())  # 读取测试用例数
for _ in range(t):
    n = int(input().strip())  # 读取数组长度
    a = list(map(int, input().strip().split()))  # 读取数组
    answer = 'YES'  # 默认答案是YES
    for i in range(n - 1, 0, -1):  # 从后往前遍历数组
        if a[i] < a[i - 1]:  # 如果当前元素小于前一个元素
            if a[i - 1] < 10:  # 如果前一个元素小于10，无法分解成单独的数字
                answer = 'NO'  # 不可能通过分解操作使数组有序
                break
            elif a[i] < a[i - 1] % 10:  # 如果当前元素小于前一个元素的十位数
                answer = 'NO'  # 同样不可能使数组有序
                break
    print(answer)  # 输出答案
