'''
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
'''


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for i in points:
            all_distance = {}
            for j in points:
                distance = (i[0]-j[0]) ** 2 + (i[1]-j[1]) ** 2
                if all_distance.__contains__(distance): all_distance[distance] += 1
                else: all_distance[distance] = 1
            for value in all_distance.values():
                result += value * (value - 1)
        return result