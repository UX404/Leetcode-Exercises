'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].


Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
'''


# 1 Problem: not all partitions are of the same length
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        count = Counter(deck)
        count = set(count.values())
        return len(count) == 1 and count != {1}


# 2 Problem: the length of the first partition isn't always the divisor of others'
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        deck.sort()
        temp = deck[0]
        step = 0

        while deck[step] == temp:
            step += 1
            if step == len(deck):
                return len(deck) > 1

        if len(deck) // step != len(deck) / step:
            return False

        for lh in range(0, len(deck), step):
            if len(set(deck[lh: lh + step])) != 1:
                return False

        return True


# 3 Problem: the smallest divisor of the deck's length isn't always the smallest divisor of all partitions
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck) == 1: return False
        deck.sort()
        step = len(deck)
        for n in range(2, int(len(deck) ** 0.5) + 1):
            if len(deck) // n == len(deck) / n:
                step = n
                break

        print(step, deck)

        for lh in range(0, len(deck), step):
            if len(set(deck[lh: lh + step])) != 1:
                return False

        return True


# 4 Correct answer
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        from collections import Counter
        count = Counter(deck)
        count = set(count.values())
        if 1 in count: return False

        count = list(count)
        temp = min(count)
        if all(m / temp == m // temp for m in count):
            return True
        for n in range(2, temp // 2 + 1):
            if all(m / n == m // n for m in count):
                return True

        print(count, temp)

        return False
