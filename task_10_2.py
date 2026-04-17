from collections import defaultdict, Counter
from itertools import product


def happy_tickets_2(n):
    count = 0
    counts = defaultdict(int)
    for a in range(min(n + 1, 10)):
        for b in range(min(n + 1 - a, 10)):
            counts[a + b] += 1

    for k, v in counts.items():
        count += counts.get(n - k, 0) * v

    return count ** 2


def count_pythagorean_triplets(nums1, nums2, nums3):
    count = 0
    c_s = {}
    for i in nums3:
        c_s[i ** 2] = c_s.get(i ** 2, 0) + 1
    for a in nums1:
        for b in nums2:
            count += c_s.get(a ** 2 + b ** 2, 0)
    return count


def pair_with_sum(nums, k):
    pairs = set()
    for n in nums:
        if k - n in pairs:
            return tuple(sorted([n, k - n]))
        else:
            pairs.add(n)


def count_triplets_with_sum(nums1, nums2, nums3, k):
    triplets_count = 0
    n1 = Counter(nums1)
    n2 = Counter(nums2)
    n3 = Counter(nums3)
    for a, a_count in n1.items():
        for b, b_count in n2.items():
            triplets_count += n3[k - a - b] * a_count * b_count
    return triplets_count


def radix_sum(n):
    sums_3 = Counter(sum(i) for i in product(range(10), repeat=3))
    sums_6_half = {i: sum(sums_3[x] * sums_3[i - x] for x in range(i + 1)) for i in range(len(sums_3))}
    n = min(n, 108 - n)
    return sum(sums_6_half[min(x, 54 - x)] * sums_6_half[min(n - x, 54 - (n - x))] for x in range(n + 1))


def count_valid_quadruplets(nums1, nums2, nums3, nums4):
    a_b = Counter(sum(i) for i in product(nums1, nums2))
    c_d = Counter(i[1] - i[0] for i in product(nums3, nums4))
    c_3d = Counter(3 * i[1] - i[0] for i in product(nums3, nums4) if i[1])
    return sum(count * (c_d[s] + c_3d[s]) for s, count in a_b.items())

