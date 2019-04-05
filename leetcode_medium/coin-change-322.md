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

第二个方法是比动态规划快得多的回溯，通过一个非常秀的剪枝大大优化了代码运行时间。

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

```cpp
class Solution {
public:
    int res = INT_MAX;  //全局结果
    int coinChange(vector<int>& coins, int amount) {
        if(!amount) return 0;
        sort(coins.begin(), coins.end(), greater<int>());
        helper(coins, 0, amount, 0);
        return res == INT_MAX ? -1 : res;
    }

    void helper(vector<int>& coins, int now, int amount, int cur){
        if(now >= coins.size()) return;
        if(amount % coins[now] == 0){
            res = min(res, cur + amount/coins[now]);
            return ;
        }

        for(int i = amount/coins[now]; i >= 0; i--){
            if(cur+i >= res - 1)    break;  //剪枝 可以放在循环外
            helper(coins, now+1, amount-coins[now]*i, cur+i);
        }
    }
};
```

当目前的硬币书大于等于当前所得到的最小的硬币数减一的时候，就不需要进行判断。