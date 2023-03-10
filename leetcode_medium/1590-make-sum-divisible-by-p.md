## 1590. 使数组和能被 P 整除

2023-03-10 10:56:22

### 题目

给你一个正整数数组 ``nums``，请你移除 **最短** 子数组（可以为 **空**），使得剩余元素的 **和** 能被 ``p`` 整除。 **不允许** 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 ``-1`` 。

**子数组** 定义为原数组中连续的一组元素。

 

**示例 1：**

```
输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。
```

**示例 2：**

```
输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。
```

**示例 3：**

```
输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。
```

**示例  4：**

```
输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。
```

**示例 5：**

```
输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0
```

 

**提示：**


- ``1 <= nums.length <= 10<sup>5</sup>``
- ``1 <= nums[i] <= 10<sup>9</sup>``
- ``1 <= p <= 10<sup>9</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/make-sum-divisible-by-p/)

### 思路及代码

设原数组累加和模 p 的结果是 e，则题目等价于删除最短的累加和模 p 为 e 的连续子数组。

设子数组的边界分别为 i+1 和 j，则应满足以下条件，其中 pre 为前缀和数组：

$$\{pre[j] - pre[i]\} \% p = e \\  pre[i] \% p = \{ pre[j] - e \} \% p$$

上述等式可以用两种方式实现：

- 使用哈希表存储所有的前缀和，枚举左边界，使用二分查找寻找最近的右边界
- 遍历前缀和数组，使用哈希表记录 `` pre[i] % p`` 最后的出现位置，同时对每个访问到的索引查找哈希表中是否存在可删除区间的左边界

显然，第二种方法有着更好的时间复杂度。

```cpp
class Solution {
public:
    int minSubarray(vector<int>& nums, int p) {
        unordered_map<int,int> hash;
        int pre = 0;
        int e = 0;
        for(auto n : nums){
            e = (e + n) % p;
        }
        if(e == 0)  return 0;

        int res = INT_MAX;
        hash[0] = -1;   // 边界
        for(int i = 0; i < nums.size(); i++){
            pre += nums[i];
            pre %= p;

            int target = (pre + p - e) % p;
            if(hash.find(target) != hash.end()){
                int left = hash[target];
                res = min(res, i - left);
            }
            hash[pre] = i;
        }

        if(res == INT_MAX || res == nums.size())  return -1;
        return res;
    }
};
```