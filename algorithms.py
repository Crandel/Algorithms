#! /usr/bin/env python
'''
I want to learn some algorithms, so I compare them sorting list
Module for testing different algorithms
'''
from copy import copy
from time import time


def swap(lst, left, right):
    '''
    Change list elements
    '''
    if left != right:
        lst[left], lst[right] = lst[right], lst[left]
    return lst


# Quick Sort Part
def part(part_list, begin, end):
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


def quick_sort_low_memory(lst, bgn, end=None):
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


def quick_sort_high_memory(lst):

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


def bubble_sort(lst):
    '''
    Bubble sort method
    '''
    for l1, val in enumerate(lst):
        for l, value in enumerate(lst):
            if lst[l] > lst[l1]:
                swap(lst, l, l1)
    return lst


def insertion_sort(lst):
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


def main():
    '''
    Start point of script
    '''
    unordered_list = [9, 34, 42, 56, 22, 87, 43, 21, 89, 76, 45, 456,
                      2, 97, 6, 75, 98, 12, 54, 32, 71, 66, 13, 334,
                      45, 74, 63, 79, 4, 1, 7, 41, 55, 75, 32, 78, 677,
                      56, 72, 97, 111, 687, 214, 99, 2, 1111, 6578, 455]
    stime = time()

    qsort_low = quick_sort_low_memory(lst=copy(unordered_list), bgn=0)
    qsort_low_time = time()
    print(qsort_low)
    print('quick_sort_low_memory {} seconds'.format(round(qsort_low_time - stime, 6)))
    print('--------------------------------------------')
    print('')

    qsort_more = quick_sort_high_memory(lst=copy(unordered_list))
    qsort_more_time = time()
    print(qsort_more)
    print('quick_sort_high_memory {} seconds'.format(round(qsort_more_time - qsort_low_time, 6)))
    print('/////////////////////////////////////////////')
    print('')

    bubble_res = bubble_sort(lst=copy(unordered_list))
    bubble_time = time()
    print(bubble_res)
    print('bubble sort {} seconds'.format(round(bubble_time - qsort_more_time, 6)))
    print('*********************************************')
    print('')

    insertion_res = insertion_sort(lst=copy(unordered_list))
    insertion_time = time()
    print(insertion_res)
    print('insertion sort {} seconds'.format(round(insertion_time - bubble_time, 6)))
    print('++++++++++++++++++++++++++++++++++++++++++++')
    print('')

    print(unordered_list)
    print('unordered_list')


if __name__ == "__main__":
    main()
