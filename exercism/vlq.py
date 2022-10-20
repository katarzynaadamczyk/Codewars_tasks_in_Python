''' exercise VLQ '''

def encode(numbers):
    ret_table = []
    numbers = [x[2:] for x in list(map(bin, numbers))]
    print(numbers)
    for number in numbers:
        number_list = [number[i:i+7] for i in range(0, len(number), 7)]
        print(number_list)
        pass
    print(numbers)
    return ret_table


def decode(bytes_):
    pass


def main():
    print(encode([0x0, 0x40, 0x2000]))
    
if __name__ == '__main__':
    main()
    