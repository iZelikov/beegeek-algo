def find_not_min_max(nums):
    mn = min(nums)
    mx = max(nums)
    for i in nums:
        if (i != mn) and (i != mx):
            return i


def min_difference(num):
    for dif1 in range(2, round(num ** 0.5) + 1):
        if num % dif1 == 0:
            dif2 = num // dif1
            return min(dif1 - 1, dif2 - dif1) if dif2 - dif1 else dif1 - 1
    return num - 1


# def max_difference(nums):
#     def next_min_max(start=0, minmax=0):
#         for j in range(start, len(nums)):
#             l = nums[j - 1:j + 2]
#             if nums[j] == (min(l), max(l))[minmax]:
#                 return j
#         return -1
#
#     i = 0
#     global_min = nums[0]
#     global_max = nums[0]
#     global_dif = global_max - global_min
#     while i != -1:
#         i = next_min_max(i + 1, 0)
#         local_min = nums[i]
#         if i != -1:
#             i = next_min_max(i + 1, 1)
#         local_max = nums[i]
#         dif1 = global_max - global_min
#         dif2 = local_max - local_min
#         dif3 = local_max - global_min
#         if dif2 == max(dif1, dif2, dif3):
#             global_min, global_max = local_min, local_max
#             if dif2 > global_dif:
#                 global_dif = dif2
#         elif dif3 == max(dif1, dif2, dif3):
#             global_max = local_max
#             if dif3 > global_dif:
#                 global_dif = dif3
#         elif local_min < global_min:
#             global_min, global_max = local_min, local_max
#
#     return (-1, global_dif)[global_dif > 0]

def max_difference(nums):
    global_min = nums[0]
    global_diff = 0
    for i in nums:
        dif = i - global_min
        if dif > global_diff:
            global_diff = dif
        if i < global_min:
            global_min = i
    return (-1, global_diff)[global_diff > 0]


def get_closest_element(nums, target):
    closest = float('-inf')
    for num in nums:
        if abs(target - num) < abs(closest - target):
            closest = num
        elif abs(target - num) == abs(closest - target) and num > closest:
            closest = num
    return closest


def steps_to_max(nums):
    mx = nums[0]
    steps = 0
    for i, v in enumerate(nums):
        if v > mx:
            steps += (v - mx) * i
            mx = v
        elif v < mx:
            steps += mx - v
    return steps


def max_divider(nums):
    divider = min(nums)
    for i in nums:
        if i % divider:
            return -1
    return divider


def max_ascending_sum(nums):
    max_sum = 0
    asc_sum = 0
    last = None
    for i in nums:
        if last is None or i > last:
            asc_sum += i
        else:
            if asc_sum > max_sum:
                max_sum = asc_sum
            asc_sum = i
        last = i
    return max(max_sum, asc_sum)


# def max_sum(nums):
#     max_s = 0
#     pos_s = 0
#     start = False
#     finish = False
#     for i in nums:
#         if not start and i < 0:
#             start = True
#             pos_s = 0
#         elif start and i >= 0:
#             pos_s += i
#         elif start and i < 0:
#             if pos_s > max_s:
#                 max_s = pos_s
#             pos_s = 0
#             finish = True
#     return (-1, max_s)[finish]

def restore_values(nums):
    add = min(nums) // 2
    return [i - add for i in nums]


def max_sum(pairs):
    raw_sum = sum(max(i) for i in pairs)
    if raw_sum % 3:
        return raw_sum
    min_tune = raw_sum
    for pair in pairs:
        tune = max(pair) - min(pair)
        if tune < min_tune and tune % 3:
            min_tune = tune
    return (-1, raw_sum - min_tune)[min_tune != raw_sum]