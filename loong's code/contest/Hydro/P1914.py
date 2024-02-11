n = int(input())
char = input()
    # 字母向后移动n位
ans = ""
for i in char:
    if i.isalpha():
        if i.isupper():
            ans += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
        else:
            ans += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
    else:
        ans += i
print(ans)