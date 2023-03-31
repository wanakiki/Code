## 2367. 算术三元组的数目

2023-03-31 09:05:05

### 题目

给你一个下标从 **0** 开始、**严格递增** 的整数数组 ``nums`` 和一个正整数 ``diff`` 。如果满足下述全部条件，则三元组 ``(i, j, k)`` 就是一个 **算术三元组** ：


- ``i < j < k`` ，
- ``nums[j] - nums[i] == diff`` 且
- ``nums[k] - nums[j] == diff``


返回不同 **算术三元组** 的数目。

 

**示例 1：**

```
输入：nums = [0,1,4,6,7,10], diff = 3
输出：2
解释：
(1, 2, 4) 是算术三元组：7 - 4 == 3 且 4 - 1 == 3 。
(2, 4, 5) 是算术三元组：10 - 7 == 3 且 7 - 4 == 3 。
```

**示例 2：**

```
输入：nums = [4,5,6,7,8,9], diff = 2
输出：2
解释：
(0, 2, 4) 是算术三元组：8 - 6 == 2 且 6 - 4 == 2 。
(1, 3, 5) 是算术三元组：9 - 7 == 2 且 7 - 5 == 2 。
```

 

**提示：**


- ``3 <= nums.length <= 200``
- ``0 <= nums[i] <= 200``
- ``1 <= diff <= 50``
- ``nums`` **严格** 递增



[LeetCode链接](https://leetcode-cn.com/problems/number-of-arithmetic-triplets/)

### 思路及代码

使用哈希表存储之前出现的元素，如果不能找到差 diff 的元素，保存为 0，能找到保存为 1。

另一种实现方式是使用三指针，确定最小的指针之后移动剩余指针的位置，由于数组本身递增，三元组的指针同样递增，顺序移动即可。

```cpp
class Solution {
public:
    int arithmeticTriplets(vector<int>& nums, int diff) {
        unordered_map<int,int> hash;
        int res = 0;
        // 0 代表第一个 1 代表第二个
        for(auto n : nums){
            int left = n - diff;

            if(hash.find(left) != hash.end()){
                if(hash[left] == 0){
                    hash[n] = 1;
                }
                else{
                    res ++;
                    hash[n] = 1;
                }
            }
            else{
                hash[n] = 0;
            }
        }
        return res;
    }
};
```