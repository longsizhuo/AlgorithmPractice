package contest

func incremovableSubarrayCount(nums []int) int64 {
	n := len(nums)
	var ans int64 = 0

	// Precompute the lengths of the longest increasing subsequences starting from each index
	lisStarting := make([]int, n)
	for i := range lisStarting {
		lisStarting[i] = 1
	}
	for i := n - 2; i >= 0; i-- {
		if nums[i] < nums[i+1] {
			lisStarting[i] = lisStarting[i+1] + 1
		}
	}

	// Precompute the lengths of the longest increasing subsequences ending at each index
	lisEnding := make([]int, n)
	for i := range lisEnding {
		lisEnding[i] = 1
	}
	for i := 1; i < n; i++ {
		if nums[i] > nums[i-1] {
			lisEnding[i] = lisEnding[i-1] + 1
		}
	}

	// Iterate through all possible subarrays and count those that can be removed
	for count := 1; count <= n; count++ {
		for left := 0; left < n; left++ {
			right := left + count
			if right > n {
				break
			}

			if (left == 0 || lisEnding[left-1] == left) &&
				(right == n || lisStarting[right] == n-right) &&
				(left == 0 || right == n || nums[left-1] < nums[right]) {
				ans++
			}
		}
	}

	return ans
}
