def calc_sum(nums, index=0):
    if index == len(nums) - 1:
        return nums[index]

    return nums[index] + calc_sum(nums, index + 1)
numbers = [int(x) for x in input().split()]

print(calc_sum(numbers))
