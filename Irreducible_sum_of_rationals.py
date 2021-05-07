import math

def sum_fracts(lst):
    if len(lst):
        result = lst[0]
        for i in range(1, len(lst)):
            # add two rationals
            com_div = math.gcd(result[1], lst[i][1])
            result[0] = result[0] * lst[i][1] // com_div + lst[i][0] * result[1] // com_div
            result[1] = result[1] * lst[i][1] // com_div
        com_div = math.gcd(result[0], result[1])
        result[0] //= com_div
        if result[1] == com_div:
            result = result[0]
        else:
            result[1] //= com_div
        return result
    return None
  

  
def main():
    print(f'Result for sum_fracts([[1, 2], [1, 3], [1, 4]]) equals {sum_fracts([[1, 2], [1, 3], [1, 4]])} while it should equal [13, 12]')
    print(f'Result for sum_fracts([[1, 3], [5, 3]]) equals {sum_fracts([[1, 3], [5, 3]])} while it should equal 2')




if __name__ == '__main__':
    main()