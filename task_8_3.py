def insertion_sort(nums):
    for i in range(1, len(nums)):
        item = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < item:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item


def binary_insertion_sort(nums):
    def find_insertion_position(left, right):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[right] <= item:
                return right
            elif nums[mid] > item:
                right = mid - 1
            else:
                left = mid
                right -= 1
        return -1

    for i in range(1, len(nums)):
        item = nums[i]
        last = find_insertion_position(0, i - 1)
        for j in range(i - 1, last, -1):
            nums[j + 1] = nums[j]
        nums[last + 1] = item

def section_sort(nums):
    for i in range(1, len(nums)):
        item = nums[i]
        if item == 0:
            continue
        j = i - 1
        while j >= 0 and nums[j] > item:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item