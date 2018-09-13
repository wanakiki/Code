# 213. House Robber II

2018年9月13日

## 题目

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

```no
Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
```

Example 2:

```no
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
```

## 分析

与题目的初版（house-robber）相比，升级版的题目多加了一个限定条件：所有的房子围成了一个圈，即数组中的第一个元素和最后一个元素是不能同时取到的。

加上了这个条件，原本的动态规划方法就不再适用了。开始我的想法是在向后遍历的过程中添加一个变量记录是否包含了首个元素，但因为动态规划实现方法的限制，这个思路并不容易实现。

不过我看到了另一个相对精明的方法，分两种情况按照原来的动态规划方法处理，比较这两种情况下的最大值返回。事实证明这种方法也很快。

## 示例代码

C++

```cpp
class Solution {
public:
    int helper(vector<int> nums, int l, int r){
        if(l == r)
            return nums[l];
        // if(r = l + 1)
        //     return max(nums[l], nums[r]);
        nums[l+1] = max(nums[l+1], nums[l]);
        for(int i = l + 2; i <= r; i++){
            nums[i] = max(nums[i] + nums[i - 2], nums[i - 1]);
        }
        return max(nums[r], nums[r - 1]);
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0)
            return 0;
        if(n == 1)
            return nums[0];
        return max(helper(nums, 1, n-1), helper(nums, 0, n-2));
    }
};
```