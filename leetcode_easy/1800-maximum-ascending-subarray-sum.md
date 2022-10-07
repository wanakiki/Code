## 1800. 最大升序子数组和

2022-10-07 09:11:32

### 题目

给你一个正整数组成的数组 ``nums`` ，返回 ``nums`` 中一个 **升序 **子数组的最大可能元素和。

子数组是数组中的一个连续数字序列。

已知子数组 ``[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]`` ，若对所有 ``i``（``l <= i < r``），``nums<sub>i </sub> < nums<sub>i+1</sub>`` 都成立，则称这一子数组为 **升序** 子数组。注意，大小为 ``1`` 的子数组也视作 **升序** 子数组。

 

**示例 1：**

```
输入：nums = [10,20,30,5,10,50]
输出：65
解释：[5,10,50] 是元素和最大的升序子数组，最大元素和为 65 。
```

**示例 2：**

```
输入：nums = [10,20,30,40,50]
输出：150
解释：[10,20,30,40,50] 是元素和最大的升序子数组，最大元素和为 150 。
```

**示例 3：**

```
输入：nums = [12,17,15,13,10,11,12]
输出：33
解释：[10,11,12] 是元素和最大的升序子数组，最大元素和为 33 。
```

**示例 4：**

```
输入：nums = [100,10,1]
输出：100
```

 

**提示：**


- ``1 <= nums.length <= 100``
- ``1 <= nums[i] <= 100``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-ascending-subarray-sum/)

### 思路及代码

累加升序数组，遇到降序时更新累加值，并更新最大值。

```cpp
class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int res = 0;
        int count = 0;
        for(int i = 0; i < nums.size(); i++){
            if(i == 0 || nums[i] <= nums[i-1]){
                res = max(res, count);
                count = nums[i];
            }
            else{
                count += nums[i];
            }
        }
        res = max(res, count);
        return res;
    }
};
```