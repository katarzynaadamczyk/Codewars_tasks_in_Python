''' exercise acronym '''

import re

def abbreviate(words):
    ret = ''
    word_regex = re.compile(r"[^a-zA-Z0-9]*\w+'?s?")
    for word in words.split():
        for match in word_regex.findall(word):
            index = 0
            while not match[index].isalpha():
                index += 1
            ret += match[index].upper()
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
        print('All well done')
    except AssertionError as e:
        print('Assertion Error')