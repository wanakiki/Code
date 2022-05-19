## 462. 最少移动次数使数组元素相等 II

2022-05-19 10:05:02

### 题目

给你一个长度为 ``n`` 的整数数组 ``nums`` ，返回使所有数组元素相等需要的最少移动数。

在一步操作中，你可以使数组中的一个元素加 ``1`` 或者减 ``1`` 。



**示例 1：**

```
输入：nums = [1,2,3]
输出：2
解释：
只需要两步操作（每步操作指南使一个元素加 1 或减 1）：
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
```

**示例 2：**

```
输入：nums = [1,10,2,9]
输出：16
```



**提示：**


- ``n == nums.length``
- ``1 <= nums.length <= 10<sup>5</sup>``
- ``-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii/)

### 思路及代码

将原始数组排序，计算前缀和，之后遍历排序后数组的每一个元素，判断将所有元素改为对应值时需要的操作步数，保留过程中的最小值。

```cpp
class Solution {
public:
    int minMoves2(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<long long> pre(nums.size(), 0);

        pre[0] = nums[0];
        for(int i = 1; i < nums.size(); i++){
            pre[i] = pre[i-1] + nums[i];
        }

        long long min_step = INT_MAX;
        int len = pre.size();
        for(int i = 0; i < nums.size(); i++){
            if(i == 0){
                min_step = min(min_step, (long long)(pre[nums.size() - 1] - (long long)nums[0] * pre.size()));
            }
            else if(nums[i] != nums[i-1]){
                min_step = min(min_step, (pre[len - 1] - pre[i]) - (long long)nums[i] * (len - i - 1) + (long long) nums[i] * i - pre[i-1]);
            }
        }
        return min_step;
    }
};
```