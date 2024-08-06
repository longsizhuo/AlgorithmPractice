def is_subsequence(s, t):
    it = iter(s)
    return all(char in it for char in t)

def is_cer_subsequence(s, t):
    it = iter(s)
    return all(any(c == sc or sc == '?' for sc in it) for c in t)

def replace_question_marks(s, t):
    s_list = list(s)
    t_list = list(t)
    j = 0
    for i in range(len(s_list)):
        if s_list[i] == '?':
            if j < len(t_list):
                s_list[i] = t_list[j]
                j += 1
            else:
                s_list[i] = 'a'
        elif j < len(t_list) and s_list[i] == t_list[j]:
            j += 1
    return ''.join(s_list)

T = int(input())
results = []

for _ in range(T):
    s = input().strip()
    t = input().strip()

    if len(t) > len(s):
        results.append("NO")
        continue

    if is_subsequence(s.replace('?', ''), t):
        results.append("YES")
        results.append(replace_question_marks(s, t))
        continue

    if not is_cer_subsequence(s, t):
        results.append("NO")
        continue

    results.append("YES")
    results.append(replace_question_marks(s, t))

for result in results:
    print(result)
