## 966. 和相同的二元子数组

2021-07-08 20:34:54       

### 题目

给你一个二元数组 ``nums`` ，和一个整数 ``goal`` ，请你统计并返回有多少个和为 ``goal`` 的**非空**子数组。

**子数组** 是数组的一段连续部分。

 

**示例 1：**

```
输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]
```

**示例 2：**

```
输入：nums = [0,0,0,0,0], goal = 0
输出：15
```

 

**提示：**


- ``1 <= nums.length <= 3 * 10<sup>4</sup>``
- ``nums[i]`` 不是 ``0`` 就是 ``1``
- ``0 <= goal <= nums.length``



[LeetCode链接](https://leetcode-cn.com/problems/binary-subarrays-with-sum/)

### 思路及代码

遍历数组，假设当前累加和为sum，则以当前元素为右边界能构成的和为goal的非空数组为$hash[sum - goal]$。其中hash为统计了当前元素之前所有累加和出现次数的哈希表，上式需要满足的条件是sum>goal。

```cpp
class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int cur_sum = 0;
        int res = 0;
        unordered_map<int, int> hash;
        hash[0] = 1;
        for(auto n : nums){
            cur_sum += n;
            if(cur_sum >= goal){
                res += hash[cur_sum - goal];
            }
            hash[cur_sum] += 1;     // 注意一定要计算过当前位置作为右边界的可能情况后再将当前累加和存入哈希表
        }
        return res;
    }
};
```