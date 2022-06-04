''' exercise pig latin '''

import re

def get_beginning(word):
    consonants = ''
    for char in word:
        if char in 'qwrtpsdfghjklzxcvbnm' or char == 'y' == word[0]:
            consonants += char
        else:
            return consonants, char
    
def translate(text):
    words = re.findall(r'[a-z]+', text.lower())
    result = []
    for word in words:
        if re.match(r'^(a|e|u|i|o|yt|xr).*$', word):
            result.append(word + 'ay')
        else:
            consonants, vowel = get_beginning(word)
            if vowel == 'u' and consonants[-1] == 'q':
                result.append(word[len(consonants + vowel):] + consonants + vowel + 'ay')
            else:
                result.append(word[len(consonants):] + consonants + 'ay')
        pass
    return ' '.join(result)

if __name__ == '__main__':
    print(translate('quIck fast run xray'))
