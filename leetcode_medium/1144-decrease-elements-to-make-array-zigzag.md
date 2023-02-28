## 1144. 递减元素使数组呈锯齿状

2023-02-27 09:38:14

### 题目

给你一个整数数组 ``nums``，每次 **操作** 会从中选择一个元素并 **将该元素的值减少 1**。

如果符合下列情况之一，则数组 ``A`` 就是 **锯齿数组**：


- 每个偶数索引对应的元素都大于相邻的元素，即 ``A[0] > A[1] < A[2] > A[3] < A[4] > ...``
- 或者，每个奇数索引对应的元素都大于相邻的元素，即 ``A[0] < A[1] > A[2] < A[3] > A[4] < ...``


返回将数组 ``nums`` 转换为锯齿数组所需的最小操作次数。

 

**示例 1：**

```
输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。
```

**示例 2：**

```
输入：nums = [9,6,1,6,2]
输出：4
```

 

**提示：**


- ``1 <= nums.length <= 1000``
- ``1 <= nums[i] <= 1000``



[LeetCode链接](https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag/)

### 思路及代码

由于数值只能减不能加，作为峰值的元素不应该被减，作为谷值的元素应减到两侧元素中较小的一个。因此可以分类成两种，分别统计需要的操作次数，返回较小值。

```cpp
class Solution {
public:
    int movesToMakeZigzag(vector<int>& nums) {
        if(nums.size() < 3) return 0;

        int count_o = 0;
        int count_e = 0;

        for(int i = 0; i < nums.size(); i++){
            int target_v = 0;
            if(i == 0){
                target_v = nums[1];
            }
            else if(i == nums.size() - 1){
                target_v = nums[i - 1];
            }
            else{
                target_v = min(nums[i-1], nums[i+1]);
            }


            if(i & 1){
                if(nums[i] >= target_v) count_o += nums[i] - target_v + 1;
            }
            else{
                if(nums[i] >= target_v) count_e += nums[i] - target_v + 1;
            }
        }
        return min(count_e, count_o);
    }
};
```