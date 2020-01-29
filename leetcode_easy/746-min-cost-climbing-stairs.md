## 746. 使用最小花费爬楼梯

2020年1月29日

### 题目

数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 ``cost[i]``(索引从0开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:
```no
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
```

示例 2:
```no
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
```

注意：
- cost 的长度将会在 [2, 1000]。
- 每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs

### 思路

很容易看出这道题目可以用动态规划求解，递推公式为``cost[i] = cost[i] + min(cost[i-1], cost[i-2])``，需要从i = 2开始进行递推，最后返回递推结果数组最右边两个数中较小的一个。

### 代码

不使用额外空间：
```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int len = cost.size();
        for(int i = 2; i < len; i++){
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2]);
        }
        return min(cost[len - 1], cost[len - 2]);
    }
};
```

使用两个变量进行存储：
```cpp
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int len = cost.size();
        int dp0 = cost[0], dp1 = cost[1];
        for(int i = 2; i < len; i++){
            int tmp = cost[i] + min(dp0, dp1);
            dp0 = dp1;
            dp1 = tmp;
        }
        return min(dp1, dp0);
    }
};
```