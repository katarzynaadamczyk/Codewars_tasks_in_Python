''' exercise VLQ '''

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
    ret_value = []
    bytes_ = [x[2:].zfill(8) for x in list(map(bin, bytes_))]
    print(bytes_)
    for byte_ in bytes_:
        pass
    return 0 # int(ret_value, 2)


def main():
    print(encode([106903]))
    print(decode(encode([106903, 21])))
    print(decode([0x8F, 0xFF, 0xFF, 0xFF, 0x7F]))
    
if __name__ == '__main__':
    main()
    