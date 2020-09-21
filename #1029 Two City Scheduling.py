'''
A company is planning to interview 2n people. Given the array costs where costs[i] = [aCosti, bCosti], the cost of flying the ith person to city a is aCosti, and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.



Example 1:

Input: costs = [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.

The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.
Example 2:

Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
Output: 1859
Example 3:

Input: costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
Output: 3086


Constraints:

2n == costs.length
2 <= costs.length <= 100
costs.length is even.
1 <= aCosti, bCosti <= 1000
'''


# Greedy: minimum cost --> Error
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        greedy = [[n, costs[n][0] > costs[n][1], min(costs[n])] for n in range(len(costs))]  # [person, min_index, min_cost]
        greedy.sort(key=lambda x:x[2])
        print(greedy)
        status = 0  # 0: not full, 1: A full, 2: B full
        total_cost = 0
        count = [0, 0]  # 0: A_count, 1: B_count
        full = len(costs) // 2
        for i in greedy:
            if status == 0:
                count[i[1]] += 1
                total_cost += i[2]
                print(total_cost, count)
                if count[1] == full: status = 1
                if count[0] == full: status = 2
            elif status == 1:
                total_cost += costs[i[0]][0]
            elif status == 2:
                total_cost += costs[i[0]][1]
        return total_cost


# Greedy: delta cost
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        greedy = [[n, costs[n][0] - costs[n][1]] for n in range(len(costs))]  # [person, delta_cost]
        greedy.sort(key=lambda x:x[1])
        total_cost = 0
        for i in greedy[:len(costs)//2]:
            total_cost += costs[i[0]][0]
        for i in greedy[len(costs)//2:]:
            total_cost += costs[i[0]][1]
        return total_cost
