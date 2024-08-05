def decimal_to_ternary(n):
    if n == 0:
        return "0"
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n = n // 3
    return ternary


input_str = int(input())
flag = 0
min_flag = 0
dicts = []
for ind, i in enumerate(decimal_to_ternary(input_str)):
    if i == '0':
        dicts.append((i, flag))
    elif i == '1':
        flag -= 1
        dicts.append((i, flag))
        if flag < min_flag:
            min_flag = flag
    elif i == '2':
        flag += 1
        dicts.append((i, flag))
    else:
        print('Error')
        break
for ind, i in dicts:
    if ind == '0':
        print(' ' * (i - min_flag) + '\u2b07')
    elif ind == '1':
        print(' ' * (i - min_flag) + '\u2b0b')
    elif ind == '2':
        print(' ' * (i - min_flag) + '\u2b0a')
    else:
        print('Error')
        break
