from bisect import bisect


class CountIntervals:

    def __init__(self):
        self.list1 = []

    def add(self, left: int, right: int) -> None:
        index = 0
        if not self.list1:
            self.list1.append([left, right])
            return
        while 1:
            # 如果最小值小于了元素的最大值，且最大值大于了最大值，则说明有交集，且拓宽范围
            if left < self.list1[index][1] < right:
                # 如果还小于了最小值，说明范围的最小值也需要拓宽
                if left < self.list1[index][0]:
                    self.list1[index][0] = left
                self.list1[index][1] = right
                index += 1
                continue

            elif self.list1[index][1] < left:
                # 如果是最后一个元素
                if index == len(self.list1) - 1 or self.list1[index + 1][0] > right:
                    self.list1.append([left, right])
                    index += 1
                    continue

                # 将前一个和后一个区间合起来的情况
            elif index != len(self.list1)-1 and self.list1[index][1] > left and self.list1[index + 1][0] < right:
                self.list1[index][1] = self.list1[index + 1][1]
                self.list1.pop(index + 1)
                continue
            index += 1
            if index >= len(self.list1):
                return

    def count(self) -> int:
        counts_ = 0
        for i in self.list1:
            counts_ += i[1] - i[0] + 1
        print(self.list1)
        return counts_


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)

countIntervals = CountIntervals()
countIntervals.add(2, 3)  # 将 [2, 3] 添加到区间集合中
countIntervals.add(7, 10)  # 将 [7, 10] 添加到区间集合中
print(countIntervals.count())

countIntervals.add(5, 8)
print(countIntervals.count())
