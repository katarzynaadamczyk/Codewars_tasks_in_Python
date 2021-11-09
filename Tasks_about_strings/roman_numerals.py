class RomanNumerals:
    
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    rroman_dict = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    
    def to_roman(val):
        ret = ''
        for key in RomanNumerals.rroman_dict.keys():
            ret += val // key * RomanNumerals.rroman_dict[key]
            val = val % key
            
        return ret

    def from_roman(roman_num):
        if len(roman_num):
            num = RomanNumerals.roman_dict[roman_num[-1]]
            for i in range(0, len(roman_num) - 1):
                if RomanNumerals.roman_dict[roman_num[i + 1]] > RomanNumerals.roman_dict[roman_num[i]]:
                    num -= RomanNumerals.roman_dict[roman_num[i]]
                else:
                    num += RomanNumerals.roman_dict[roman_num[i]]
            return num
        return 0
                

def main():
    print('TESTS FROM ROMAN')
    print(f'XXI should == 21 and it == {RomanNumerals.from_roman("XXI")}')
    print(f'I should == 1 and it == {RomanNumerals.from_roman("I")}')
    print(f'IV should == 4 and it == {RomanNumerals.from_roman("IV")}')
    print(f'MMVIII should == 2008 and it == {RomanNumerals.from_roman("MMVIII")}')
    print(f'MDCLXVI should == 1666 and it == {RomanNumerals.from_roman("MDCLXVI")}')
    print('TESTS TO ROMAN')
    print(f'1000 should == "M" and it == {RomanNumerals.to_roman(1000)}')
    print(f'4 should == "IV" and it == {RomanNumerals.to_roman(4)}')
    print(f'1 should == "I" and it == {RomanNumerals.to_roman(1)}')
    print(f'1990 should == "MCMXC" and it == {RomanNumerals.to_roman(1990)}')
    print(f'2008 should == "MMVIII" and it == {RomanNumerals.to_roman(2008)}')
    

if __name__ == '__main__':
    main()