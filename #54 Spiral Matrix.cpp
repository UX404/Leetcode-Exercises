/*
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
*/


class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> ans;
        int m = matrix.size()-1;
        int n = matrix[0].size();
        int i = 0, j = -1;
        bool right = true, down = true;
        bool stop = false;
        while (!stop){
            if (m == 0) stop = true;
            for (int step = 0; step < n; ++step){
                right ? j++ : j--;
                ans.push_back(matrix[i][j]);
            }
            right = !right;
            n--;
            if (stop) break;
            if (n == 0) stop = true;
            for(int step = 0; step < m; ++step){
                down ? i++ : i--;
                ans.push_back(matrix[i][j]);
            }
            down = !down;
            m--;
        }
        return ans;
    }
};