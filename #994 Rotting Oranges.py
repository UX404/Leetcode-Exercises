'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.



Example 1:



Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.


Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
'''


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        time = 0
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if grid[n][m] == 2:
                    queue.append([n, m])
        while queue:
            temp = []
            rotten = False
            for loc in queue:
                if loc[0] > 0 and grid[loc[0]-1][loc[1]] == 1:
                    grid[loc[0]-1][loc[1]] = 2
                    temp.append([loc[0]-1, loc[1]])
                    rotten = True  # Up
                if loc[0] < len(grid)-1 and grid[loc[0]+1][loc[1]] == 1:
                    grid[loc[0]+1][loc[1]] = 2
                    temp.append([loc[0]+1, loc[1]])
                    rotten = True  # Down
                if loc[1] > 0 and grid[loc[0]][loc[1]-1] == 1:
                    grid[loc[0]][loc[1]-1] = 2
                    temp.append([loc[0], loc[1]-1])
                    rotten = True  # Left
                if loc[1] < len(grid[0])-1 and grid[loc[0]][loc[1]+1] == 1:
                    grid[loc[0]][loc[1]+1] = 2
                    temp.append([loc[0], loc[1]+1])
                    rotten = True  # Right
            if rotten:
                time += 1
            queue = temp
        for n in range(len(grid)):
            for m in range(len(grid[0])):
                if grid[n][m] == 1:
                    return -1
        return time