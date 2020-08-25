'''
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]


Constraints:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
'''


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        p = len(logs) - 1
        for n in range(len(logs) - 1, -1, -1):
            if '0' <= logs[n][logs[n].index(' ') + 1] <= '9':
                logs[n], logs[p] = logs[p], logs[n]
                p -= 1

        for n in range(0, p):
            for m in range(n + 1, p + 1):
                div1 = logs[n].index(' ')
                div2 = logs[m].index(' ')
                front1, back1 = logs[n][:div1], logs[n][div1 + 1:]
                front2, back2 = logs[m][:div2], logs[m][div2 + 1:]
                if back1[0].isalpha() and back2[0].isalpha():
                    if back1 > back2:
                        logs[n], logs[m] = logs[m], logs[n]
                    elif back1 == back2 and front1 > front2:
                        logs[n], logs[m] = logs[m], logs[n]
        return logs