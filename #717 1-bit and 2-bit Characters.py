'''
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input:
bits = [1, 0, 0]
Output: True
Explanation:
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.
Example 2:
Input:
bits = [1, 1, 1, 0]
Output: False
Explanation:
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.
'''


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 1: return True
        n = len(bits) - 2
        while n >= 0:
            if bits[n] == 0:
                return True
            else:
                n -= 1
                if n < 0: return False
                if bits[n] == 0:
                    return False
                else:
                    n -= 1
                    if n < 0: return True


'''
Decision tree works as follows, bits arranged from the end to start:
×1   √0
    |   |
   √0   ×1
      |   |
     ×0   √1
         |   |
        √0   ×1
            |   |
           ×0   √1
                ...
'''