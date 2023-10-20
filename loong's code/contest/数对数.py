from typing import List
import os
import sys


def find_node(s):
    node = 1
    depth = 1
    for direction in s:
        # 判断自己的深度
        if direction == "L":
            node = node * 2 - 1
        else:
            node = node * 2
    return node

# 输入
n, q = map(int, input().split())
for _ in range(q):
    s = input().strip()
    print(find_node(s))
