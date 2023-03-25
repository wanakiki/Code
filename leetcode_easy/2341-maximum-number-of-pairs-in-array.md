## 2341. 数组能形成多少数对

2023-02-16 08:58:24

### 题目

给你一个下标从 **0** 开始的整数数组 ``nums`` 。在一步操作中，你可以执行以下步骤：


- 从 ``nums`` 选出 **两个** **相等的** 整数
- 从 ``nums`` 中移除这两个整数，形成一个 **数对**


请你在 ``nums`` 上多次执行此操作直到无法继续执行。

返回一个下标从 **0** 开始、长度为 ``2`` 的整数数组 ``answer`` 作为答案，其中<em>*``answer[0]``<em>*是形成的数对数目，``answer[1]`` 是对 ``nums`` 尽可能执行上述操作后剩下的整数数目。

 

**示例 1：**

```
输入：nums = [1,3,2,1,3,2,2]
输出：[3,1]
解释：
nums[0] 和 nums[3] 形成一个数对，并从 nums 中移除，nums = [3,2,3,2,2] 。
nums[0] 和 nums[2] 形成一个数对，并从 nums 中移除，nums = [2,2,2] 。
nums[0] 和 nums[1] 形成一个数对，并从 nums 中移除，nums = [2] 。
无法形成更多数对。总共形成 3 个数对，nums 中剩下 1 个数字。```

**示例 2：**

```
输入：nums = [1,1]
输出：[1,0]
解释：nums[0] 和 nums[1] 形成一个数对，并从 nums 中移除，nums = [] 。
无法形成更多数对。总共形成 1 个数对，nums 中剩下 0 个数字。```

**示例 3：**

```
输入：nums = [0]
输出：[0,1]
解释：无法形成数对，nums 中剩下 1 个数字。
```

 

**提示：**


- ``1 <= nums.length <= 100``
- ``0 <= nums[i] <= 100``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-number-of-pairs-in-array/)

### 思路及代码

根据数据范围，开辟长度为101的数组存储每个数字出现的次数，之后遍历计数数组，获得每个数字对应的数对个数并判断是否存在剩余数字。可以存在的优化是跳过计数数组中数字为零的项。

```cpp
class Solution {
public:
    vector<int> numberOfPairs(vector<int>& nums) {
        vector<int> count(101, 0);
        for(auto n : nums){
            count[n]++;
        }

        int count_pair = 0;
        int count_left = 0;
        for(auto n : count){
            if(n == 0)  continue;
            count_pair += n / 2;
            count_left += n % 2;
        }

        return {count_pair, count_left};
    }
};
```