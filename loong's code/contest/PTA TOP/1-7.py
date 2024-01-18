import sys


head_addr, n = input().split()
n = int(n)
if n <= 0 or head_addr == '-1':
    sys.exit(0)

nodes = {}
for _ in range(n):
    addr, value, next_addr = input().split()
    nodes[addr] = (int(value), next_addr)



def process_linked_list(head_addr, nodes):
    seen = set()
    unique_list_head = unique_list_tail = None
    removed_list_head = removed_list_tail = None
    current_addr = head_addr

    # 新增变量用于处理头节点是重复节点的情况
    new_head_found = False

    while current_addr != '-1':
        value, next_addr = nodes[current_addr]
        abs_value = abs(value)

        if abs_value not in seen:
            seen.add(abs_value)
            if not unique_list_head:
                unique_list_head = current_addr
                new_head_found = True  # 找到了新的头节点
            if unique_list_tail:
                nodes[unique_list_tail] = (nodes[unique_list_tail][0], current_addr)
            unique_list_tail = current_addr
        else:
            if not removed_list_head:
                removed_list_head = current_addr
            if removed_list_tail:
                nodes[removed_list_tail] = (nodes[removed_list_tail][0], current_addr)
            removed_list_tail = current_addr

        current_addr = next_addr

    if unique_list_tail:
        nodes[unique_list_tail] = (nodes[unique_list_tail][0], '-1')
    if removed_list_tail:
        nodes[removed_list_tail] = (nodes[removed_list_tail][0], '-1')

    # 如果原始头节点是重复的，更新头节点地址
    if not new_head_found:
        unique_list_head = '-1'

    return unique_list_head, removed_list_head


def print_linked_list(head, nodes):
    current_addr = head
    while current_addr != '-1':
        value, next_addr = nodes[current_addr]
        print(f"{current_addr} {value} {next_addr}")
        current_addr = next_addr


unique_list_head, removed_list_head = process_linked_list(head_addr, nodes)
print_linked_list(unique_list_head, nodes)
print_linked_list(removed_list_head, nodes)
