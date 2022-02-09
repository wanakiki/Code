## 2006. 差的绝对值为 K 的数对数目

2022-02-09 09:43:02

### 题目

给你一个整数数组 ``nums`` 和一个整数 ``k`` ，请你返回数对 ``(i, j)`` 的数目，满足 ``i < j`` 且 ``|nums[i] - nums[j]| == k`` 。

``|x|`` 的值定义为：


- 如果 ``x >= 0`` ，那么值为 ``x`` 。
- 如果 ``x < 0`` ，那么值为 ``-x`` 。




**示例 1：**

```
输入：nums = [1,2,2,1], k = 1
输出：4
解释：差的绝对值为 1 的数对为：
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
```

**示例 2：**

```
输入：nums = [1,3], k = 3
输出：0
解释：没有任何数对差的绝对值为 3 。
```

**示例 3：**

```
输入：nums = [3,2,1,5,4], k = 2
输出：3
解释：差的绝对值为 2 的数对为：
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]
```



**提示：**


- ``1 <= nums.length <= 200``
- ``1 <= nums[i] <= 100``
- ``1 <= k <= 99``



[LeetCode链接](https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k/)  

### 思路及代码

是用哈希表存储数字的出现次数，遍历原始数组，对于数组中的每个元素n，查找n+k n-k的出现次数，并累加到结果上。

```cpp
class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        vector<int> count(101, 0);
        int res = 0;
        for(auto n : nums){
            int t = n + k;
            if(t < 101) res += count[t];

            t = n - k;
            if(t > 0)   res += count[t];

            count[n]++;
        }
        return res;
    }
};
```
