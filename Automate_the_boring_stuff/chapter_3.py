def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    print(number * 3 + 1)
    return number * 3 + 1


def main():
    while True:
        try:
            number = int(input('Please put in a natural number > 0: \n'))
            if number > 0:
                break
            print('You did not put in number > 0')
        except ValueError:
            print('Make sure you put in a natural number')
    while number != 1:
        number = collatz(number)
    

if __name__ == '__main__':
    main()