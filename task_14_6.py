def hamming_weight(num):
    return bin(num).count('1')


def hex_color_code(r, g, b):
    return f'#{r:02X}{g:02X}{b:02X}'


def max_binary_gap(num):
    b_str = f'{num:b}'
    max_gap = 0
    gap=0
    for i in b_str:
        if i =='0':
            gap+=1
        else:
            max_gap = max(max_gap, gap)
            gap =0
    return max_gap

def bit_reverse(num):
    return int("".join(reversed(f'{num:b}')), 2)