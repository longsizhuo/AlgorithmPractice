package main

import (
	"fmt"
	"math"
)

func main() {
	var n int
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}
	arr := make([]int, n)
	for i := range arr {
		_, err := fmt.Scan(&arr[i])
		if err != nil {
			return
		}
	}
	maxSoFar := math.MinInt32
	maxEndingHere := 0
	for _, num := range arr {
		maxEndingHere += num
		if maxEndingHere < num {
			maxEndingHere = num
		}
		if maxSoFar < maxEndingHere {
			maxSoFar = maxEndingHere
		}
	}
	fmt.Println(maxSoFar)
}
