from string import ascii_lowercase

# 1
def find_first_unique_letter(s):
    letters = set()
    for i in range(len(s)):
        if s[i].lower() in letters:
            continue
        if s[i].lower() in ascii_lowercase:
            letters.add(s[i].lower())
            if s[i].lower() not in s[i+1:].lower():
                return(s[i])

    return None

# 2
def find_first_unique_letter_2(s):
    letters = dict()
    for char in s.lower():
        if char in ascii_lowercase:
            letters.setdefault(char, 0)
            letters[char] += 1
    for char in s:
        if char.lower() in letters.keys() and letters[char.lower()] == 1:
            return char

    return None

# 3
def find_first_unique_letter_3(s):
    letters = dict()
    for i in range(len(s)):
        if s[i].lower() in ascii_lowercase:
            letters.setdefault(s[i].lower(), [0, i])
            letters[s[i].lower()][0] += 1
    
    for key in letters.keys():
        if letters[key][0] == 1:
            return s[letters[key][1]]

    return None


def main():
    print('First:')
    print(find_first_unique_letter('Kasia'))
    print(find_first_unique_letter('Przemek'))
    print(find_first_unique_letter('ala ma kota Leona'))
    print(find_first_unique_letter('bardzo KOCHA tego swojego Baczka'))
    print('Second:')
    print(find_first_unique_letter_2('Kasia'))
    print(find_first_unique_letter_2('Przemek'))
    print(find_first_unique_letter_2('ala ma kota Leona'))
    print(find_first_unique_letter_2('bardzo KOCHA tego swojego Baczka'))
    print('Third:')
    print(find_first_unique_letter_3('Kasia'))
    print(find_first_unique_letter_3('Przemek'))
    print(find_first_unique_letter_3('ala ma kota Leona'))
    print(find_first_unique_letter_3('bardzo KOCHA tego swojego Baczka'))
    

if __name__ == '__main__':
    main()