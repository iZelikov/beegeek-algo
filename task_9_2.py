from itertools import pairwise, groupby


def has_intersecting_segments(segments):
    s = sorted(segments)
    for i in range(1, len(segments)):
        if s[i][0] <= s[i - 1][1]:
            return True
    return False


def min_difference_pairs(nums):
    s = sorted(nums)
    dif = min(b - a for a, b in pairwise(s))
    return [i for i in pairwise(s) if i[1] - i[0] == dif]


def bound_sort(nums, k):
    m = max(nums[i] for i in range(k + 1))
    for i in range(k + 1, len(nums)):
        if nums[i] <= max(nums[i - 1], m):
            return False
    return True


def count_beautiful_pairs(nums):
    s = set(nums)
    return len(s) * (len(s) - 1) // 2


def min_steps_to_make_equal(nums):
    target = sorted(nums)[len(nums) // 2]
    return sum(abs(i - target) for i in nums)


def find_num(nums: list[int]):
    nums.sort()
    nums.remove(nums[0] * nums[1])
    return nums[-1] // nums[2]


def year_with_max_living_people(years_of_life):
    years = {}
    for i in years_of_life:
        years[i[0]] = years.get(i[0], 0) + 1
        years[i[1] + 1] = years.get(i[1] + 1, 0) - 1
    population = max_population = 0
    max_year = float('-inf')
    for year, delta in sorted(years.items()):
        population += delta
        if population > max_population:
            max_population = population
            max_year = year
    return max_year


def common_free_time(plan):
    hours = [0] * 24
    for employee in plan:
        for interval in employee:
            hours[interval[0]:interval[1]] = [1] * (interval[1] - interval[0])
    start = 0
    work = False
    result = []
    for i, v in enumerate(hours):
        if v == 1 and not work:
            work = True
            if start < i:
                result.append((start, i))
        if v == 0 and work:
            start = i
            work = False
    if start < 23:
        result.append((start, 23))
    return result
