def guess(n):
    x = 16
    if n > x:
        return "Меньше"
    elif n < x:
        return "Больше"
    else:
        return "Отгадал!"


def guess_number():
    right = 1
    while guess(right) != "Меньше":
        right *= 2

    left = right // 2
    while left <= right:
        mid = left + (right - left) // 2
        if guess(mid) == "Отгадал!":
            return mid
        elif guess(mid) == "Больше":
            left = mid + 1
        else:
            right = mid - 1
    return left


def find_index(nums, target):
    right = 1
    while nums[right] < target:
        right *= 2

    left = right // 2
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def is_value(values, target):
    right = 1
    while values[right] > target:
        right *= 2

    left = right // 2
    while left <= right:
        mid = left + (right - left) // 2
        if values[mid] == target:
            return True
        elif values[mid] > target:
            left = mid + 1
        else:
            right = mid - 1
    return False


def min_positive(func):
    right = 1
    while func(right) <= 0:
        right *= 2

    left = right // 2
    while left <= right:
        mid = left + (right - left) // 2
        m = func(mid)
        l = func(left)
        if l > 0:
            return l
        elif m <= 0:
            left = mid + 1
        else:
            right = mid
    return func(left)


def get_argument(func, value):
    f = func(0)
    if f < value:
        right = 1
        while func(right) < value:
            right *= 2
        left = right // 2
    elif f > value:
        left = -1
        while func(left) > value:
            left *= 2
        right = left // 2
    else:
        return 0

    while left <= right:
        mid = left + (right - left) // 2
        m = func(mid)
        if m == value:
            return mid
        elif m < value:
            left = mid + 1
        else:
            right = mid - 1
    return None


def count_victories(power):
    enemies = lambda i: i * (i + 1) * (2 * i + 1) // 6
    right = 1
    while enemies(right) < power:
        right *= 2

    left = right // 2
    while left < right:
        mid = left + (right - left) // 2
        m = enemies(mid)
        r = enemies(right)
        if r <= power:
            return right
        elif m > power:
            right = mid - 1
        else:
            left = mid
            right -= 1
    return right
