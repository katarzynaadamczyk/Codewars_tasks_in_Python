def run_length_encoding(s):
    ret = []
    if len(s):
        last_letter = s[0]
        letter_count = 1
        
        for i in range(1, len(s)):
            if s[i] == last_letter:
                letter_count += 1
            else:
                ret.append([letter_count, last_letter])
                last_letter = s[i]
                letter_count = 1
        ret.append([letter_count, last_letter])
    
    return ret

    


def main():
    print(f'Solution for "" is {run_length_encoding("")}')
    print(f'Solution for "abc" is {run_length_encoding("abc")}')
    print(f'Solution for "aab" is {run_length_encoding("aab")}')
    print(f'Solution for "hello world!" is {run_length_encoding("hello world!")}')
    print(f'Solution for "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb" is {run_length_encoding("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbb")}')
    print(f'''Solution for "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW" 
            is {run_length_encoding("WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW")}''')


if __name__ == '__main__':
    main()