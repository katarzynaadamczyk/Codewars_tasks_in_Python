def breakPalindrome(palindrome: str) -> str:
        if len(palindrome) < 2:
            return ''
        position = -1
        for i in range(len(palindrome)):
            if palindrome[i] != 'a' and i != len(palindrome) // 2:
                position = i
                break
        if position < 0:
            return palindrome[0:len(palindrome)-1] + 'b'
        return palindrome[0:position] + 'a' + palindrome[position+1::]


def main():
    print(f'Solution for "anna" is {breakPalindrome("anna")}')
    print(f'Solution for "a" is {breakPalindrome("a")}')
    print(f'Solution for "bejbi" is {breakPalindrome("bejbi")}')
    print(f'Solution for "aaaaa" is {breakPalindrome("aaaaa")}')
    print(f'Solution for "aba" is {breakPalindrome("aba")}')


if __name__ == '__main__':
    main()