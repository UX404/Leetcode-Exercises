/*
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:


Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]
Example 2:

Input: n = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
*/


class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        int count = 1;
        vector<int> row(n, 0);
        vector<vector<int>> matrix(n, row);
        int i = 0, j = 0;
        for(; j < n; ++j)
            matrix[i][j] = count++;
        j--;
        for(int step = n-1; step > 0; --step){
            if ((n - step) % 2 == 1){
                for(int step2 = 0; step2 < step; ++step2)
                    matrix[++i][j] = count++;
                for(int step2 = 0; step2 < step; ++step2)
                    matrix[i][--j] = count++;
            }
            else{
                for(int step2 = 0; step2 < step; ++step2)
                    matrix[--i][j] = count++;
                for(int step2 = 0; step2 < step; ++step2)
                    matrix[i][++j] = count++;
            }
        }
        return matrix;
    }
};