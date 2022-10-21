''' exercise VLQ '''

from multiprocessing.sharedctypes import Value


def encode(numbers):
    ret_table = []
    numbers = [x[2:] for x in list(map(bin, numbers))]
    for number in numbers:
        number = number.zfill((len(number) // 7 + 1 if len(number) % 7 else len(number) // 7) * 7)
        number_list = [number[i:i+7] for i in range(0, len(number), 7)]
        number_list = ['1' + number_list[i] for i in range(len(number_list) - 1)] + [number_list[-1].zfill(8)]
        ret_table += number_list
    return [int(x, 2) for x in ret_table]


def decode(bytes_):
    ret_table, act_number = [], ''
    bytes_ = [x[2:].zfill(8) for x in list(map(bin, bytes_))]
    if bytes_[-1].startswith('1'):
        raise ValueError("incomplete sequence")
    print(bytes_)
    for byte_ in bytes_:
        act_number += byte_[1:]
        if byte_.startswith('0'):
            if len(act_number) > 28 and '1' in act_number[0:-28]:
                act_number = 32 * '1'
            ret_table.append(act_number)
            act_number = ''
    return [int(x, 2) for x in ret_table]


def main():
    print(encode([106903]))
    print(decode(encode([106903, 21])))
    print(decode([0x8F, 0xFF, 0xFF, 0xFF, 0x7F]))
    
if __name__ == '__main__':
    main()
    