//
// Created by longs on 2024/8/6.
//

#include "remove_element.h"
#include <vector>
#include <algorithm>
#include <iostream>

class Solution {
public:
    static auto removeElement(std::vector<int>& nums, int val) {
        auto new_end = std::remove(nums.begin(), nums.end(), val);
        // 我想在这里测试new_end的值
        return new_end;
//        nums.erase(std::remove(nums.begin(), nums.end(), val), nums.end());
//        return nums.size();
    }
};

int main() {
    std::vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    auto result = Solution::removeElement(nums, val);
    std::cout << result - nums.begin() << std::endl;
    return 0;
}