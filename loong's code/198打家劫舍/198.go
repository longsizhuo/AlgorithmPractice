package main

import "fmt"

func rob(nums []int) int {
	cur, pre := 0, 0
	for i := range nums {
		cur, pre = max(pre+nums[i], cur), cur
	}
	return cur
}

func rob2(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	return max(rob(nums[:len(nums)-1]), rob(nums[1:]))
}

func main() {
	var canshu []int
	//canshu = make([]int, 4)
	canshu = append([]int{1, 2, 3, 1})
	fmt.Println(rob2(canshu))
}
