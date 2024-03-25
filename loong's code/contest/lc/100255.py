from collections import Counter
import heapq

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        # 计算每个字符的频率
        freq = Counter(word)

        # 如果最大值和最小值之差小于等于k，则不需要删除
        if max(freq.values()) - min(freq.values()) <= k:
            return 0

        # 将频率及其对应字符转换为(频率，字符)元组列表，并维护最小堆
        min_heap = [(f, char) for char, f in freq.items()]
        heapq.heapify(min_heap)

        ans = 0
        while True:
            # 获取当前最小和最大频率
            min_freq, _ = min_heap[0]
            max_freq = max(freq.values())

            # 如果最大和最小频率之差已经不超过k，则结束循环
            if max_freq - min_freq <= k:
                break

            # 从堆中弹出最小频率的字符，并更新答案和频率表
            _, char_to_remove = heapq.heappop(min_heap)
            delete_count = freq[char_to_remove]
            ans += delete_count  # 增加到总的删除次数
            del freq[char_to_remove]  # 从频率表中删除该字符

        return ans



print(Solution().minimumDeletions("aabcaba", 0))  # 0
print(Solution().minimumDeletions("dabdcbdcdcd", 2))  # 2
print(Solution().minimumDeletions("aaaabaaaa", 2))  # 0

