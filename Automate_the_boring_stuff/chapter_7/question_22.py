'''
pytanie 21 / 211
wyrazenie regularne dopasowujace imie i nazwisko
'''

from tokenize import String
import re

def if_sentence(str: String) -> bool:
    sentenceRegex = re.compile(r'(Alicja|Bob|Karol)\s(je|głaszcze|rzuca)\s(jabłka|kota|piłkę)\.', re.IGNORECASE)
    return True if sentenceRegex.match(str) else False


if __name__ == '__main__':
    assert if_sentence('Alicja je jabłka.') == True
    assert if_sentence('RoboCop je jabłka.') == False
    assert if_sentence('Bob GŁASZCZE kota.') == True
