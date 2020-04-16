'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''


# 1 Recursion ??
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        # [8 4 2 1 : 32 16 8 4 2 1]
        light = [0 for n in range(10)]
        result = []

        def lighten(times, start):
            global light
            global result
            if times == 0:
                if light.count(1) == num:
                    hour = 8 * light[0] + 4 * light[1] + 2 * light[2] + 1 * light[3]
                    minute = 32 * light[4] + 16 * light[5] + 8 * light[6] + 4 * light[7] + 2 * light[8] + 1 * light[9]
                    if hour < 12 and minute < 10:
                        result.append(str(hour) + ":0" + str(minute))
                    elif hour < 12 and minute < 60:
                        result.append(str(hour) + ":" + str(minute))
                light = [0 for n in range(10)]
                return
            for n in range(start, 10):
                light[n] = 1
                lighten(times - 1, start + 1)

        lighten(num, 0)
        return result


# 2 Iteration
class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        result = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == num:
                    if minute < 10: result.append(str(hour) + ":0" + str(minute))
                    else: result.append(str(hour) + ":" + str(minute))
        return result