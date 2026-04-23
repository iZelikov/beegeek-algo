import math
from collections import Counter


def max_average_sublist(nums, k):
    m_av = av = sum(nums[x] for x in range(k))
    for i in range(len(nums) - k):
        av += (nums[i + k] - nums[i])
        m_av = max(av, m_av)
    return m_av / k


def negatives_count_in_every_sublist(nums, k):
    negs = [sum(nums[i] < 0 for i in range(k))]
    for i in range(len(nums) - k):
        negs.append(negs[-1] + (nums[i + k] < 0) - (nums[i] < 0))
    return negs


def shortest_sublist_with_greater_sum(nums, k):
    min_l = float('inf')
    i = j = 0
    cur_sum = 0
    while j <= len(nums):
        if cur_sum <= k:
            if j >= len(nums):
                break
            cur_sum += nums[j]
            j += 1
        else:
            min_l = min(min_l, j - i)
            cur_sum -= nums[i]
            i += 1

    return (-1, min_l)[min_l <= len(nums)]


def has_duplicates_within_range(nums, k):
    k = min(len(nums), k)
    sub = {nums[i] for i in range(k)}
    for i in range(len(nums) - k):
        sub.add(nums[i + k])
        if len(sub) < k + 1:
            return True
        else:
            sub.discard(nums[i])
    return False


def uniques_count_in_every_sublist(nums, k):
    k = k - 1
    freq = Counter(nums[i] for i in range(k))
    uniq = len(freq)
    result = []
    for i in range(len(nums) - k):
        freq[nums[i + k]] += 1
        uniq += freq[nums[i + k]] == 1
        result.append(uniq)
        freq[nums[i]] -= 1
        uniq -= freq[nums[i]] == 0
    return result


def contains_permutation(s1, s2):
    chars = Counter(s2)
    l = len(s2) - 1
    current = Counter(s1[i] for i in range(l))
    for i in range(len(s1) - l):
        current[s1[i + l]] += 1
        if current == chars:
            return True
        current[s1[i]] -= 1
    return False


def first_negative_in_every_sublist(nums, k):
    i = -1
    j = 0
    result = []
    while j < len(nums) and i < len(nums) - k:
        if nums[j] >= 0:
            if j == len(nums) - 1:
                i += 1
                result.append(0)
            else:
                j += 1
        else:
            if i + k < j:
                i += 1
                result.append(0)
            elif i == j:
                j += 1
            else:
                result.append(nums[j])
                i += 1
    return result


def longest_sublist_of_ones(binary_list):
    left = right = max_list = 0
    for i in binary_list:
        if i:
            right += 1
        else:
            max_list = max(max_list, left + right)
            left, right = right, 0
    max_list = max(max_list, left + right)
    return min(max_list, len(binary_list) - 1)


def count_sublists_with_sum(binary_list, k):
    left = right = 0
    sub_sum = 0
    count = 0
    if k == 0:
        for x in binary_list:
            if x:
                count += sub_sum * (sub_sum + 1) // 2
                sub_sum = 0
            else:
                sub_sum += 1
        count += sub_sum * (sub_sum + 1) // 2
        return count

    while right <= len(binary_list):
        if right < len(binary_list) and sub_sum < k:
            sub_sum += binary_list[right]
        elif sub_sum == k:
            l_zeros = r_zeros = 0
            while left < right and binary_list[left] == 0:
                left += 1
                l_zeros += 1

            while right < len(binary_list) and binary_list[right] == 0:
                right += 1
                r_zeros += 1
            count += (l_zeros + 1) * (r_zeros + 1)
            left += 1
        right += 1
    return count
