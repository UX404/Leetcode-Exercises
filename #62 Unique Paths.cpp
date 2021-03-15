/*
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

 

Example 1:


Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
Example 3:

Input: m = 7, n = 3
Output: 28
Example 4:

Input: m = 3, n = 3
Output: 6
 

Constraints:

1 <= m, n <= 100
It's guaranteed that the answer will be less than or equal to 2 * 109.
*/


// 1 Recursion (Time limit exceeded)
class Solution {
public:
    int uniquePaths(int m, int n) {
        if (m == 0 || n == 0)
            return 0;
        else if (m == 1 && n == 1)
            return 1;
        else
            return uniquePaths(m-1, n) + uniquePaths(m, n-1);
    }
};


// 2 Iteration
// 其实这就是个从右下角往左上角延伸的杨辉三角
class Solution {
public:
    int uniquePaths(int m, int n) {
        int grid[m][n];
        for (int i = 0; i < m; ++i){
            for (int j = 0; j < n; ++j){
                if (i == 0 || j == 0)
                    grid[i][j] = 1;
                else
                    grid[i][j] = grid[i-1][j] + grid[i][j-1];
            }
        }
        return grid[m-1][n-1];
    }
};