## 442. 数组中重复的数据

2022-05-08 09:57:08

### 题目

给你一个长度为 ``n`` 的整数数组 ``nums`` ，其中 ``nums`` 的所有整数都在范围 ``[1, n]`` 内，且每个整数出现 **一 
次** 或 **两次** 。请你找出所有出现 **两次** 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 ``O(n)`` 且仅使用常量额外空间的算法解决此问题。



**示例 1：**

```
输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]
```

**示例 2：**

```
输入：nums = [1,1,2]
输出：[1]
```

**示例 3：**

```
输入：nums = [1]
输出：[]
```



**提示：**


- ``n == nums.length``
- ``1 <= n <= 10<sup>5</sup>``
- ``1 <= nums[i] <= n``
- ``nums`` 中的每个元素出现 **一次** 或 **两次**



[LeetCode链接](https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/)

### 思路及代码

数据长度和数据范围相等， 可以直接使用原有数组空间作为哈希表记录已经出现过的数值，达到使用常量额外空间的目的。在实现时通过将对应位置的数据取相反数进行标记。

```cpp
class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        int index = 0;
        int n = nums.size();
        while(index < nums.size()){
            int cur = abs(nums[index]) - 1;
            if(nums[cur] < 0){
                res.push_back(cur + 1);
            }
            else
                nums[cur] = - nums[cur];
            index++;
        }
        return res;
    }
};
```