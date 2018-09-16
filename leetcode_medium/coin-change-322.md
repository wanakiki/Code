# 322. Coin Change

2018年9月16日

## 题目

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

```no
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```

Example 2:

```no
Input: coins = [2], amount = 3
Output: -1
```

Note:

You may assume that you have an infinite number of each kind of coin.

## 分析

刚学编程的时候从一个代课老师那里了解到了贪心算法，当时老师用的就是这个题目。

很明显，简单的贪心算法是不能完美解决这个问题的。我这里采用的是动态规划的方法，维护一个一维数组，数组中索引为i值表示总数为i时最少的钱币数。实现很简单，但是比较难想出来。

## 示例代码

C++

```cpp
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> dp(amount + 1, amount + 1);
        dp[0] = 0;
        for(int i = 1; i <= amount; i++){
            for(int j = 0; j < coins.size(); j++){
                if(coins[j] <= i){
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1);
                }
            }
        }
        return dp[amount] == amount + 1 ? -1 : dp[amount];
    }
};
```