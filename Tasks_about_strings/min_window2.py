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
        # get starting min and max indexes
        minIndex, maxIndex = self.findMinMaxIndex(s, tCounter)
        # set min word to min - max indexes
        minWord = (minIndex, maxIndex)
        # set iterators
        iMin, iMax = minIndex, minIndex + len(t) - 1
        # get actual sCounter
        sCounter = Counter(s[iMin:iMax + 1])
        # main loop
        while iMin < iMax and iMax < maxIndex:
            # expand iMax so that all letters from t are coveres
            while iMax < maxIndex and not self.checkCounters(sCounter, tCounter):
                iMax += 1
                sCounter[s[iMax]] += 1
            # check if actual word is shortest one    
            if self.checkCounters(sCounter, tCounter) and iMax - iMin < minWord[1] - minWord[0]:
                minWord = (iMin, iMax)
            # expand iMin so that one letter is missing
            while iMin < iMax and self.checkCounters(sCounter, tCounter):
                sCounter[s[iMin]] -= 1
                iMin += 1
            # add missing letter to counter
            sCounter[s[iMin - 1]] += 1
            # check if it is smallest word
            if self.checkCounters(sCounter, tCounter) and iMax - iMin + 1 < minWord[1] - minWord[0]:
                minWord = (iMin - 1, iMax)
            # remove letter from counter
            sCounter[s[iMin - 1]] -= 1
        # return min word
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
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'fzzvqprlizelwmkjchwtcdbvpbosminsjpncehnmgtzegk\'')
    # test 5
    s = "xeaifhaqslynbcwxncwgeezbrjorzyuwevejcecuscjvgfutkrcqxbromihlgcjnzpybwcxqeglknhgzyiqxljnyrvlazvnyklbgoywugjftrltrvlrgueeobsoandazqbigbgbhqgdjtycojtwfydtbvjekmejdirjlymvquybnyddjxaoxfkyatckijvlrnwcnjxfdxgtvjweiyvfdhefaipkrnviaunpfmukkcdhlcmwcjbgqhnsqfdhsasuwhjbtfmdhrluvzqykugcbtutyzdqcxkyevaxcodjhogdpwbzsjducxpdzsvbpizvfbtirwtzmzebyhcqqfmueczdwveofgjkhesbamaolgrlpvcfcqbhubmtythdzspizijbwlqjrjvgfznhprqmudfsyoxzimhhutjsebcykxgpywznnpbhuizuwythkbohwzzacbanyhewdfmsvpzryamuyhdkkurgvrjysjntqrrvxfnuvonvqbrqjvbvpucklligu"
    t = "xbnpukocakzqzuhdlxoga"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'nsqfdhsasuwhjbtfmdhrluvzqykugcbtutyzdqcxkyevaxcodjhogdp\'')
    # test 6
    s = "acbdbaab"
    t = "aabd"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'dbaa\'')


if __name__ == '__main__':
    main()