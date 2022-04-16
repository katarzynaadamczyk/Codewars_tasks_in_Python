'''
projekt ze strony 212
Oparta na wyrażeniu regularnym wersja metody strip()
'''

import re
from tokenize import String

def newStrip(text: String, signs: String = '') -> String:
    if signs == '':
        myRegexStart = re.compile(r'^\s*')
        myRegexStop = re.compile(r'\s*$')
    else:
        myRegexStart = re.compile(rf'^[{signs}]+')
        myRegexStop = re.compile(rf'[{signs}]+$')
    text = myRegexStart.sub('', text)
    text = myRegexStop.sub('', text)
    return text
    

if __name__ == '__main__':
    print(newStrip('   popso   '))
    print(newStrip('babmixb', 'ba'))
    print(newStrip('****ania**-', '*-=+'))
    