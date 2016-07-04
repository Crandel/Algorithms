package main

import (
	"fmt"
)

func bubbleSort(lst []int8) []int8 {
	for key := range lst {
		for l := range lst {
			if lst[l] > lst[key] {
				lst[l], lst[key] = lst[key], lst[l]
			}
		}
	}
	return lst
}

func qsort(lst []int8) []int8 {
	// this check for recursion
	if len(lst) < 2 {
		return lst
	}
	// first and last index of slice
	l, r := 0, len(lst)-1
	// control element is a middle of slice
	pivot := len(lst) / 2
	// move control element to right
	lst[pivot], lst[r] = lst[r], lst[pivot]

	for i, v := range lst {
		if v < lst[r] {
			lst[i], lst[l] = lst[l], lst[i]
			l++
		}
	}

	lst[l], lst[r] = lst[r], lst[l]
	// list was separated in 2 parts
	// in left part we have elements less than lst[l]
	// in right - more than it

	// sort left part recursively
	qsort(lst[:l])
	// sort right part recursively
	qsort(lst[l+1:])
	return lst
}

func main() {
	lst := []int8{9, 34, 42, 56, 22, 87, 43, 21, 89, 76, 45, 2, 97, 6, 75, 98, 12, 54, 32, 71, 66, 13, 45, 74, 63, 79, 4, 1, 7, 41}
	fmt.Println(lst)
	qArray := qsort(lst)
	fmt.Println(qArray)
	bArray := bubbleSort(lst)
	fmt.Println(bArray)
}
