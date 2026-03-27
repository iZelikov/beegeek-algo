def binary_search(data, target):
    left = 0
    right = len(data) - 1
    desc = data[-1] < data[0]
    while left < right:
        middle = left + (right - left) // 2
        if data[middle] < target:
            if desc:
                right = middle - 1
            else:
                left = middle + 1
        elif data[middle] > target:
            if desc:
                left = middle + 1
            else:
                right = middle - 1
        else:
            return middle
    return (-1, left)[data[left] == target]


def bounded_binary_search(data, target, left=None, right=None):
    left = (left, 0)[left is None]
    right = (right, len(data) - 1)[right is None]
    while left < right:
        middle = left + (right - left) // 2
        if data[middle] < target:
            left = middle + 1
        elif data[middle] > target:
            right = middle - 1
        else:
            return middle
    return (-1, left)[data[left] == target]


def guess(num):
    g = 11111111
    if g < num:
        return "Меньше"
    elif g > num:
        return 'Больше'
    elif g == num:
        return 'Отгадал!'


def get_number(limit):
    left = 1
    right = limit
    while left <= right:
        mid = left + (right - left) // 2
        result = guess(mid)
        if result == 'Меньше':
            right = mid - 1
        elif result == 'Больше':
            left = mid + 1
        else:
            print(mid)
            break

get_number(10 ** 11)