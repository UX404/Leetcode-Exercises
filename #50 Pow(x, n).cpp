/*
Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104
*/


// 1 for (Time limit exceeded)
class Solution {
public:
    double myPow(double x, int n) {
        int power = abs(n);
        double ans = 1.0;
        for (int i = 0; i < power; ++i)
            ans *= x;
        return n > 0 ? ans : 1/ans;
    }
};


// 2 Binary based
class Solution {
public:
    double myPow(double x, int n) {
        long power = abs(n);
        double ans = 1.0;
        while (power != 0){
            double ans_temp = x;
            long power_temp = 2;
            while (power_temp < power){
                ans_temp *= ans_temp;
                power_temp *= 2;
            }
            power -= power_temp / 2;
            ans *= ans_temp;
        }
        return n > 0 ? ans : 1/ans;
    }
};