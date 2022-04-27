''' exercise acronym '''

import re

def abbreviate(words):
    ret = ''
    word_regex = re.compile(r'\W*\w+(\'s)?\W*')
    for word in words.split():
        print(re.match(r'^\W*\w+(\'s)?\W*$', word))
        if re.match(r'^\W*\w+(\'s)?\W*$', word):
            index = 0
            while not word[index].isalpha():
                index += 1
            ret += word[index].upper()
    return ret

if __name__ == '__main__':
    try:
        assert abbreviate("Portable Network Graphics") == "PNG"
        assert abbreviate("Ruby on Rails") == "ROR"
        assert abbreviate("First In, First Out") == 'FIFO'
        assert abbreviate("GNU Image Manipulation Program") == "GIMP"
        assert abbreviate("Something - I made up from thin air") == "SIMUFTA"
        assert abbreviate("Halley's Comet") == "HC"
        assert abbreviate("The Road _Not_ Taken") == "TRNT"
        assert abbreviate("Complementary metal-oxide semiconductor") == "CMOS"
    except AssertionError as e:
        print(e, e.args)