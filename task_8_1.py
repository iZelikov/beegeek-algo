def selection_sort(nums):
    for i in range(len(nums) - 1):
        max_i = i
        for j in range(i, len(nums)):
            if nums[j] > nums[max_i]:
                max_i = j
        if i != max_i:
            nums[i], nums[max_i] = nums[max_i], nums[i]


def sum_of_seven_smallest(nums):
    s = 0
    for i in range(7):
        max_i = i
        for j in range(i, len(nums)):
            if nums[j] < nums[max_i]:
                max_i = j
        s += nums[max_i]
        if i != max_i:
            nums[i], nums[max_i] = nums[max_i], nums[i]
    return s


def sort_by_digit_and_value(nums):
    for i in range(len(nums) - 1):
        max_i = i
        for j in range(i, len(nums)):
            if (abs(nums[j]) % 10, -nums[j]) > (abs(nums[max_i]) % 10, -nums[max_i]):
                max_i = j
        if i != max_i:
            nums[i], nums[max_i] = nums[max_i], nums[i]


def sort_like_nums(nums):
    def key(x):
        if isinstance(x, list):
            return x[0], 1
        return x, 0

    for i in range(len(nums) - 1):
        min_i = i
        for j in range(i, len(nums)):
            if key(nums[j]) < key(nums[min_i]):
                min_i = j
        if i != min_i:
            nums[i], nums[min_i] = nums[min_i], nums[i]


import operator


def alter_sort(nums):
    for i in range(len(nums) - 1):
        alter_i = i
        op = (operator.gt, operator.lt)[i % 2]
        for j in range(i, len(nums)):
            if op(nums[j], nums[alter_i]):
                alter_i = j
        if i != alter_i:
            nums[i], nums[alter_i] = nums[alter_i], nums[i]


def sort_except_one(nums, k):
    for i in range(len(nums) - 1):
        if i == k: continue
        min_i = i
        for j in range(i, len(nums)):
            if j == k: continue
            if nums[j] < nums[min_i]:
                min_i = j
        if i != min_i:
            nums[i], nums[min_i] = nums[min_i], nums[i]


def sort_only_odds(nums):
    for i in range(len(nums) - 1):
        if nums[i] % 2 == 0: continue
        min_i = i
        for j in range(i, len(nums)):
            if nums[j] % 2 == 0: continue
            if nums[j] < nums[min_i]:
                min_i = j
        if i != min_i:
            nums[i], nums[min_i] = nums[min_i], nums[i]


def sort_by_parity(nums):
    for i in range(len(nums) - 1):
        alter_i = i
        for j in range(i, len(nums)):
            if nums[i] % 2 == 0 and nums[j] % 2 == 0:
                if nums[j] > nums[alter_i]:
                    alter_i = j
            elif nums[i] % 2 == 1 and nums[j] % 2 == 1:
                if nums[j] < nums[alter_i]:
                    alter_i = j
        if i != alter_i:
            nums[i], nums[alter_i] = nums[alter_i], nums[i]


def sort_by_index(nums):
    for i in range(len(nums) - 1):
        alter_i = i
        for j in range(i, len(nums)):
            if i % 2 == 0 and j % 2 == 0:
                if nums[j] < nums[alter_i]:
                    alter_i = j
            elif i % 2 == 1 and j % 2 == 1:
                if nums[j] > nums[alter_i]:
                    alter_i = j
        if i != alter_i:
            nums[i], nums[alter_i] = nums[alter_i], nums[i]


def sort_grades(nums):
    def key(x: str):
        opt = {'-': 1, '+': -1}
        result = [x[0], opt.get(x[-1], 0)]
        return result

    for i in range(len(nums) - 1):
        min_i = i
        for j in range(i, len(nums)):
            if key(nums[j]) < key(nums[min_i]):
                min_i = j
        if i != min_i:
            nums[i], nums[min_i] = nums[min_i], nums[i]


def book_count(prices, cash):
    count = 0
    for i in range(len(prices)):
        min_i = i
        for j in range(i, len(prices)):
            if prices[j] < prices[min_i]:
                min_i = j
        if i != min_i:
            prices[i], prices[min_i] = prices[min_i], prices[i]
        cash -= prices[i]
        if cash >= 0:
            count += 1
        else:
            break
    return count


def double_selection_sort(nums):
    for i in range(0, len(nums) - 1, 2):
        min_i_1 = i
        min_i_2 = i + 1
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_i_1]:
                min_i_1, min_i_2 = j, min_i_1
            elif i+1 < len(nums) and nums[j] < nums[min_i_2]:
                min_i_2 = j

        if i != min_i_1:
            nums[i], nums[min_i_1] = nums[min_i_1], nums[i]
        if i + 1 != min_i_2 and i + 1 < len(nums) and min_i_1 != min_i_2:
            if min_i_2 != i:
                nums[i + 1], nums[min_i_2] = nums[min_i_2], nums[i + 1]
            else:
                nums[i + 1], nums[min_i_1] = nums[min_i_1], nums[i + 1]


def two_sided_selection_sort(nums):
    for i in range(len(nums) // 2):
        min_i = i
        max_i = ~i
        for j in range(i + 1, len(nums) - i):
            if nums[j] < nums[min_i]:
                min_i = j
            if nums[~j] > nums[max_i]:
                max_i = ~j
        if i != min_i:
            nums[i], nums[min_i] = nums[min_i], nums[i]
        if ~i != max_i:
            if i != len(nums) + max_i:
                nums[~i], nums[max_i] = nums[max_i], nums[~i]
            else:
                nums[~i], nums[min_i] = nums[min_i], nums[~i]

