'''
pytanie 21 / 211
wyrazenie regularne dopasowujace imie i nazwisko
'''

from tokenize import String
import re

def if_name(str: String) -> bool:
    return True if re.match(r'[A-Z]\w+\sNakamoto', str) else False


if __name__ == '__main__':
    assert if_name('Satoshi Nakamoto') == True
    assert if_name('Alicja Nakamoto') == True
    assert if_name('RoboCop Nakamoto') == True
    assert if_name('satoshi Nakamoto') == False
    assert if_name('Mr. Nakamoto') == False
    assert if_name('Nakamoto') == False
    assert if_name('Satoshi nakamoto') == False
