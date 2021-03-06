#! /usr/bin/env python
'''
I want to learn some algorithms, so I compare them sorting list
Module for testing different algorithms
'''
from copy import copy
import timeit


from typing import List, Optional
unordered_list = [9, 34, 42, 56, 22, 87, 43, 21, 89, 76, 45, 456,
                  2, 97, 6, 75, 98, 12, 54, 32, 71, 66, 13, 334,
                  45, 74, 63, 79, 4, 1, 7, 41, 55, 75, 32, 78, 677,
                  56, 72, 97, 111, 687, 214, 99, 2, 1111, 6578, 455]

quick_sort_low_memory_unordered_list = copy(unordered_list)
quick_sort_high_memory_unordered_list = copy(unordered_list)
bubble_sort_unordered_list = copy(unordered_list)
insertion_sort_unordered_list = copy(unordered_list)
selection_sort_unordered_list = copy(unordered_list)
merge_sort_high_memory_unordered_list = copy(unordered_list)


def swap(lst: List[int], left: int, right: int) -> List[int]:
    '''
    Change list elements
    '''
    if left != right:
        lst[left], lst[right] = lst[right], lst[left]
    return lst


# Quick Sort Part
def part(part_list: List[int], begin: int, end: int) -> int:
    '''
    Help function for quick sort
    '''
    # We will pass through list starting from begin+1
    pivot = begin
    # Start range from begin+1, because we need to compare all members
    for i in range(begin + 1, end + 1):

        if part_list[i] <= part_list[begin]:
            pivot += 1
            swap(part_list, i, pivot)
    # After loop we separate list in 2 parts
    # In left part will be elements that less then list[pivot]
    # In right part will be more than pivot element
    swap(part_list, begin, pivot)
    return pivot


def quick_sort_low_memory(lst: List[int], bgn: int, end: Optional[int] = None) -> Optional[List[int]]:
    '''
    Use minimal memory, only move elements
    '''
    if end is None:
        end = len(lst) - 1
    if bgn >= end:
        return
    # Sort list in 2 parts
    pivot = part(lst, bgn, end)
    # Sort recursively left part of list
    quick_sort_low_memory(lst, bgn, pivot - 1)
    # Sort recursively right part of list
    quick_sort_low_memory(lst, pivot + 1, end)
    return lst


def quick_sort_high_memory(lst: List[int]) -> List[int]:
    '''
    Use more memory, create new lists
    '''
    if not lst:
        return []
    # Found all elements equal to first element
    pivots = [x for x in lst if x == lst[0]]
    # Sort recursively all less members
    less = quick_sort_high_memory([x for x in lst if x < lst[0]])
    # Sort recursively all greater elements
    great = quick_sort_high_memory([x for x in lst if x > lst[0]])

    # Join lists
    return less + pivots + great


def bubble_sort(lst: List[int]) -> List[int]:
    '''
    Bubble sort method
    '''
    for l1, val in enumerate(lst):
        for l, value in enumerate(lst):
            if lst[l] > lst[l1]:
                swap(lst, l, l1)
    return lst


def insertion_sort(lst: List[int]) -> List[int]:
    sort_end_index = 1

    def insert_index(lst, value):
        for i in range(len(lst)):
            if lst[i] >= value:
                return i

    while sort_end_index < len(lst):
        value = lst[sort_end_index]
        if value < lst[sort_end_index - 1]:
            index = insert_index(lst, value)
            del lst[sort_end_index]
            lst.insert(index, value)
        sort_end_index += 1
    return lst


def selection_sort(lst: List[int]) -> List[int]:
    '''
    Selection sort algorithm
    '''
    sort_end_index = 0
    end = len(lst)

    while sort_end_index < end:
        smallest = lst[sort_end_index]
        smallest_index = sort_end_index

        for i in range(sort_end_index, end):
            if smallest > lst[i]:
                smallest = lst[i]
                smallest_index = i

        swap(lst, sort_end_index, smallest_index)
        sort_end_index += 1
    return lst


def merge_sort_high_memory(lst: List[int]) -> Optional[List[int]]:
    '''
    Merge sort algorithm, memory unoptimized
    '''
    def merge(lst, left, right):
        lindex, rindex, target_index = 0, 0, 0
        llen, rlen = len(left), len(right)
        remaining = llen + rlen
        while remaining > 0:
            if lindex >= llen:
                lst[target_index] = right[rindex]
                rindex += 1
            elif rindex >= rlen:
                lst[target_index] = left[lindex]
                lindex += 1
            elif left[lindex] < right[rindex]:
                lst[target_index] = left[lindex]
                lindex += 1
            else:
                lst[target_index] = right[rindex]
                rindex += 1
            target_index += 1
            remaining -= 1
        return lst

    lenght = len(lst)
    if lenght > 1:
        left_size = lenght // 2
        right_size = lenght - left_size
        left = lst[:left_size]
        right = lst[-right_size:]
        merge_sort_high_memory(left)
        merge_sort_high_memory(right)

        merge(lst, left, right)
        return lst


def main() -> None:
    '''
    Start point of script
    '''

    print('Unordered list')
    print(unordered_list)
    print()

    print('Start sorting test')
    print()

    print('quick_sort_low_memory')
    print(quick_sort_low_memory(quick_sort_low_memory_unordered_list, bgn=0))
    print(timeit.timeit('quick_sort_low_memory(quick_sort_low_memory_unordered_list, bgn=0)', number=100000, globals=globals()))
    print()

    print('quick_sort_high_memory')
    print(quick_sort_high_memory(quick_sort_high_memory_unordered_list))
    print(timeit.timeit('quick_sort_high_memory(quick_sort_high_memory_unordered_list)', number=100000, globals=globals()))
    print()

    print('bubble_sort')
    print(bubble_sort(bubble_sort_unordered_list))
    print(timeit.timeit('bubble_sort(bubble_sort_unordered_list)', number=100000, globals=globals()))
    print()

    print('insertion_sort')
    print(insertion_sort(insertion_sort_unordered_list))
    print(timeit.timeit('insertion_sort(insertion_sort_unordered_list)', number=100000, globals=globals()))
    print()

    print('selection_sort')
    print(selection_sort(selection_sort_unordered_list))
    print(timeit.timeit('selection_sort(selection_sort_unordered_list)', number=100000, globals=globals()))
    print()

    print('merge_sort_high_memory')
    print(merge_sort_high_memory(merge_sort_high_memory_unordered_list))
    print(timeit.timeit('merge_sort_high_memory(merge_sort_high_memory_unordered_list)', number=100000, globals=globals()))
    print()


if __name__ == '__main__':
    main()
