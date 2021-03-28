## 456. 132 模式

2021-03-24 17:43:06

### 题目

给你一个整数数组 ``nums`` ，数组中共有 ``n`` 个整数。**132 模式的子序列**  
由三个整数 ``nums[i]``、``nums[j]`` 和 ``nums[k]`` 组成，并同时满足：``i < 
j < k`` 和 ``nums[i] < nums[k] < nums[j]`` 。

如果 ``nums`` 中存在 **132 模式的子序列** ，返回 ``true`` ；否则，返回 ``false`` 。

 

**进阶：**很容易想到时间复杂度为 ``O(n^2)`` 的解决方案，你可以设计一个时间 
复杂度为 ``O(n logn)`` 或 ``O(n)`` 的解决方案吗？

 

**示例 1：**

```
输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。
```

**示例 2：**

```
输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。
```

**示例 3：**

```
输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。
```

 

**提示：**


- ``n == nums.length``
- ``1 <= n <= 10<sup>4</sup>``
- ``-10<sup>9</sup> <= nums[i] <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/132-pattern/)

### 思路及代码

这是一个比较绕的题目，可以使用单调栈来解题，下面是参照官方题解代码写出来的程序，目前不能完全说清楚原理。

```cpp
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        stack<int> candidate_k;
        int max_k = INT_MIN;
        
        int len = nums.size();
        if(len < 3) return false;
        candidate_k.push(nums[len-1]);

        for(int i = len - 2; i >= 0; i--){
            if(nums[i] < max_k){
                return true;
            }

            while(!candidate_k.empty() && nums[i] > candidate_k.top()){
                max_k = candidate_k.top();
                candidate_k.pop();
            }

            if(nums[i] > max_k){
                candidate_k.push(nums[i]);
            }
        }
        return false;
    }
};
```