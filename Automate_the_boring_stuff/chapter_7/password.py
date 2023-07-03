'''
wykryj silne hasło zawierające co najmniej jedna dużą, jedną małą literę i jedną cyfrę
hasło musi mieć co najmniej 8 znaków
'''

import re
from tabnanny import check


def checkPassword(password):
    passwordRegex = re.compile(r'^[A-Za-z0-9]{8,}$')
    bigLettersRegex = re.compile(r'[A-Z]')
    smallLettersRegex = re.compile(r'[a-z]')
    numbersRegex = re.compile(r'[0-9]')
    if passwordRegex.findall(password):
        print(passwordRegex.findall(password))
        if bigLettersRegex.findall(password) and smallLettersRegex.findall(password) \
            and numbersRegex.findall(password):
            return True
    return False

if __name__ == '__main__':
    assert checkPassword('AbacCd9876') == True
    assert checkPassword('sas') == False
    assert checkPassword('AAAAAAAA') == False