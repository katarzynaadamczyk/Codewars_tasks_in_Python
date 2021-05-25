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


def main():
    print(find_first_unique_letter('Kasia'))
    print(find_first_unique_letter('Przemek'))
    print(find_first_unique_letter('ala ma kota Leona'))
    print(find_first_unique_letter('bardzo KOCHA tego swojego Baczka'))
    

if __name__ == '__main__':
    main()