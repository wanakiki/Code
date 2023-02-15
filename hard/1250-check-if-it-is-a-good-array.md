## 1250. 检查「好数组」

2023-02-15 19:32:44

### 题目

给你一个正整数数组 ``nums``，你需要从中任选一些子集，然后将子集中每一个数乘以一个 **任意整数**，并求出他们的和。

假如该和结果为 ``1``，那么原数组就是一个「**好数组**」，则返回 ``True``；否则请返回 ``False``。

 

**示例 1：**

```
输入：nums = [12,5,7,23]
输出：true
解释：挑选数字 5 和 7。
5*3 + 7*(-2) = 1
```

**示例 2：**

```
输入：nums = [29,6,10]
输出：true
解释：挑选数字 29, 6 和 10。
29*1 + 6*(-3) + 10*(-1) = 1
```

**示例 3：**

```
输入：nums = [3,6]
输出：false
```

 

**提示：**


- ``1 <= nums.length <= 10^5``
- ``1 <= nums[i] <= 10^9``



[LeetCode链接](https://leetcode-cn.com/problems/check-if-it-is-a-good-array/)

### 思路及代码

读完题目，发现只要数组中存在两个数的最大公因数是1即可满足条件，如果数据更多，只要让额外的数据乘0即可。看解析发现是一个数论题目，涉及裴蜀定理。

```cpp
class Solution {
public:
    bool isGoodArray(vector<int>& nums) {
        int cur = nums[0];
        for(auto n : nums){
            cur = gcd(n, cur);
            if(cur == 1){
                break;
            }
        }
        return cur == 1;
    }
};
```