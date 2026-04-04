import math


def count_maxes(nums):
    m = float('-inf')
    count = 0
    for i in nums:
        if i == m:
            count += 1
        elif i > m:
            m = i
            count = 1
    return count


def min_rectangle(points):
    left = right = points[0][0]
    top = bottom = points[0][1]
    for p in points:
        left = min(p[0], left)
        right = max(p[0], right)
        top = max(p[1], top)
        bottom = min(p[1], bottom)

    return [(left, bottom), (right, top)]


def min_distance_between_peaks(nums):
    peak = None
    min_dist = len(nums)
    for i in range(1, len(nums) - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            if peak:
                min_dist = min(min_dist, i - peak)
            peak = i

    return (-1, min_dist)[min_dist < len(nums)]


def count_numbers_with_equal_halves(n):
    count = 0
    top = 10
    for i in range(1, n):
        if i == top:
            top *= 10
        if i * top + i > n:
            break
        count += 1
    return count


def min_product_of_three(nums):
    min1 = min2 = min3 = float('inf')
    max1 = max2 = float('-inf')
    for i in nums:
        if i > max1:
            max1, max2 = i, max1
        elif i > max2:
            max2 = i

        if i < min1:
            min1, min2, min3 = i, min1, min2
        elif i < min2:
            min2, min3 = i, min2
        elif i < min3:
            min3 = i

    return min(min1 * min2 * min3, max1 * max2 * min1)


# def count_triplets(n):
#     count = 0
#     for a in range(1, n):
#         count += (n - 1) // a
#     return count

def count_triplets(nums1, nums2, nums3):
    def b_search(arr, target, desc=False):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if desc:
                if arr[right] < target:
                    return right
                elif arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid
                    right -= 1
            else:
                if arr[left] > target:
                    return left
                elif arr[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
                    left += 1
        return -1

    count = 0
    for j in range(len(nums2)):
        i = b_search(nums1, nums2[j], desc=True)
        if i == -1:
            continue
        k = b_search(nums3, nums2[j])
        if k == -1:
            continue
        count += (i + 1) * (len(nums3) - k)
    return count


def count_triangles(lines):
    def b_search(left, target):
        right = len(lines) - 1
        if lines[left] >= target:
            return left - 1
        while left <= right:
            mid = left + (right - left) // 2
            if lines[right] < target:
                return right
            elif lines[mid] >= target:
                right = mid - 1
            else:
                left = mid
                right -= 1

    count = 0
    for a in range(len(lines) - 2):
        for b in range(a + 1, len(lines) - 1):
            idx = b_search(b + 1, lines[a] + lines[b])
            count += idx - b
    return count
