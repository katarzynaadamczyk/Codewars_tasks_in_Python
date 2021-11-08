class RomanNumerals:
    
    def to_roman(val):
        return ''

    def from_roman(roman_num):
        return 0
                

def main():
    print('TESTS FROM ROMAN')
    print(f'XXI should == 21 and it == f{RomanNumerals.from_roman("XXI")}')
    print(f'I should == 1 and it == f{RomanNumerals.from_roman("I")}')
    print(f'IV should == 4 and it == f{RomanNumerals.from_roman("IV")}')
    print(f'MMVIII should == 2008 and it == f{RomanNumerals.from_roman("MMVIII")}')
    print(f'MDCLXVI should == 1666 should == 2008 and it == f{RomanNumerals.from_roman("MDCLXVI")}')
    print('TESTS TO ROMAN')
    print(f'1000 should == "M" and it == f{RomanNumerals.to_roman(1000)}')
    print(f'4 should == "IV" and it == f{RomanNumerals.to_roman(4)}')
    print(f'1 should == "I" and it == f{RomanNumerals.to_roman(1)}')
    print(f'1990 should == "MCMXC" and it == f{RomanNumerals.to_roman(1990)}')
    print(f'2008 should == "MMVIII" and it == f{RomanNumerals.to_roman(2008)}')
    

if __name__ == '__main__':
    main()