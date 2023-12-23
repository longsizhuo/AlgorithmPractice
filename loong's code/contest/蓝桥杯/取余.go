package main

import (
	"fmt"
)

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func countValidPairs(A, B, S, T int) int64 {
	var count int64 = 0
	for b := 1; b <= B; b++ {
		// 计算完整周期内满足条件的a的数量
		fullCycles := A / b
		count += int64(max(0, min(b, T+1)-S)) * int64(fullCycles)

		// 计算最后一个不完整周期
		remaining := A % b
		count += int64(max(0, min(remaining+1, T+1)-S))
	}
	return count
}

func main() {
	var A, B, S, T int
	fmt.Scan(&A, &B, &S, &T)

	fmt.Println(countValidPairs(A, B, S, T))
}
