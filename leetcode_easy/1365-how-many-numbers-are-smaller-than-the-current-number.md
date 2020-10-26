## 1365. 有多少小于当前数字的数字

2020年10月26日

### 题目

给你一个数组 ``nums``，对于其中每个元素 ``nums[i]``，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 ``nums[i]`` 你必须计算出有效的 ``j`` 的数量，其中 ``j`` 满足 ``j != i`` **且** ``nums[j] < nums[i]`` 。

以数组形式返回答案。

**示例 1：**

```
输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释：
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。
对于 nums[3]=2 存在一个比它小的数字：（1）。
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。
```

**示例 2：**

```
输入：nums = [6,5,4,8]
输出：[2,1,0,3]
```

**示例 3：**

```
输入：nums = [7,7,7,7]
输出：[0,0,0,0]
```

**提示：**


- ``2 <= nums.length <= 500``
- ``0 <= nums[i] <= 100``


### 思路及代码

将原数组复制一份，之后排序，排序后相同数字会彼此相邻，首次出现位置的索引就是小于该数字的数字个数。遍历一次排序之后的数组，统计每个数字的情况，将其保存在哈希表中，最后参照原数组遍历一遍，记录结果。

```cpp
class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> tmp(nums);
        sort(tmp.begin(), tmp.end());
        unordered_map<int, int> hash;
        for(int i = 0; i < tmp.size(); i++){
            if(i == 0 || tmp[i] != tmp[i-1]){
                hash[tmp[i]] = i;
            }
        }

        vector<int> res(nums.size(), 0);
        for(int i = 0; i < nums.size(); i++){
            res[i] = hash[nums[i]];
        }
        return res;
    }
};
```