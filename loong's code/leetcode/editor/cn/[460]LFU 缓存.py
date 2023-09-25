# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。 
# 
#  实现 LFUCache 类： 
# 
#  
#  LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象 
#  int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。 
#  void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 
# capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。 
#  
# 
#  为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。 
# 
#  当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。 
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
# 
#  
# 
#  示例： 
# 
#  
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", 
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // 返回 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // 返回 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 10⁴ 
#  0 <= key <= 10⁵ 
#  0 <= value <= 10⁹ 
#  最多调用 2 * 10⁵ 次 get 和 put 方法 
#  
# 
#  Related Topics 设计 哈希表 链表 双向链表 👍 764 👎 0
import collections


# leetcode submit region begin(Prohibit modification and deletion)
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_value = {}  # 保存键到值的映射
        self.key_to_freq = {}   # 保存键到使用频率的映射
        self.freq_to_keys = defaultdict(OrderedDict)  # 保存使用频率到键的映射，使用OrderedDict来维护顺序
        self.min_freq = 0       # 记录最小的使用频率

    def get(self, key: int) -> int:
        if key in self.key_to_value:
            # 如果键存在，更新使用频率
            self.key_to_freq[key] += 1
            freq = self.key_to_freq[key]
            # 将键从旧的频率列表中移除，并添加到新的频率列表中
            del self.freq_to_keys[freq - 1][key]
            self.freq_to_keys[freq][key] = None
            # 如果旧频率列表为空，更新最小频率
            if not self.freq_to_keys[freq - 1]:
                if freq - 1 == self.min_freq:
                    self.min_freq += 1
            return self.key_to_value[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_value:
            # 如果键已存在，更新值和使用频率
            self.key_to_value[key] = value
            self.key_to_freq[key] += 1
            freq = self.key_to_freq[key]
            # 移除旧频率列表中的键，添加到新频率列表中
            del self.freq_to_keys[freq - 1][key]
            self.freq_to_keys[freq][key] = None
            # 如果旧频率列表为空，更新最小频率
            if not self.freq_to_keys[freq - 1]:
                if freq - 1 == self.min_freq:
                    self.min_freq += 1
        else:
            # 如果缓存已满，移除最不经常使用的键
            if len(self.key_to_value) >= self.capacity:
                # 获取最小频率列表的第一个键，并移除它
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_value[evict_key]
                del self.key_to_freq[evict_key]
            # 添加新键到字典中，初始化使用频率为1，加入频率为1的列表中
            self.key_to_value[key] = value
            self.key_to_freq[key] = 1
            self.freq_to_keys[1][key] = None
            self.min_freq = 1

# class LFUCache:
#
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cache = collections.OrderedDict(list)
#
#     def get(self, key: int) -> int:
#         # 如果key在字典中，返回value
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             return self.cache[key]
#         else:
#             return -1
#
#     def put(self, key: int, value: int) -> None:
#         keys = list(self.cache.keys())
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             self.cache[key][1] = value
#             self.cache[key][0] += 1
#             # 与右边的数比较，如果大于右边的数，交换位置
#             # 找到当前键的索引
#             idx = keys.index(key)
#
#             # 如果当前键不是最后一个键，并且其值大于下一个键的值，就进行交换
#             if idx < len(keys) - 1 and self.cache[keys[idx]][0] > self.cache[keys[idx + 1]][0]:
#                 # 交换键的位置
#                 keys[idx], keys[idx + 1] = keys[idx + 1], keys[idx]
#
#
#
#         else:
#             if len(self.cache) == self.capacity:
#                 # 如果key不在字典中，且字典已满，删除最不经常使用的项
#
#                 self.cache.popitem(last=False)
#             self.cache[key] = 1
#
#

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
