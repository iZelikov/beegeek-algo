# def jump_search(nums, target):
#     block_size = int(len(nums) ** 0.5)
#     left = 0
#     right = block_size - 1
#     while nums[right] > target:
#         left = right + 1
#         right = min(right + block_size, len(nums) - 1)
#         if left >= len(nums):
#             return -1
#
#     for i in range(left, right + 1):
#         if nums[i] == target:
#             return i
#
#     return -1


def jump_search(nums, target):
    block_size = int(len(nums) ** 0.5)
    left = 0
    right = block_size - 1
    while nums[~right] > target:
        left = right + 1
        right = min(right + block_size, len(nums) - 1)
        if left >= len(nums):
            return -1

    for i in range(left, right + 1):
        if nums[~i] == target:
            return len(nums) + ~i

    return -1
