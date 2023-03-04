## 982. 按位与为零的三元组

2023-03-04 12:41:13

### 题目

给你一个整数数组 ``nums`` ，返回其中 **按位与三元组** 的数目。

**按位与三元组** 是由下标 ``(i, j, k)`` 组成的三元组，并满足下述全部条件：


- ``0 <= i < nums.length``
- ``0 <= j < nums.length``
- ``0 <= k < nums.length``
- ``nums[i] &amp; nums[j] &amp; nums[k] == 0`` ，其中 ``&amp;`` 表示按位与运算符。

 

**示例 1：**

```

输入：nums = [2,1,3]
输出：12
解释：可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 &amp; 2 &amp; 1
(i=0, j=1, k=0) : 2 &amp; 1 &amp; 2
(i=0, j=1, k=1) : 2 &amp; 1 &amp; 1
(i=0, j=1, k=2) : 2 &amp; 1 &amp; 3
(i=0, j=2, k=1) : 2 &amp; 3 &amp; 1
(i=1, j=0, k=0) : 1 &amp; 2 &amp; 2
(i=1, j=0, k=1) : 1 &amp; 2 &amp; 1
(i=1, j=0, k=2) : 1 &amp; 2 &amp; 3
(i=1, j=1, k=0) : 1 &amp; 1 &amp; 2
(i=1, j=2, k=0) : 1 &amp; 3 &amp; 2
(i=2, j=0, k=1) : 3 &amp; 2 &amp; 1
(i=2, j=1, k=0) : 3 &amp; 1 &amp; 2
```

**示例 2：**

```

输入：nums = [0,0,0]
输出：27
```

 

**提示：**


- ``1 <= nums.length <= 1000``
- ``0 <= nums[i] < 2<sup>16</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/triples-with-bitwise-and-equal-to-zero/)

### 思路及代码

最容易想到的方式是直接三重遍历，找到可行的方案总数，但是复杂度较高。采用经典的解题思路，使用哈希表保存二重遍历的结果，再对哈希表和原数组的数据进行一次遍历，对复杂度进行优化。

在具体代码实现时，在最开始增加了数据去重的操作。

```python
class Solution {
public:
    int countTriplets(vector<int>& nums) {
        unordered_map<int,int> real_nums;
        unordered_map<int,int> hash;

        for(auto n : nums){
            real_nums[n]++;
        }
        
        for(auto &[k, v] : real_nums){
            for(auto &[u, w] : real_nums){
                hash[k & u] += v * w;
            }
        }

        int res = 0;
        for(auto &[k, v] : hash){
            for(auto &[u,w] : real_nums){
                if((k & u) == 0){
                    res += v * w;
                }
            }
        }
        return res;
    }
};
```