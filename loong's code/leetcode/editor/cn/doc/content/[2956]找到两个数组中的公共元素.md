<p>给你两个下标从 <strong>0</strong>&nbsp;开始的整数数组&nbsp;<code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;，它们分别含有 <code>n</code>&nbsp;和 <code>m</code>&nbsp;个元素。请你计算以下两个数值：</p>

<ul> 
 <li><code>answer1</code>：使得&nbsp;<code>nums1[i]</code>&nbsp;在&nbsp;<code>nums2</code>&nbsp;中出现的下标&nbsp;<code>i</code>&nbsp;的数量。</li> 
 <li><code>answer2</code>：使得&nbsp;<code>nums2[i]</code>&nbsp;在&nbsp;<code>nums1</code>&nbsp;中出现的下标&nbsp;<code>i</code>&nbsp;的数量。</li> 
</ul>

<p>返回 <code>[answer1, answer2]</code>。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<div class="example-block"> 
 <p><strong>输入：</strong><span class="example-io">nums1 = [2,3,2], nums2 = [1,2]</span></p> 
</div>

<p><strong>输出：</strong><span class="example-io">[2,1]</span></p>

<p><strong>解释：</strong></p>

<p><img src="https://assets.leetcode.com/uploads/2024/05/26/3488_find_common_elements_between_two_arrays-t1.gif" style="width: 225px; height: 150px;" /></p>

<p><strong class="example">示例 2：</strong></p>

<div class="example-block"> 
 <p><strong>输入：</strong><span class="example-io">nums1 = [4,3,2,3,1], nums2 = [2,2,5,2,3,6]</span></p> 
</div>

<p><strong>输出：</strong><span class="example-io">[3,4]</span></p>

<p><strong>解释：</strong></p>

<p><code>nums1</code>&nbsp;中下标在 1，2，3 的元素在&nbsp;<code>nums2</code>&nbsp;中也存在。所以&nbsp;<code>answer1</code>&nbsp;为&nbsp;3。</p>

<p><code>nums2</code>&nbsp;中下标在 0，1，3，4 的元素在&nbsp;<code>nums1</code>&nbsp;中也存在。所以&nbsp;<code>answer2</code>&nbsp;为 4。</p>

<p><strong class="example">示例 3：</strong></p>

<div class="example-block"> 
 <p><strong>输入：</strong><span class="example-io">nums1 = [3,4,2,3], nums2 = [1,5]</span></p> 
</div>

<p><strong>输出：</strong><span class="example-io">[0,0]</span></p>

<p><strong>解释：</strong></p>

<p><code>nums1</code>&nbsp;和&nbsp;<code>nums2</code>&nbsp;中没有相同的数字，所以答案是 [0,0]。</p>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>n == nums1.length</code></li> 
 <li><code>m == nums2.length</code></li> 
 <li><code>1 &lt;= n, m &lt;= 100</code></li> 
 <li><code>1 &lt;= nums1[i], nums2[i] &lt;= 100</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数组</li><li>哈希表</li></div></div><br><div><li>👍 23</li><li>👎 0</li></div>