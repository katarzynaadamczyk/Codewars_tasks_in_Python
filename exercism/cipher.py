''' exercise cipher '''

from secrets import randbelow

class Cipher:
    def __init__(self, key=None):
        if key is None:
            self.key = ''.join([chr(ord('a') + randbelow(26)) for _ in range(100)])
        else:
            self.key = key

    def enlarge_key(self, text):
        while len(self.key) < len(text):
            self.key += self.key
    
    def encode(self, text):
        self.enlarge_key(text)
        index, result = 0, ''
        for char in text:
            if char.isalpha():
                result += chr(ord('a') + (ord(self.key[index]) + ord(char.lower()) - 2 * ord('a')) % 26)
                index += 1
            else:
                result += char
        return result

    def decode(self, text):
        self.enlarge_key(text)
        index, result = 0, ''
        for char in text:
            if char.isalpha():
                result += chr(ord('a') + (ord(char.lower()) - ord(self.key[index])) % 26)
                index += 1
            else:
                result += char
        return result


if __name__ == '__main__':
    new_cipher = Cipher('abc')
    result = new_cipher.encode('any free text')
    print(result)
    new_result = new_cipher.decode(result)
    print(new_result)
    