parts1 = input().strip().split('/')
parts2 = input().strip().split('/')

i, j = 0, 0
right_i, right_j = len(parts1) - 1, len(parts2) - 1
while i < len(parts1) and j < len(parts2):
    if parts1[i] == parts2[j]:
        i += 1
        j += 1
    else:
        while right_i >= i and right_j >= j and parts1[right_i] == parts2[right_j]:
            right_i -= 1
            right_j -= 1
        break
diff1 = parts1[i:right_i + 1]
diff2 = parts2[j:right_j + 1]
if parts1[:i]:
    print('/'.join(parts1[:i]) + '/', end='')
if diff1 or diff2:
    print('{' + '/'.join(diff1) + ' => ' + '/'.join(diff2) + '}', end='')
if parts1[right_i + 1:]:
    print('/' + '/'.join(parts1[right_i + 1:]), end='')
