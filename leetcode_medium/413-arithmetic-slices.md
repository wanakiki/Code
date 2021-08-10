## 413. 等差数列划分

2021-08-10 20:24:41

### 题目

如果一个数列 **至少有三个元素** ，并且任意两个相邻元素之差相同，则称该数列为等差数列。


- 例如，``[1,3,5,7,9]``、``[7,7,7,7]`` 和 ``[3,-1,-5,-9]`` 都是等差数列。


给你一个整数数组 ``nums`` ，返回数组 ``nums`` 中所有为等差数组的 **子数组** 个数。

**子数组** 是数组中的一个连续序列。

 

**示例 1：**

```
输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
```

**示例 2：**

```
输入：nums = [1]
输出：0
```

 

**提示：**


- ``1 <= nums.length <= 5000``
- ``-1000 <= nums[i] <= 1000``




[LeetCode链接](https://leetcode-cn.com/problems/arithmetic-slices/)

### 思路及代码

```cpp
class Solution {
public:
    int helper(int n){
        if(n <= 2)  return 0;
        n -= 2;
        return n * (n + 1) / 2;
    }

    int numberOfArithmeticSlices(vector<int>& nums) {
        int len = nums.size();
        if(len < 3) return 0;

        int res = 0;
        int count = 1;
        int last_diff = nums[1] - nums[0];
        for(int i = 2; i < len; i++){
            int cur_diff = nums[i] - nums[i-1];
            if(cur_diff == last_diff){
                count++;
            }
            else{
                res += helper(count + 1);
                count = 1;
                last_diff = cur_diff;
            }
        }
        res += helper(count + 1);
        return res;
    }
};

/*
n   count
1   0
2   0
3   1
4   1 + 2 = 3
5   1 + 2 + 3 = 6
6   1 + 2 + 3 + 4 = 10

n > 2 时
n -= 2
n * (n + 1) / 2
*/
```