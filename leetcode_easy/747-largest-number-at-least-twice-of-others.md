## 748. 至少是其他数字两倍的最大数

2022-01-13 19:16:12

### 题目

给你一个整数数组 ``nums`` ，其中总是存在 **唯一的** 一个最大整数 。

请你找出数组中的最大元素并检查它是否 **至少是数组中每个其他数字的两倍** 。如果是，则返回 **最大元素的下标** ，否则返回 ``-1`` 。

 

**示例 1：**

```
输入：nums = [3,6,1,0]
输出：1
解释：6 是最大的整数，对于数组中的其他整数，6 大于数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。
```

**示例 2：**

```
输入：nums = [1,2,3,4]
输出：-1
解释：4 没有超过 3 的两倍大，所以返回 -1 。
```

**示例 3：**

```
输入：nums = [1]
输出：0
解释：因为不存在其他数字，所以认为现有数字 1 至少是其他数字的两倍。
```

 

**提示：**


- ``1 <= nums.length <= 50``
- ``0 <= nums[i] <= 100``
- ``nums`` 中的最大元素是唯一的



[LeetCode链接](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others/)

### 思路及代码

遍历数组，记录最大值和次大值，最后判断最大值是否是次大值的二倍。

```cpp
class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        int max_2_index = -1;
        int max_1 = -1, max_2 = -1;
        for(int i = 0; i < nums.size(); i++){
            int n = nums[i];
            if(n > max_1){
                if(n <= max_2){
                    max_1 = n;
                }
                else{
                    max_1 = max_2;
                    max_2 = n;
                    max_2_index = i;
                }
            }
        }

        if(max_1 == -1 || max_1 * 2 <= max_2)   return max_2_index;
        else    return -1;
    }
};
```