"""
<p>给定两个整数数组&nbsp;<code>preorder</code> 和 <code>inorder</code>&nbsp;，其中&nbsp;<code>preorder</code> 是二叉树的<strong>先序遍历</strong>， <code>inorder</code>&nbsp;是同一棵树的<strong>中序遍历</strong>，请构造二叉树并返回其根节点。</p>

<p>&nbsp;</p>

<p><strong>示例 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="height: 302px; width: 277px;" /> 
<pre>
<strong>输入</strong><strong>:</strong> preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
<strong>输出:</strong> [3,9,20,null,null,15,7]
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> preorder = [-1], inorder = [-1]
<strong>输出:</strong> [-1]
</pre>

<p>&nbsp;</p>

<p><strong>提示:</strong></p>

<ul> 
 <li><code>1 &lt;= preorder.length &lt;= 3000</code></li> 
 <li><code>inorder.length == preorder.length</code></li> 
 <li><code>-3000 &lt;= preorder[i], inorder[i] &lt;= 3000</code></li> 
 <li><code>preorder</code>&nbsp;和&nbsp;<code>inorder</code>&nbsp;均 <strong>无重复</strong> 元素</li> 
 <li><code>inorder</code>&nbsp;均出现在&nbsp;<code>preorder</code></li> 
 <li><code>preorder</code>&nbsp;<strong>保证</strong> 为二叉树的前序遍历序列</li> 
 <li><code>inorder</code>&nbsp;<strong>保证</strong> 为二叉树的中序遍历序列</li> 
</ul>

<div><div>Related Topics</div><div><li>树</li><li>数组</li><li>哈希表</li><li>分治</li><li>二叉树</li></div></div><br><div><li>👍 1962</li><li>👎 0</li></div>
"""
from typing import List, Optional


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root
# leetcode submit region end(Prohibit modification and deletion)
