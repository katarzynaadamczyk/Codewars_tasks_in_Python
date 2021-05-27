def int32_to_ip(int32):
    data = bin(int32)[2:].zfill(32)
    out = list()
    while len(data) > 0:
        out.insert(0, str(int(data[-8:], 2)))
        data = data[:-8]
    return '.'.join(out)

def main():
    print(int32_to_ip(2154959208))
    print(int32_to_ip(0))
    print(int32_to_ip(2149583361))


if __name__ == '__main__':
    main()