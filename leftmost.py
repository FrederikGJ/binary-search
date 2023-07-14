# The leftmost binary search is a variant of the standard binary search algorithm, 
#designed for efficient searching in sorted lists, particularly those with many repeated instances of the same value. 
#This algorithm is advantageous when one needs to find the first or 'leftmost' occurrence of a particular value within the list.

def leftmost_binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    if arr[left] == target:
        return left
    else:
        return -1
