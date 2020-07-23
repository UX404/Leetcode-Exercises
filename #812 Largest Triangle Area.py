'''
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.


Notes:

3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
'''


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        import numpy as np
        S = 0
        for a in range(0, len(points)):
            for b in range(a, len(points)):
                for c in range(b, len(points)):
                    mat = np.array([[points[a][0], points[a][1], 1],
                                   [points[b][0], points[b][1], 1],
                                   [points[c][0], points[c][1], 1]])
                    S = max(S, abs(np.linalg.det(mat)) / 2)
        return S