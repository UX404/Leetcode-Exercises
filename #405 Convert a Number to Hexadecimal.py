'''
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

1. All letters in hexadecimal (a-f) must be in lowercase.
2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
4. You must not use any method provided by the library which converts/formats the number to hex directly.
'''


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0: return "0"
        num = num % 0x100000000
        convert = "0123456789abcdef"
        result_reverse = ""
        while num > 0:
            result_reverse += convert[num % 16]
            num //= 16
        return result_reverse[::-1]