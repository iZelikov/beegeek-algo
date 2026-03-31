# def matrix_search(matrix, target):
#     for row in matrix:
#         left, right = 0, len(row) - 1
#         while left <= right:
#             mid = left + (right - left) // 2
#             if row[mid] == target:
#                 return True
#             elif row[mid] < target:
#                 left = mid + 1
#             else:
#                 right = mid - 1
#     return False


def triangle_of_coins(n):
    return int((((1 + 8 * n) ** 0.5 - 1) / 2))


def ternary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3
        if nums[mid1] == target:
            return True
        elif nums[mid2] == target:
            return True
        elif target < nums[mid1]:
            right = mid1 - 1
        elif target > nums[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1
    return False


def get_closest_element(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    l = nums[left - 1:left + 1]
    return min(l, key=lambda x: (abs(x - target), -x), default=nums[left])


def lower_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return (-1, right)[nums[right] == target]


def upper_bound(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        m_value = nums[mid]
        r_value = nums[right]
        if r_value == target:
            return right
        elif m_value < target:
            left = mid + 1
        elif m_value > target:
            right = mid - 1
        elif m_value == target and r_value > target:
            left = mid
            right -= 1
    return -1


def search_insert_position(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return left if nums[left] >= target else left + 1


def equal(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        m = nums[mid]
        if nums[left] == left:
            return left
        elif m < mid:
            left = mid + 1
        elif m > mid:
            right = mid - 1
        elif m == mid:
            right = mid
    return -1


def prefix_search(strings: list[str], prefix: str) -> str | None:
    left, right = 0, len(strings) - 1
    while left <= right:
        mid = left + (right - left) // 2
        m = strings[mid]
        if strings[left].startswith(prefix):
            return strings[left]
        elif m.startswith(prefix):
            right = mid
        elif m < prefix:
            left = mid + 1
        else:
            right = mid - 1
    return None


def is_stable_version(version):
    return version <= 2325


def find_unstable(max_version):
    left, right = 0, max_version + 1
    while left < right:
        mid = left + (right - left) // 2
        if not is_stable_version(left):
            return left
        elif is_stable_version(mid):
            left = mid + 1
        else:
            right = mid
    return right


def special_list(nums):
    if nums[0] >= len(nums):
        return True
    left = 1
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        mid_value = nums[mid]
        prev_value = nums[mid - 1]
        elements_count = len(nums) - mid
        if mid_value >= elements_count > prev_value:
            return True
        elif mid_value < elements_count:
            left = mid + 1
        else:
            right = mid - 1
    return False


def is_majority_element(nums, target):
    left = 0
    right = len(nums) - 1
    lm = rm = right // 2
    if nums[lm] != target:
        return False
    while left < lm or right > rm:
        mid = left + (lm - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            lm = mid
        mid = rm + (right - rm) // 2
        if nums[right] == target:
            rm = right
        elif nums[mid] > target:
            right = mid - 1
        else:
            right -= 1
            rm = mid
    return right - left + 1 > len(nums) // 2


def matrix_search(matrix, target):
    n = len(matrix)
    left = 0
    right = n ** 2 - 1
    while left <= right:
        mid = left + (right - left) // 2
        row = mid // n
        col = mid % n
        m = matrix[row][col]
        if m == target:
            return True
        elif m < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def find_min(nums):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        l = nums[left]
        r = nums[right]
        m = nums[mid]
        if l <= m <= r:
            return l
        elif r <= m <= l:
            return r
        elif m < r < l:
            right = mid
        elif r < l < m:
            left = mid + 1
    return nums[left]

def find_number(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        l = nums[left]
        r = nums[right]
        m = nums[mid]
        if l == target:
            return left
        elif m == target:
            return mid
        elif r == target:
            return right
        elif l < target < m:
            right = mid -1
        elif m < target < r:
            left = mid + 1
        elif l >= m:
            right = mid -1
        elif m >= r:
            left = mid + 1
    return (-1, left)[nums[left] == target]
