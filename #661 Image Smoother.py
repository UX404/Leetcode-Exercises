'''
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
'''


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        result = [[0 for n in range(len(M[0]))] for m in range(len(M))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                left = max(0, j-1)
                right = min(len(M[0]), j+2)
                up = max(0, i-1)
                down = min(len(M), i+2)
                avg = [sum(i[left: right]) for i in M[up:down]]
                result[i][j] = int(sum(avg) / ((right-left) * (down-up)))
        return result