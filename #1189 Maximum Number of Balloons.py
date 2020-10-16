'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.



Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0


Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
'''


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        count = Counter(text)
        if count.__contains__('b') and count.__contains__('a') and count.__contains__('l') and count.__contains__('o') and count.__contains__('n'):
            return min(count['b'], count['a'], count['l']//2, count['o']//2, count['n'])
        else:
            return 0