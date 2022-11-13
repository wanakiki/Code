## 915. 分割数组

2022-10-24 09:57:42

### 题目

给定一个数组 ``nums`` ，将其划分为两个连续子数组 ``left`` 和 ``right``， 使得：


- ``left`` 中的每个元素都小于或等于 ``right`` 中的每个元素。
- ``left`` 和 ``right`` 都是非空的。
- ``left`` 的长度要尽可能小。

*在完成这样的分组后返回 ``left`` 的 **长度 **</em>。

用例可以保证存在这样的划分方法。



**示例 1：**

```

输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]
```

**示例 2：**

```

输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]
```



**提示：**


- ``2 <= nums.length <= 10<sup>5</sup>``
- ``0 <= nums[i] <= 10<sup>6</sup>``
- 可以保证至少有一种方法能够按题目所描述的那样对 ``nums`` 进行划分。



[LeetCode链接](https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals/)

### 思路及代码

普通思路，双端遍历找到切分位置。

```cpp
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        vector<int> min_val(nums.size());
        int cur_min = INT_MAX;
        for(int i = nums.size() - 1; i >= 0; i--){
            cur_min = min(cur_min, nums[i]);

            min_val[i] = cur_min;
        }

        int cur_max = 0;
        for(int i = 0; i < nums.size() - 1; i++){
            cur_max = max(cur_max, nums[i]);

            if(cur_max <= min_val[i + 1]){
                return i + 1;
            }
        }
        return 0;
    }
};
```

进阶思路，单次遍历，维护左侧区间的最大值。

```cpp
class Solution {
public:
    int partitionDisjoint(vector<int>& nums) {
        int left_max = nums[0];
        int left_pos = 0;
        int cur_max = nums[0];
        for(int i = 1; i < nums.size() - 1; i++){
            cur_max = max(cur_max, nums[i]);

            if(nums[i] < left_max){
                left_max = cur_max;
                left_pos = i;
            }
        }
        return left_pos + 1;
    }
};
```