def min_product_of_two(nums):
    min1 = min2 = float('inf')
    for i in nums:
        if i <= min1:
            min1, min2 = i, min1
        elif min1 <= i <= min2:
            min2 = i
    return min1 * min2


def third_max_value(nums):
    max1 = max2 = max3 = float('-inf')
    for i in nums:
        if i >= max1:
            max1, max2, max3 = i, max1, max2
        elif max2 <= i <= max1:
            max2, max3 = i, max2
        elif max3 <= i <= max2:
            max3 = i
    return max3


def find_silver_score(scores):
    max1 = max2 = 0
    for i in scores:
        if i > max1:
            max1, max2 = i, max1
        elif max1 > i > max2:
            max2 = i
    return max2


def max_product_of_two(nums):
    max1 = max2 = float("-Inf")
    min1 = min2 = float("Inf")
    for i in nums:
        if i >= max1:
            max1, max2 = i, max1
        elif i >= max2:
            max2 = i

        if i <= min1:
            min1, min2 = i, min1
        elif i <= min2:
            min2 = i

    return max(min1 * min2, max1 * max2)


def max_product_of_three(nums):
    max1 = max2 = max3 = float("-Inf")
    min1 = min2 = float("Inf")
    for i in nums:
        if i >= max1:
            max1, max2, max3 = i, max1, max2
        elif i >= max2:
            max2, max3 = i, max2
        elif i >= max3:
            max3 = i

        if i <= min1:
            min1, min2 = i, min1
        elif i <= min2:
            min2 = i

    return max(min1 * min2 * max1, max1 * max2 * max3)
