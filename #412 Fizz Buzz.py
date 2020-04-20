'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


# 1 Basic method
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for m in range(1, n+1):
            if m % 15 == 0: result.append("FizzBuzz")
            elif m % 3 == 0: result.append("Fizz")
            elif m % 5 == 0: result.append("Buzz")
            else: result.append(str(m))
        return result


# 2 Add gradually
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = ["Fizz" if (m + 1) % 3 == 0 else "" for m in range(n)]
        for m in range(n):
            if (m + 1) % 5 == 0:
                result[m] += "Buzz"
            elif not result[m]:
                result[m] = str(m + 1)
        return result
# add Fizz -> add Buzz -> add number
