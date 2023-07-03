'''
wyszukuje adresy email i amerykanskie numery telefonów ze schowka
'''

import pyperclip, re

phoneRegex = re.compile(r'''(
                            (\d{3}|\(\d{3}\))?                  # numer kierunkowy
                            (\s|-|\.)?                          # przerwa
                            (\d{3})                             # pierwsze 3 cyfry
                            (\s|-|\.)?                          # przerwa
                            (\d{4})                             # 4 cyfry
                            (\s*(ext|ext\.|x)\s*(\d{2,5}))?     # numer wewnetrzny
                            )''', re.VERBOSE)

emailRegex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+                       # nazwa użytkownika
                        @                                       # małpka
                        [a-zA-Z0-9.-]+                          # nazwa domeny
                        (\.[a-zA-Z]{2,4})                       # kropka i cokolwiek
                        )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[x] for x in range(1, 6, 2)])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    print(groups)
    matches.append(groups[0])
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Skopiowano do schowka: ')
    print('\n'.join(matches))
else:
    print('Nie znaleziono numeru telefonu lub adresu email.')
