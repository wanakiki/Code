## 377. 组合总和 Ⅳ

2021-04-24 16:06:17

### 题目

给你一个由 **不同** 整数组成的数组 ``nums`` ，和一个目标整数 ``target`` 。请你从 ``nums`` 中找出并返回总和为 ``target`` 
的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

 

**示例 1：**

```
输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
```

**示例 2：**

```
输入：nums = [9], target = 3
输出：0
```

 

**提示：**


- ``1 <= nums.length <= 200``
- ``1 <= nums[i] <= 1000``
- ``nums`` 中的所有元素 **互不相同**
- ``1 <= target <= 1000``


 

**进阶：** 如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？      


[LeetCode链接](https://leetcode-cn.com/problems/combination-sum-iv/)

### 思路及代码

动态规划，由于顺序不同的序列视为不同组合，可以根据nums数组中的值向前查找，并进行累加。

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<int> dp(target+1, 0);
        dp[0] = 1;
        for(int i = 1; i <= target; i++){
            for(auto num : nums){
                // 注意排除过程中出现的越界数据
                if(num <= i && dp[i-num] < INT_MAX - dp[i]){
                    dp[i] += dp[i-num];
                }
            }
        }
        return dp[target];
    }
};
```

当数据中出现负数时，正数和复数相加可能出现零，如果不对每种组合的长度进行限制，组合的可能数是无限多的（零可以无限叠加），无法求出。