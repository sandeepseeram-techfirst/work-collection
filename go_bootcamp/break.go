package main

import "fmt"

func main() {
	pow := make([]int, 10)
	for i := range pow {
		pow[i] = 1 << uint(i) 
		if pow[i] >= 16 {
			break //stop iterating over pow when it reaches 16
		}
	}
	fmt.Println(pow)
	// [1 2 4 8 16 0 0 0 0 0]
}