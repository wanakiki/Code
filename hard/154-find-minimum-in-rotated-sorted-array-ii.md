## 154. 寻找旋转排序数组中的最小值 II

2021-04-09 10:30:59

### 题目

已知一个长度为 ``n`` 的数组，预先按照升序排列，经由 ``1`` 到 ``n`` 次 **旋转** 后，得到输入数组。例如，原数组 ``nums = [0,1,4,4,5,6,7]`` 在变化后可能得到：

- 若旋转 ``4`` 次，则可以得到 ``[4,5,6,7,0,1,4]``
- 若旋转 ``7`` 次，则可以得到 ``[0,1,4,4,5,6,7]``


注意，数组 ``[a[0], a[1], a[2], ..., a[n-1]]`` **旋转一次** 的结果为数组 ``[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`` 。

给你一个可能存在 **重复** 元素值的数组 ``nums`` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最
小元素** 。

 

**示例 1：**

```
输入：nums = [1,3,5]
输出：1
```

**示例 2：**

```
输入：nums = [2,2,2,0,1]
输出：0
```

 

**提示：**


- ``n == nums.length``
- ``1 <= n <= 5000``
- ``-5000 <= nums[i] <= 5000``
- ``nums`` 原来是一个升序排序的数组，并进行了 ``1`` 至 ``n`` 次旋转


 

**进阶：**


- 这道题是 <a href="https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/">寻找旋转排序数组中的最小值</a> 的延伸题目。
- 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？



[LeetCode链接](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)

### 思路及代码

看完题目之后感觉是二分，但是找不到解决方案，乖乖去看了题解。

简单说一下题解的思路，将位于中间的元素和右边界进行比较，出现三种情况：

- nums[pivot] > nums[right]，说明最小值应该在pivot右边，忽略左半部分。
- nums[pivot] < nums[right]，最小值在pivot左边，忽略右半部分
- 当两者相等时，因为存在重复元素，不能确定最小值的位置，但是右端点对应的元素必然至少存在一个替代品（存在相同的nums[pivot]），可以忽略右端点。

![示例](https://assets.leetcode-cn.com/solution-static/154/4.png)

相等的情况较难理解，感觉对二分法掌握不怎么样。

```cpp
class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0, high = nums.size() - 1;
        while(low < high){
            int pivot = low + (high - low) / 2;
            if(nums[pivot] < nums[high]){
                high = pivot;
            }
            else if(nums[pivot] > nums[high]){
                low = pivot + 1;
            }
            else{
                high -= 1;
            }
        }
        return nums[low];
    }
};
```