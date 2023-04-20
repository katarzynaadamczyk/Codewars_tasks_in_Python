''' my solution to kata https://www.codewars.com/kata/55ee3ebff71e82a30000006a'''

def title_to_number(title):
    return sum([26 ** index * (ord(char) - ord('A') + 1) for index, char in enumerate(title[::-1])])

def main():
    print(title_to_number('A'))
    print(title_to_number('ABC'))
    print(title_to_number('CA'))
    print(title_to_number('DAFAQWDRFASFVG'))
    
if __name__ == '__main__':
    main()
    