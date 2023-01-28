## 1664. 生成平衡数组的方案数

2023-01-28 21:04:02

### 题目

给你一个整数数组 ``nums`` 。你需要选择 **恰好** 一个下标（下标从 **0** 开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。

比方说，如果 ``nums = [6,1,7,4,1]`` ，那么：


- 选择删除下标 ``1`` ，剩下的数组为 ``nums = [6,7,4,1]`` 。
- 选择删除下标 ``2`` ，剩下的数组为 ``nums = [6,1,4,1]`` 。
- 选择删除下标 ``4`` ，剩下的数组为 ``nums = [6,1,7,4]`` 。


如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 **平衡数组** 。

请你返回删除操作后，剩下的数组 ``nums``是 **平衡数组** 的 **方案数** 。

 

**示例 1：**

```
输入：nums = [2,1,6,4]
输出：1
解释：
删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
只有一种让剩余数组成为平衡数组的方案。
```

**示例 2：**

```
输入：nums = [1,1,1]
输出：3
解释：你可以删除任意元素，剩余数组都是平衡数组。
```

**示例 3：**

```
输入：nums = [1,2,3]
输出：0
解释：不管删除哪个元素，剩下数组都不是平衡数组。
```

 

**提示：**


- ``1 <= nums.length <= 10<sup>5</sup>``
- ``1 <= nums[i] <= 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/ways-to-make-a-fair-array/)

### 思路及代码

反向遍历计算数组后缀和，之后正向遍历数组判断每个位置删除后奇偶数组的和是否相等。

```cpp
class Solution {
public:
    int waysToMakeFair(vector<int>& nums) {
        vector<long long> count(nums.size(), 0);
        int len = nums.size();
        int res = 0;

        count[len - 1] = nums[len - 1];
        if(len > 1) count[len - 2] = nums[len - 2];

        for(int i = len - 3; i >= 0; i --){
            count[i] = nums[i] + count[i + 2];
        }

        // 正向遍历
        long long even = 0;
        long long odd = 0;

        for(int i = 0; i < len; i++){
            long long cur_even = even;
            long long cur_odd = odd;
            int next_even;
            int next_odd;
            // 根据当前元素的奇偶性计算下个位置的索引
            if(i & 1){
                odd += nums[i];
                next_even = i + 2;
                next_odd = i + 1;    
            }
            else{
                even += nums[i];
                next_even = i + 1;
                next_odd = i + 2;
            }

            if(next_odd < len)  cur_odd += count[next_odd];
            if(next_even < len)  cur_even += count[next_even];
            if(cur_odd == cur_even) res++;
        }
        return res;
    }
};
```