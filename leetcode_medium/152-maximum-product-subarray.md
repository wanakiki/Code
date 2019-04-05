# Maximum Product Subarray

2019年4月5日10点33分

动态规划

## 题目

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

```no
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
```

Example 2:

```no
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

## 分析

因为负数乘负数会出现正数，所以在求最大子序列的时候需要保存之前的最小值。比较容易联想到动态规划算法，而且用动态规划来实现会非常方便。代码没有太多要注意的点，注释处tmp变量是必须的，因为high会被优先更新。

```cpp
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int high, low, res, tmp;
        if(!nums.size())
            return 0;
        high = low = res = nums[0];
        for(int i = 1; i < nums.size(); i++){
            tmp = high; //high会发生变化
            high = max(high*nums[i], max(nums[i], low*nums[i]));
            low = min(tmp*nums[i], min(nums[i], low*nums[i]));
            if(high > res)
                res = high;
        }
        return res;
    }
};
```