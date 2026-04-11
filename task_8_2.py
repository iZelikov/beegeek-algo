def bubble_sort(nums):
    for i in range(len(nums) - 1):
        flag = False
        for j in range(len(nums) - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True
        if not flag:
            break


def number_of_swaps(nums):
    n = len(nums)
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] > nums[j]:
                res += 1

    return res


def move_zeros(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j] == 0:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


def cocktail_sort(nums):
    for i in range(len(nums) - 1):
        swapped = False
        for j in range(i // 2, len(nums) - i // 2 - 1):
            if i % 2 == 0:
                idx_1, idx_2 = j, j + 1
            else:
                idx_1, idx_2 = ~j - 1, ~j
            if nums[idx_1] > nums[idx_2]:
                nums[idx_1], nums[idx_2] = nums[idx_2], nums[idx_1]
                swapped = True
        if not swapped:
            break


def sum_of_five_largest_and_smallest(nums):
    for i in range(10):
        for j in range(i // 2, len(nums) - i // 2 - 1):
            if i % 2 == 0:
                idx_1, idx_2 = j, j + 1
            else:
                idx_1, idx_2 = ~j - 1, ~j
            if nums[idx_1] > nums[idx_2]:
                nums[idx_1], nums[idx_2] = nums[idx_2], nums[idx_1]
    mins, maxes = 0, 0
    for i in range(5):
        mins += nums[i]
        maxes += nums[~i]
    return maxes, mins


def k_swaps_to_sort(n, k):
    nums = list(range(1, n + 1))
    for i in range(n - 1):
        for j in range(n - i - 1):
            if not k:
                return nums
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            k -= 1
    return nums


def largest_possible_number(nums):
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            s1 = str(nums[j])
            s2 = str(nums[j + 1])
            if s2 + s1 > s1 + s2:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return int("".join(map(str, nums)))


def sort_matrix(matrix):
    n = len(matrix)
    for i in range(n ** 2 - 1):
        swapped = False
        for j in range(n ** 2 - i - 1):
            y1, x1 = j // n, j % n
            y2, x2 = (j + 1) // n, (j + 1) % n
            if matrix[y1][x1] > matrix[y2][x2]:
                matrix[y1][x1], matrix[y2][x2] = matrix[y2][x2], matrix[y1][x1]
                swapped = True
        if not swapped:
            break
