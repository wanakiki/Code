## 279. 完全平方数

2021-06-11 10:34:22

### 题目

给定正整数*n</em>，找到若干个完全平方数（比如 ``1, 4, 9, 16, ...``）使得它们的和等于<em> n</em>。你需要让组成和的完全平方
数的个数最少。

给你一个整数 ``n`` ，返回和为 ``n`` 的完全平方数的 **最少数量** 。

**完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如，``1``、``4``、``9`` 和 ``16`` 都是完全平方数，而 ``3`` 和 ``11`` 不是。

 

**示例 1：**

```

输入：n = 12
输出：3
解释：12 = 4 + 4 + 4```

**示例 2：**

```

输入：n = 13
输出：2
解释：13 = 4 + 9```
 

**提示：**


- ``1 <= n <= 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/perfect-squares/)

### 思路及代码

动态规划，$dp[i] = 1 + min\{dp[i-j^2]|1\le j \le \sqrt{i}\}$。

```cpp
class Solution {
public:
    int numSquares(int n) {
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0;
        for(int i = 1; i <= n; i++){
            int cur = INT_MAX;
            for(int j = 1; j * j <= i; j++){
                cur = min(cur, dp[i - j*j]);
            }
            if(cur != INT_MAX){
                dp[i] = cur+1;
            }
            else{
                dp[i] = cur;
            }
        }
        return dp[n];
    }
};
```

与这个题目相关的是四平方和定理，任意正整数可表示为最多四个正整数的平方和。