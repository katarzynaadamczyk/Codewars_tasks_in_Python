''' rail fence cipher '''

from turtle import position


def get_rails_indexes(rails, lenght):
    r, up = 0, True
    for i in range(lenght):
        yield (r, i)
        r = r + 1 if up else r - 1
        if r == 0:
            up = True
        elif r == rails - 1:
            up = False


def encode(message, rails):
    message_dict = {position: letter for position, letter in zip(get_rails_indexes(rails, len(message)), message)}
    return ''.join([message_dict[position] for position in sorted(list(message_dict.keys()), key=lambda x: (x[0], x[1]))])


def decode(encoded_message, rails):
    zig_zag = sorted(list(get_rails_indexes(rails, len(encoded_message))), key=lambda x: (x[0], x[1]))
    message_dict = {position: letter for position, letter in zip(zig_zag, encoded_message)}
    return ''.join([message_dict[position] for position in sorted(zig_zag, key=lambda x: x[1])])


def main():
    lst = [x for x in get_rails_indexes(3, 10)]
    print(lst)
    print(encode("WEAREDISCOVEREDFLEEATONCE", 3), 'should equal WECRLTEERDSOEEFEAOCAIVDEN')
    print(decode('WECRLTEERDSOEEFEAOCAIVDEN', 3), 'should equal WEAREDISCOVEREDFLEEATONCE')


if __name__ == '__main__':
    main()