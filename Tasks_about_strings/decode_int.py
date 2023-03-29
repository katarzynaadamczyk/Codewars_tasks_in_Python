''' my solution to kata https://www.codewars.com/kata/566859a83557837d9700001a '''

def get_count(n):
    result, n_str = 0, str(n)
    for act_len in range(1, len(n_str)):
        for i in range(len(n_str) - act_len + 1):
            act_num = int(n_str[i:i+act_len])
            if act_num != 0 and n % act_num == 0:
                result += 1
    return result
        
def main():
    print(get_count(11))
    print(get_count(877692))
    print(get_count(877692877692))
    print(get_count(877692877692877692))
    
if __name__ == '__main__':
    main()
    