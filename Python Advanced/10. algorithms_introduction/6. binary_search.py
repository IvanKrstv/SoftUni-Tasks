def binary_search(arr, t):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        mid_el = arr[mid]
        if mid_el == t:
            return mid
        elif mid_el > t:
            right = mid - 1
        else:
            left = mid + 1

    return -1

numbers = [int(x) for x in input().split()]
target = int(input())
print(binary_search(numbers, target))