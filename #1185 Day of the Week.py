'''
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.



Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"


Constraints:

The given dates are valid dates between the years 1971 and 2100.
'''


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        ans = 4
        ans += (year-1971)*365 + (year-1968)//4
        mon_day = {1: 0, 2: 31, 3: 59, 4: 90, 5: 120, 6: 151, 7: 181, 8: 212, 9: 243, 10: 273, 11: 304, 12: 334}
        ans += mon_day[month]
        ans += day
        if year == 2100:
            ans -= 1  # 2100 not lunar year
        elif year % 4 == 0 and month <= 2:
            ans -= 1  # not 2/29 yet
        week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        return week[ans%7]