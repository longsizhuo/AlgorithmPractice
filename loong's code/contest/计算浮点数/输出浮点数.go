package main

import "fmt"

func main() {
	var n float64
	_, err := fmt.Scan(&n)
	if err != nil {
		return
	}
	fmt.Printf("%f\n", n)
	fmt.Printf("%.5f\n", n)
	fmt.Printf("%e\n", n)
	fmt.Printf("%g\n", n)
}
