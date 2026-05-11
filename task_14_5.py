def bin_to_oct(binary_str):
    triplets = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
    n = len(binary_str)
    first = [binary_str[0: n % 3].zfill(3)] if n % 3 else []
    split = first + [binary_str[i:i + 3] for i in range(n % 3, n, 3)]
    return ''.join([triplets[t] for t in split])


def hex_to_bin(hex_str):
    hex2bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    return ''.join([hex2bin[h] for h in hex_str]).lstrip('0') or '0'


def oct_to_hex(oct_str):
    oct2bin = {
        '0': '000', '1': '001', '2': '010', '3': '011',
        '4': '100', '5': '101', '6': '110', '7': '111'}

    bin2hex = {'0000': '0', '0001': '1', '0010': '2', '0011': '3',
               '0100': '4', '0101': '5', '0110': '6', '0111': '7',
               '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
               '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}

    binary_str = ''.join([oct2bin[d] for d in oct_str]).lstrip('0') or '0'
    n = len(binary_str)
    first = [binary_str[0: n % 4].zfill(4)] if n % 4 else []
    split = first + [binary_str[i:i + 4] for i in range(n % 4, n, 4)]
    return ''.join([bin2hex[t] for t in split])

def hex_to_oct(hex_str):
    return bin_to_oct(hex_to_bin(hex_str))