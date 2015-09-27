package main

import (
	"fmt"
)

func part(lst []int, bgn int, end int) int {
	pivot := bgn
	fmt.Println(bgn, end)
	for i := bgn + 1; i < end; i++ {
		if lst[i] >= lst[bgn] {
			pivot++
			lst[pivot], lst[i] = lst[i], lst[pivot]
		}
	}
	lst[pivot], lst[bgn] = lst[bgn], lst[pivot]
	return pivot
}

func qsort_low(lst []int, bgn int, end int) []int {
	if end == 0 {
		end = len(lst)
	}
	if bgn >= end {
		var empty_slice []int
		return empty_slice
	}
	pivot := part(lst, bgn, end)
	fmt.Println(lst, bgn, end, len(lst), cap(lst), pivot)
	return lst
}

func main() {
	fmt.Println("Hello world")
	lst := []int{9, 34, 42, 56, 22, 87, 43, 21, 89, 76, 45, 2, 97, 6, 75, 98, 12, 54, 32, 71, 66, 13, 45, 74, 63, 79, 4, 1, 7, 41}
	new_array := qsort_low(lst, 1, 0)
	fmt.Println(new_array)
}
