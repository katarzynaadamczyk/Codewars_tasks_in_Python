import re

def parse_number(s):
    return True if re.match(r"^-?\d\d*\.?\d*e?\d*$", s) else False
   

def main():
    print(f'Result for "12.3" equals {parse_number("12.3")} when it should equal True"')
    print(f'Result for "12.a" equals {parse_number("12a")} when it should equal False"')
    print(f'Result for "123" equals {parse_number("123")} when it should equal True"')
    print(f'Result for "-123" equals {parse_number("-123")} when it should equal True"')
    print(f'Result for "-0.3" equals {parse_number("-0.3")} when it should equal True"')
    print(f'Result for "1.5e5" equals {parse_number("1.5e5")} when it should equal True"')
    print(f'Result for "-.3" equals {parse_number("-.3")} when it should equal False"')
    print(f'Result for "1 2" equals {parse_number("1 2")} when it should equal False"')
    print(f'Result for "1e1.2" equals {parse_number("1e1.2")} when it should equal False"')


if __name__ == '__main__':
    main()