#! /usr/bin/env python


# Help function for quick sort
def part(part_list, begin, end):
    # We will pass through list starting from begin+1
    pivot = begin
    # Start range from begin+1, because we need to compare all members 
    for i in range(begin+1, end+1):

        if part_list[i] <= part_list[begin]:
            pivot += 1
            part_list[i], part_list[pivot] = part_list[pivot], part_list[i]
    # After loop we separate list in 2 parts
    # In left part will be elements that less then list[pivot]
    # In right part will be more than pivot element
    part_list[pivot], part_list[begin] = part_list[begin], part_list[pivot]
    return pivot


def quick_sort_low_memory(lst, bgn, end=None):
    if end is None:
        end = len(lst) - 1
    if bgn >= end:
        return
    # Sort list in 2 parts
    pivot = part(lst, bgn, end)
    # Sort recursively left part of list
    quick_sort_low_memory(lst, bgn, pivot-1)
    # Sort recursively right part of list
    quick_sort_low_memory(lst, pivot+1, end)
    return lst


def main():
    unordered_list = [9, 3, 45, 2, 97, 6, 75, 98, 12, 54, 32, 71, 66, 13, 45, 74, 63, 79, 4, 1, 7, 41]
    qsort = quick_sort_low_memory(lst=unordered_list, bgn=0)
    print(unordered_list)

if __name__ == "__main__":
    main()
