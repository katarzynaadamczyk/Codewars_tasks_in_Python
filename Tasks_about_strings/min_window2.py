'''
leetcode
task: 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/
fast solution with a sliding window
'''

from collections import Counter

class Solution:
    # function to find first and last index where to look for the shortest substr
    def findMinMaxIndex(self, s: str, tCounter: Counter) -> tuple[int, int]:
        minIndex, maxIndex = len(s) - 1, 0
        for char in tCounter.keys():
            minIndex = min(s.index(char), minIndex)
            maxIndex = max(s.rindex(char), maxIndex)
        return (minIndex, maxIndex)

    # validate if tCounter is included in sCounter,if so True, else False
    def checkCounters(self, sCounter: Counter, tCounter: Counter) -> bool:
        for char, value in tCounter.items():
            if sCounter[char] < value:
                return False
        return True

    # solution function
    def minWindow(self, s: str, t: str) -> str:
        # create and keep counter of chars in t
        tCounter = Counter(t) 
        # no solution if s is empty or s does not contain all characters from t
        if s == '' or not self.checkCounters(Counter(s), tCounter):
            return ''
        minIndex, maxIndex = self.findMinMaxIndex(s, tCounter)
        tLength = len(t)
        minWord = (minIndex, maxIndex)
        iMin, iMax = minIndex, minIndex + tLength - 1
        sCounter = Counter(s[iMin:iMax + 1])
        while iMin < maxIndex - tLength + 1 and iMax < maxIndex:
            print(iMin, iMax)
            while iMax < maxIndex and not self.checkCounters(sCounter, tCounter):
                iMax += 1
                sCounter[s[iMax]] += 1
            if self.checkCounters(sCounter, tCounter) and iMax - iMin < minWord[1] - minWord[0]:
                minWord = (iMin, iMax)
            while iMin < maxIndex - tLength and self.checkCounters(sCounter, tCounter):
                sCounter[s[iMin]] -= 1
                iMin += 1
         #   sCounter[iMin - 1] += 1
            if self.checkCounters(sCounter, tCounter) and iMax - iMin < minWord[1] - minWord[0]:
                minWord = (iMin, iMax)
            sCounter[iMin - 1] -= 1

            
        return s[minWord[0]:minWord[1]+1]

def main():
    sol = Solution()
    # test 1
    s = "ADOBECODEBANC"
    t = "ABC"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'BANC\'')
    # test 2
    s = "a"
    t = "a"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'a\'')
    # test 3
    s = ""
    t = "a"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'\'')
    # test 4
    s = "qdsvbyuipqxnhkbgqdgozelvapgcainsofnrfjzvawihgmpwpwnqcylcnufqcsiqzwhhhjchfmqmagkrexigytklnrdslmkniuurdwzikrwlxhcbgkjegwsvnvpzhamrwgjzekjobizbreexqqewmwubtjadlowhwhiarurvcsyvwcunsylgwhisrivezrmvzwwsqppuhnreqmtkkgrjozbhjwlkpzgqwejotylamcgeqzobihmwinduloecqmtoqcejcpmqusukulncsbabodxbtbeloxzgbesdveupyocuzryutyxjdulzvpklokspqkslqodqfhlgajatkxfntqorhzcxlwmdigoyxtrcccidnlyxidnevdveczbpwpugyjhveyxhcfkpqipboehjhcombrdzhyghjncnnzwpggezrvcfzjqjngvoyyqhwwohlsvarrpzavatrcasnqbazyrzxhivfydsqasjtjiteloxposdhtfgswhrfpomnteftyonjyiojxnznfeubjctijmnyaanwgsphieqhpgsoutbbxycjaxrklekogakpsbwdimkxvelpyosvmxgnuxzgejwmjgbehxhpmtohzbyxqsvepbrmzsufcqrnwttfscxgxlpxnpufirjxtdjuvfzzvqprlizelwmkjchwtcdbvpbosminsjpncehnmgtzegknkrmdvrhrgihywsoobdedhltvtmxzuhmeaakysrpybyzxqnouqszzfswahtzbanidoubilsgoqfnjubdmvclaxkaedbfeppj"
    t = "fjknwevk"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'\'')
    # test 5
    s = "xeaifhaqslynbcwxncwgeezbrjorzyuwevejcecuscjvgfutkrcqxbromihlgcjnzpybwcxqeglknhgzyiqxljnyrvlazvnyklbgoywugjftrltrvlrgueeobsoandazqbigbgbhqgdjtycojtwfydtbvjekmejdirjlymvquybnyddjxaoxfkyatckijvlrnwcnjxfdxgtvjweiyvfdhefaipkrnviaunpfmukkcdhlcmwcjbgqhnsqfdhsasuwhjbtfmdhrluvzqykugcbtutyzdqcxkyevaxcodjhogdpwbzsjducxpdzsvbpizvfbtirwtzmzebyhcqqfmueczdwveofgjkhesbamaolgrlpvcfcqbhubmtythdzspizijbwlqjrjvgfznhprqmudfsyoxzimhhutjsebcykxgpywznnpbhuizuwythkbohwzzacbanyhewdfmsvpzryamuyhdkkurgvrjysjntqrrvxfnuvonvqbrqjvbvpucklligu"
    t = "xbnpukocakzqzuhdlxoga"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'\'')


if __name__ == '__main__':
    main()