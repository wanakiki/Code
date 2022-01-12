## 334. 递增的三元子序列

2022-01-12 12:30:10

### 题目

给你一个整数数组 ``nums`` ，判断这个数组中是否存在长度为 ``3`` 的递增子序列。

如果存在这样的三元组下标 ``(i, j, k)`` 且满足 ``i < j < k`` ，使得 ``nums[i] < nums[j] < nums[k]`` ，返回 ``true`` ；否则，返回 ``false`` 。



**示例 1：**

```
输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意
```

**示例 2：**

```
输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
```

**示例 3：**

```
输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6
```



**提示：**


- ``1 <= nums.length <= 5 * 10<sup>5</sup>``
- ``-2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1``




**进阶：** 你能实现时间复杂度为 ``O(n)`` ，空间复杂度为 ``O(1)`` 的解决方案吗？


[LeetCode链接](https://leetcode-cn.com/problems/increasing-triplet-subsequence/)

### 思路及代码

采用贪心思想，遍历数组保留当前找到的最小数字和大于一个数字的最小数字，并将新访问到的数字与其比较并更新值，如果新找到的数字大于当前保存的大于一个数的最小数字，则存在三元组。

```cpp
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if(nums.size() < 3) return false;
        // 记录大于0个数的最小值和大于1个数的最小值
        int min_0 = nums[0];
        int min_1 = INT_MAX;

        for(int i = 1; i < nums.size(); i++){
            int cur = nums[i];
            if(cur <= min_0) min_0 = cur;
            else{
                if(cur <= min_1) min_1 = cur;
                else     return true;
            }
        }
        return false;
    }
};
```

之前打比赛的时候也看到过这个题目，当时用到的做法是直接双向遍历，保存左侧的最小值和右侧的最大值，之后与当前元素比较。