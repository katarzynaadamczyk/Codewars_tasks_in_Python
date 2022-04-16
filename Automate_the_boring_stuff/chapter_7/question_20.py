'''
pytanie 20 / 210
wyrazenie regularne dopasowujace liczbe z przecinkami po kazdych trzech cyfrach
'''

from tokenize import String
import re

def if_number(str: String) -> bool:
    return True if re.match(r'^\d{1,3}(,\d{3})*$', str) else False


if __name__ == '__main__':
    assert if_number('42') == True
    assert if_number('1,234') == True
    assert if_number('6,368,745') == True
    assert if_number('12,34,567') == False
    assert if_number('1234') == False
