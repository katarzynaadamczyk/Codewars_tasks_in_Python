''' my solution to KATA: https://www.codewars.com/kata/54b72c16cd7f5154e9000457/'''

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
    if one == step:
        return '.'
    elif one == 3 * step:
        return '-'

def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    ones_len, zeros_len = [len(x) for x in re.findall(r'[1]{1,}', bits)], [len(x) for x in re.findall(r'[0]{1,}', bits)]
    if sum(ones_len + zeros_len) != len(bits):
        raise ValueError('got not only ones and zeros')
    step = min(ones_len + zeros_len)
    result = ''
    for one, zero in zip(ones_len, zeros_len):
        result += get_one(one, step)
        if zero == 3 * step:
            result += ' '
        elif zero == 7 * step:
            result += '   '
    result += get_one(ones_len[-1], step)
    return result

def decode_morse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    words, result = morseCode.split('   '), []
    for word in words:
        result.append(''.join([MORSE_CODE[char] for char in word.split()]))
    return ' '.join(result)

def main():
    print(decode_morse(decode_bits('1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011')))
    print('should equal: ', 'HEY JUDE')
    
if __name__ == '__main__':
    main()
