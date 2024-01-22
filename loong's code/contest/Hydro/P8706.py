string = input()
stack = []
ans = ""
for i in string:
    if i.isalpha() and not stack:
        stack.append(i)
    elif i.isalpha() and stack:
        ans += stack.pop()
        stack.append(i)
    elif i.isnumeric():
        ans += stack.pop() * int(i)
if stack:
    ans += stack.pop()
print(ans)



