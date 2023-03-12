'''
my solution to task:
https://www.codewars.com/kata/5968bb83c307f0bb86000015

'''

def nico(key, message):
    # prepare key and message to appriopriate length
    chunk_len = len(key)
    if len(message) % chunk_len != 0:
        message = message + (chunk_len - len(message) % chunk_len) * ' '
    sorted_key, numeric_key = sorted(key), [0 for _ in range(chunk_len)]
    for index, char in enumerate(sorted_key):
        numeric_key[index] = key.find(char)
        
    # get result
    chunks, result = [message[chunk_len * i: chunk_len * (i + 1)] for i in range(len(message) // chunk_len)], ''
    for chunk in chunks:
        new_chunk = ''
        for index in numeric_key:
            new_chunk += chunk[index]
        result += new_chunk
    return result

def main():
    print(nico('crazy', 'secretinformation'))
    
if __name__ == '__main__':
    main()
    
    