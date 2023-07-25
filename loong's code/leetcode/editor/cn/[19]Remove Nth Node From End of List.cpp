/**
<p>Given the <code>head</code> of a linked list, remove the <code>n<sup>th</sup></code> node from the end of the list and return its head.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" /> 
<pre>
<strong>Input:</strong> head = [1,2,3,4,5], n = 2
<strong>Output:</strong> [1,2,3,5]
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> head = [1], n = 1
<strong>Output:</strong> []
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre>
<strong>Input:</strong> head = [1,2], n = 1
<strong>Output:</strong> [1]
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li>The number of nodes in the list is <code>sz</code>.</li> 
 <li><code>1 &lt;= sz &lt;= 30</code></li> 
 <li><code>0 &lt;= Node.val &lt;= 100</code></li> 
 <li><code>1 &lt;= n &lt;= sz</code></li> 
</ul>

<p>&nbsp;</p> 
<p><strong>Follow up:</strong> Could you do this in one pass?</p>

<div><div>Related Topics</div><div><li>链表</li><li>双指针</li></div></div><br><div><li>👍 2501</li><li>👎 0</li></div>
*/

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for singly-linked list.**/
//struct ListNode {
//    int val;
//    ListNode *next;
//    ListNode() : val(0), next(nullptr) {}
//    ListNode(int x) : val(x), next(nullptr) {}
//    ListNode(int x, ListNode *next) : val(x), next(next) {}
//};

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *yummyNode = new ListNode(0);
        yummyNode->next = head;
        ListNode *fast = yummyNode;
        ListNode *slow = yummyNode;
        for(int i = 0; i < n; i++){
            slow = slow->next;
        }
        while (slow->next != nullptr){
            fast = fast->next;
            slow = slow->next;
        }
        ListNode *del = fast->next;
        fast->next = del->next;
        delete del;
        ListNode *ret = yummyNode->next;
        delete yummyNode;
        return ret;


    }
};
//leetcode submit region end(Prohibit modification and deletion)
