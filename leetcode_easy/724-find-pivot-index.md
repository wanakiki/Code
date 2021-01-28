## 724. 寻找数组的中心索引

2021-01-28 13:04:15

### 题目

给定一个整数类型的数组 ``nums``，请编写一个能够返回数组 **中心索引**的方法。

我们是这样定义数组**中心索引**的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。

如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。

 

**示例 1：**

```
输入：
nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
索引 3 (nums[3] = 6) 的左侧数之和 (1 + 7 + 3 = 11)，与右侧数之和 (5 + 6 = 11) 相等。
同时, 3 也是第一个符合要求的中心索引。
```

**示例 2：**

```
输入：
nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心索引。
```

 

**说明：**


- ``nums`` 的长度范围为 ``[0, 10000]``。
- 任何一个 ``nums[i]`` 将会是一个范围在 ``[-1000, 1000]``的整数。



[LeetCode链接](https://leetcode-cn.com/problems/find-pivot-index/)

### 思路及代码

题目比较简单，但是需要注意中心索引允许出现一侧元素个数为零的情况。

```cpp
class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int len = nums.size();
        if(len == 0){
            return -1;
        }
        vector<int> count(len, 0);
        for(int i = 0; i < len; i++){
            if(i == 0){
                count[i] = nums[i];
            }
            else{
                count[i] = nums[i] + count[i-1];
            }
        }
        int aim = count[len-1];
        int left = 0;
        int res = -1;
        for(int i = 0; i < len; i++){
            if(left * 2 + nums[i] == aim){
                res = i;
                break;
            }
            left = count[i];
        }
        return res;
    }
};
```