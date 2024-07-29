'''
leetcode
task: 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/
'''

from collections import Counter
from queue import PriorityQueue

class Solution:
    def findMinMaxIndex(self, s: str, tCounter: Counter) -> tuple[int, int]:
        minIndex, maxIndex = len(s) - 1, 0
        for char in tCounter.keys():
            minIndex = min(s.index(char), minIndex)
            maxIndex = max(s.rindex(char), maxIndex)
        return (minIndex, maxIndex)

    def checkCounters(self, sCounter: Counter, tCounter: Counter) -> bool:
        for char, value in tCounter.items():
            if sCounter[char] < value:
                return False
        return True
    
    # rekurencja
    def moveCounter(self, s: str, minIndex: int, maxIndex: int, tLength: int, tCounter: Counter) -> str:
        windows = set()
        if maxIndex - minIndex >= tLength and self.checkCounters(Counter(s[minIndex + 1:maxIndex + 1]), tCounter):
            windows.add(self.moveCounter(s, minIndex + 1, maxIndex, tLength, tCounter))
        if maxIndex - minIndex >= tLength and self.checkCounters(Counter(s[minIndex: maxIndex]), tCounter):
            windows.add(self.moveCounter(s, minIndex, maxIndex - 1, tLength, tCounter))
        if len(windows) == 0:
            return s[minIndex:maxIndex+1]
        return min(windows, key=lambda x: len(x))

    def moveCounterDynamic(self, s: str, minIndex: int, maxIndex: int, tLength: int, tCounter: Counter) -> str:
        last_word = (minIndex, maxIndex)
        words, used_words = set(), set()
        words.add(last_word)
        used_words.add(last_word)
        while words:
            new_words = set()
            for word in words:
                last_word = word
                if last_word[1] - last_word[0] >= tLength:
                    if self.checkCounters(Counter(s[last_word[0] + 1:last_word[1] + 1]), tCounter) and (last_word[0] + 1, last_word[1]) not in used_words:
                        new_words.add((last_word[0] + 1, last_word[1]))
                        used_words.add((last_word[0] + 1, last_word[1]))
                    if self.checkCounters(Counter(s[last_word[0]:last_word[1]]), tCounter) and (last_word[0], last_word[1] - 1) not in used_words:
                        new_words.add((last_word[0], last_word[1] - 1))
                        used_words.add((last_word[0], last_word[1] - 1))
            del words
            words = new_words
        print(len(used_words))
        return s[last_word[0]:last_word[1]+1]
    
    def moveCounterQueue(self, s: str, minIndex: int, maxIndex: int, tLength: int, tCounter: Counter) -> str:
        indexQueue = PriorityQueue()
        indexQueue.put((maxIndex - minIndex, minIndex, maxIndex))
        usedWords = set()
        usedWords.add((minIndex, maxIndex))
        minWord = (minIndex, maxIndex)
        while not indexQueue.empty():
            _, minIndex, maxIndex = indexQueue.get()
            changeMade = False
            if maxIndex - minIndex >= tLength:
                if self.checkCounters(Counter(s[minIndex + 1:maxIndex + 1]), tCounter) and (minIndex + 1, maxIndex) not in usedWords:
                    usedWords.add((minIndex + 1, maxIndex))
                    indexQueue.put((maxIndex - 1 - minIndex, minIndex + 1, maxIndex))
                    changeMade = True
                if self.checkCounters(Counter(s[minIndex:maxIndex]), tCounter) and (minIndex, maxIndex - 1) not in usedWords:
                    usedWords.add((minIndex, maxIndex - 1))
                    indexQueue.put((maxIndex - 1 - minIndex, minIndex, maxIndex - 1))
                    changeMade = True
            if not changeMade:
              #  print(minIndex, maxIndex)
              #  print(minWord)
                if (maxIndex - minIndex) < (minWord[1] - minWord[0]):
                    minWord = (minIndex, maxIndex)
                    print(s[minWord[0]:minWord[1]+1])
              #  else:
               #     return s[minWord[0]:minWord[1]+1]
        print(len(usedWords))
        return s[minWord[0]:minWord[1]+1]


    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        if s == '' or not self.checkCounters(Counter(s), tCounter):
            return ''
        minIndex, maxIndex = self.findMinMaxIndex(s, tCounter)
        tLength = len(t)
        return self.moveCounterQueue(s, minIndex, maxIndex, tLength, tCounter)
      #  return self.moveCounterDynamic(s, minIndex, maxIndex, tLength, tCounter)
       # return self.moveCounter(s, minIndex, maxIndex, tLength, tCounter)

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