# Linear - performance = O(n)

def linear_search(nums, target):
    for idx, num in enumerate(nums):
        if num == target:
            return idx
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 9]
target = 5

print(linear_search(nums, target))


# Binary search - peformance - O(log(n))  - only ordered data structure
# first index + last index / 2
# [1,2,3,4,5]
# L    M,L  R

def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = nums[mid_idx]

        if mid_el == target:
            return mid_idx

        if target > mid_el:
            left = mid_idx + 1
        else:
            right = mid_idx - 1
    return -1


nums = [int(x) for x in input().split()]
target = int(input())
print(binary_search(nums, target))

# Selection Sort

nums = [int(x) for x in input().split()]

for idx in range(len(nums)):
    current_number = nums[idx]
    min_number = current_number
    min_idx = idx
    for next_idx in range(idx + 1, len(nums)):
        next_number = nums[next_idx]
        if next_number < min_number:
            min_number = next_number
            min_idx = next_idx
    nums[idx], nums[min_idx] = nums[min_idx], nums[idx]

print(*nums, sep=' ')

for idx in range(len(nums)):
    min_idx = idx
    for curr_idx in range((idx + 1), len(nums)):
        if nums[curr_idx] < nums[min_idx]:
            nums[idx], nums[min_idx] = num[min_idx], nums[idx]

# Bubble Sort - two indexes - time O(n^2), memory O(1)

nums = [int(x) for x in input().split()]

is_sorted = False
counter = 0  # filed idex in the end

while not is_sorted:
    is_sorted = True
    for idx in range(1, len(nums) - counter):
        if nums[idx] < nums[idx - 1]:
            nums[idx], nums[idx - 1] = nums[idx - 1], nums[idx]
            is_sorted = False
    counter += 1

print(*nums, sep=' ')

# Bubble sort 2

nums = [1, 2, 3, 4, 2, 5, 6]
for i in range(len(nums)):
    for j in range(1, len(nums) - i):
        if nums[j - 1] > nums[j]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]

# Insertion sort

nums = [int(x) for x in input().split()]

for i in range(1, len(nums)):
    for j in range(i, 0, -1):
        if nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
        else:
            break  # not so much iteration if the first are sorted
print(*nums, sep=' ')

# Insertion sort 2

for i in ragne(len(nums)):
    j = 1
    while j > 0 and nums[j] < nums[j - 1]:
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
        j -= 1


#  Quick sort - Memory: O(log(n)), Time(n^^2)


def quick_sort(start, end, nums):
    if start >= end:
        return
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1

    nums[pivot], nums[right] = nums[right], nums[pivot]
    quick_sort(start, right - 1, nums)
    quick_sort(left, end, nums)


nums = [int(x) for x in input().split()]
quick_sort(0, len(nums) - 1, nums)
print(*nums, sep='')


#  Quick sort - 2

def quick_sort(nums, start, end):
    if start >= end:
        return
    pivot, left, right = start, strat + 1, end
    while left <= right:
        if nums[left] > nums[pivot] > nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
        if nums[left] <= nums[pivot]:
            left += 1
        if nums[right] >= nums[pivot]:
            right -= 1
        nums[pivot], nums[right] = nums[right], nums[pivot]
        quick_sort(nums, start, right - 1)
        quick_sort(nums, right + 1, end)


# Merge Sort - Memory(O(n)/O(n*log n) - Time:O(n*logn)
def merge_arrays(left, right):
    result = [None] * (len(left) + len(right))

    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < (len(right)):
        if left[left_idx] < right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1
        else:
            result[result_idx] = right[right_idx]
            right_idx += 1
        result_idx += 1

    while left_idx < len(left):
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    while right_idx < len(right):
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    return result


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid_idx = len(nums) // 2
    left = nums[:mid_idx]
    right = nums[mid_idx:]

    return merge_arrays(merge_sort(left), merge_sort(right))


nums = [int(x) for x in input().split()]
result = merge_sort(nums)
print(*result, sep=' ')


# Merge sort 2 - Memory O(n*logn)
def merge_sort(nums):
    if len(nums) == 1:
        return nums
    mid_idx = len(nums) // 2
    left = num[:mid_idx]
    right = num[mid_idx:]
    return merge_arrays(merge_sort(left), merge_sort(right))

