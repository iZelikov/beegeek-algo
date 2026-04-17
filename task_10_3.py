from collections import Counter
from random import randint

from timer import timer


def count_pairs_with_sum(nums, k):
    i, j = 0, len(nums) - 1
    count = 0
    while i < j:
        s = nums[i] + nums[j]
        if s == k:
            count += 1
            i += 1
            j -= 1
        elif s < k:
            i += 1
        else:
            j -= 1
    return count


def have_common_element(nums1, nums2):
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            return True
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return False


def move_zeros(nums):
    i = j = 0
    while j < len(nums):
        if nums[j] == 0:
            j += 1
        elif nums[i] == 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        else:
            i += 1
            j += 1


def sort_half_sorted(nums):
    i = 0
    j = (len(nums) + 1) // 2
    result = []
    while i < (len(nums) + 1) // 2 and j < len(nums):
        if nums[i] < nums[j]:
            result.append(nums[i])
            i += 1
        else:
            result.append(nums[j])
            j += 1
    return result + nums[i: (len(nums) + 1) // 2] + nums[j: len(nums)]


def merge_sorted_lists(nums1, nums2, nums3=None):
    i = j = 0
    result = []
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1
    result += nums1[i:] + nums2[j:]
    if nums3:
        return merge_sorted_lists(nums3, result)
    else:
        return result


def card_game_results(cards):
    def move():
        nonlocal i, j
        if i > j:
            return 0
        elif cards[i] > cards[j]:
            i += 1
            return cards[i - 1]
        else:
            j -= 1
            return cards[j + 1]

    i = 0
    j = len(cards) - 1
    a = t = 0
    while i <= j:
        t += move()
        a += move()
    return t, a


def alternate_order(nums):
    return [nums[i // 2 - i * (i % 2)] for i in range(len(nums))]


def reverse_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = list(s)
    i = 0
    j = len(s) - 1
    while i < j:
        if result[i] not in vowels:
            i += 1
        elif result[j] not in vowels:
            j -= 1
        else:
            result[i], result[j] = result[j], result[i]
            i += 1
            j -= 1
    return "".join(result)


def is_almost_palindrome(s, i=0, k=None):
    j = k or len(s) - 1
    while i < j:
        if s[i] != s[j]:
            if k:
                return False
            else:
                return is_almost_palindrome(s, i + 1, j) or is_almost_palindrome(s, i, j - 1)
        i += 1
        j -= 1
    return True


def is_flippable_number(num):
    d = {'0': '0', '6': '9', '9': '6'}
    i = 0
    j = len(num) - 1
    while i <= j:
        if num[i] != d[num[j]]:
            return False
        i += 1
        j -= 1
    return True


def min_original_size(s):
    d = {'0': '1', '1': '0'}
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != d[s[j]]:
            return j - i + 1
        i += 1
        j -= 1
    return j - i + 1


def duplicate_zeros(nums: list[int]):
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums[i] == 0:
            j -= 1
        i += 1
    if i == j:
        nums[-1] = nums[j]
        i = j - 1
        j = len(nums) - 2
    else:
        i = j
        j = len(nums) - 1

    while j > i >= 0:
        if nums[i] == 0:
            nums[j] = 0
            j -= 1
        nums[j] = nums[i]
        j -= 1
        i -= 1


def could_type(word, typed):
    i = 0
    j = 0
    while i < len(word) and j < len(typed):
        if word[i] == typed[j]:
            c = word[i]
            n = k = 0
            while i < len(word) and word[i] == c:
                n += 1
                i += 1
            while j < len(typed) and typed[j] == c:
                k += 1
                j += 1
            if k < n:
                return False
        else:
            return False
    return i == len(word) and j == len(typed)


def sort_numbers_from_one_to_three(nums):
    i = 0
    j = 0
    for n in range(1, 4):
        while j < len(nums):
            if nums[i] == n:
                i += 1
                j += 1
            elif nums[j] == n:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            else:
                j += 1
        j = i

