## 523. 连续的子数组和

2021-06-02 19:25:51

### 题目

给你一个整数数组 ``nums`` 和一个整数 ``k`` ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：


- 子数组大小 **至少为 2** ，且
- 子数组元素总和为 ``k`` 的倍数。


如果存在，返回 ``true`` ；否则，返回 ``false`` 。

如果存在一个整数 ``n`` ，令整数 ``x`` 符合 ``x = n * k`` ，则称 ``x`` 是 ``k`` 的一个倍数。

 

**示例 1：**

```
输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
```

**示例 2：**

```
输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
```

**示例 3：**

```
输入：nums = [23,2,6,4,7], k = 13
输出：false
```

 

**提示：**


- ``1 <= nums.length <= 10<sup>5</sup>``
- ``0 <= nums[i] <= 10<sup>9</sup>``
- ``0 <= sum(nums[i]) <= 2<sup>31</sup> - 1``
- ``1 <= k <= 2<sup>31</sup> - 1``



[LeetCode链接](https://leetcode-cn.com/problems/continuous-subarray-sum/)

### 思路及代码

还是经典前缀和搭配哈希表，不过需要注意模k。$(pre[j] - pre[i])\%k=0 \Rightarrow pre[j]\%k - pre[i]\%k = 0$，用哈希表存储模k之后的前缀和，并进行查找，需要注意的是题目要求结果数组的长度至少为2，所以当查找到目标之后需要判断数组长度，因此最好存储前缀和的索引，且只保存第一个。

```cpp
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int pre = 0;
        unordered_map<int, int> hash;
        // 允许出现零 但间隔要大于2
        hash[0] = -1;
        for(int i = 0; i < nums.size(); i++){
            int n = nums[i];
            pre += n;
            int cur = pre % k;
            if(hash.find(cur) != hash.end()){
                if(i - hash[cur] > 1){
                    return true;
                }
            }
            else{
                hash[cur] = i;
            }

        }
        return false;
    }
};
```