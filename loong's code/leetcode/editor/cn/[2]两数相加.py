"""
<p>给你两个&nbsp;<strong>非空</strong> 的链表，表示两个非负的整数。它们每位数字都是按照&nbsp;<strong>逆序</strong>&nbsp;的方式存储的，并且每个节点只能存储&nbsp;<strong>一位</strong>&nbsp;数字。</p>

<p>请你将两个数相加，并以相同形式返回一个表示和的链表。</p>

<p>你可以假设除了数字 0 之外，这两个数都不会以 0&nbsp;开头。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p> 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" /> 
<pre>
<strong>输入：</strong>l1 = [2,4,3], l2 = [5,6,4]
<strong>输出：</strong>[7,0,8]
<strong>解释：</strong>342 + 465 = 807.
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>l1 = [0], l2 = [0]
<strong>输出：</strong>[0]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
<strong>输出：</strong>[8,9,9,9,0,0,0,1]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>每个链表中的节点数在范围 <code>[1, 100]</code> 内</li> 
 <li><code>0 &lt;= Node.val &lt;= 9</code></li> 
 <li>题目数据保证列表表示的数字不含前导零</li> 
</ul>

<div><div>Related Topics</div><div><li>递归</li><li>链表</li><li>数学</li></div></div><br><div><li>👍 9707</li><li>👎 0</li></div>
"""
from typing import Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        carry += l1.val + (l2.val if l2 else 0)
        l1.val = carry % 10
        l1.next = self.addTwoNumbers(l1.next, l2.next if l2 else None, carry//10)
        return l1
        # l1_list = []
        # l2_list=[]
        # def recursion_list(node:ListNode, listt):
        #     if not node:
        #         return listt
        #     listt.append(node.val)
        #     return recursion_list(node.next, listt)
        # l1_list = recursion_list(l1, l1_list)
        # l2_list = recursion_list(l2, l2_list)
        # l1_list = ''.join(map(str, l1_list))
        # l2_list = ''.join(map(str, l2_list))
        # l3 = str(int(l1_list)+int(l2_list))
        # print(l3)
        # def recursion_linkArray(num):
        #     if not num:
        #         return None
        #     head = ListNode(0)
        #     current = head
        #     for c in num:
        #         current.next = ListNode(int(c))
        #         current = current.next
        #     return head.next
        # head = recursion_linkArray(l3[::-1])
        # print(recursion_list(head, []))
        # print(type(l1), type(head))
        # return head

# leetcode submit region end(Prohibit modification and deletion)
