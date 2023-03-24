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

def decodeBitsAdvanced(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    ones_len, zeros_len = [len(x) for x in re.findall(r'[1]{1,}', bits)], [len(x) for x in re.findall(r'[0]{1,}', bits)]
    print(ones_len)
    print(zeros_len)
    return bits.replace('111', '-').replace('000', ' ').replace('1', '.').replace('0', '')

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return morseCode.replace('.', 'E').replace('-', 'T').replace(' ', '')

def main():
    print(decodeMorse(decodeBitsAdvanced('0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000')))
    print('should equal: ', 'HEY JUDE')
    
if __name__ == '__main__':
    main()
    