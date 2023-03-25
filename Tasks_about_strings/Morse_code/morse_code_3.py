''' '''

import re

MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', 
              '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', 
              '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', 
              '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', 
              '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': 
              '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', 
              '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", 
              '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', 
              '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', 
              '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}

def get_one(one, step):
    if one < step:
        return '.'
    else:
        return '-'

def decodeBitsAdvanced(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    ones_len, zeros_len = [len(x) for x in re.findall(r'[1]{1,}', bits)], [len(x) for x in re.findall(r'[0]{1,}', bits)]
    if sum(ones_len + zeros_len) != len(bits):
        raise ValueError('got not only ones and zeros')
    step = 5
    result = ''
    for one, zero in zip(ones_len, zeros_len):
        result += get_one(one, step)
        if 5 <= zero <= 10:
            result += ' '
        elif zero > 10:
            result += '   '
    result += get_one(ones_len[-1], step)
    return result

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    words, result = morseCode.split('   '), []
    for word in words:
        result.append(''.join([MORSE_CODE[char] for char in word.split()]))
    return ' '.join(result)

def main():
    print(decodeMorse(decodeBitsAdvanced('0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000')))
    print('should equal: ', 'HEY JUDE')
    
if __name__ == '__main__':
    main()
    