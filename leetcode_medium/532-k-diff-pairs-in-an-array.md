## 532. 数组中的 k-diff 数对

2022-06-16 14:59:41

### 题目

给你一个整数数组 ``nums`` 和一个整数 ``k``，请你在数组中找出**不同的**k-diff 数对，并返回不同的 **k-diff 数对** 的数目。

**k-diff** 数对定义为一个整数对 ``(nums[i], nums[j])``，并满足下述全部条件：


- ``0 <= i, j < nums.length``
- ``i != j``
- ``nums[i] - nums[j] == k``


**注意**，``|val|`` 表示 ``val`` 的绝对值。



**示例 1：**

```
输入：nums = [3, 1, 4, 1, 5], k = 2
输出：2
解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个 1 ，但我们只应返回不同的数对的数量。
```

**示例 2：**

```
输入：nums = [1, 2, 3, 4, 5], k = 1
输出：4
解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5) 。
```

**示例 3：**

```
输入：nums = [1, 3, 1, 5, 4], k = 0
输出：1
解释：数组中只有一个 0-diff 数对，(1, 1) 。
```



**提示：**


- ``1 <= nums.length <= 10<sup>4</sup>``
- ``-10<sup>7</sup> <= nums[i] <= 10<sup>7</sup>``
- ``0 <= k <= 10<sup>7</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/k-diff-pairs-in-an-array/)

### 思路及代码

使用哈希表存放已经遍历过的元素，每遇到一个新元素n，在哈希表中查看是否存在n+k、n-k，如果存在则将数对中较小的数存放进set去重，最后返回set中元素的个数。

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        set<int> set_a;

        unordered_map<int,int> hash;
        for(auto n : nums){
            if(hash.find(n + k) != hash.end()){
                set_a.emplace(n);
            }
            if(hash.find(n - k) != hash.end()){
                set_a.emplace(n - k);
            }
            hash[n]++;
        }
        return set_a.size();
    }
};
```