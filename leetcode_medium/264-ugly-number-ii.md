## 264. 丑数 II

2021-04-11 11:58:03

### 题目

给你一个整数 ``n`` ，请你找出并返回第 ``n`` 个 **丑数** 。   

**丑数**就是只包含质因数 ``2``、``3`` 和/或 ``5`` 的正整数。

 

**示例 1：**

```
输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
```

**示例 2：**

```
输入：n = 1
输出：1
解释：1 通常被视为丑数。
```

 

**提示：**


- ``1 <= n <= 1690``



[LeetCode链接](https://leetcode-cn.com/problems/ugly-number-ii/)

### 思路及代码

将得到的丑数分别和2、3、5相乘，保留较小值。

```cpp
class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> dp(n+1, 1);
        int p2 = 1, p3 = 1, p5 = 1;
        for(int i = 2; i <= n; i++){
            int num2 = dp[p2] * 2;
            int num3 = dp[p3] * 3;
            int num5 = dp[p5] * 5;

            dp[i] = min(num2, min(num3, num5));

            if(dp[i] == num2){
                p2++;
            }
            if(dp[i] == num3){
                p3++;
            }
            if(dp[i] == num5){
                p5++;
            }
        }
        return dp[n];
    }
};
```