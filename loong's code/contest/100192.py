class Solution:
    def minimumPushes(self, word: str) -> int:
        # 统计字母频率
        freq = {}
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1

        # 按频率排序
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # 映射分配
        push_count = 0
        button_press = 1  # 当前按键上的字母需要的按键次数
        for i, (char, count) in enumerate(sorted_chars):
            # 每9个字母，按键次数增加1
            if i % 8 == 0 and i > 0:
                button_press += 1
            push_count += count * button_press

        return push_count

# 示例
print(Solution().minimumPushes("aabbccddeeffgghhiiiiii"))
