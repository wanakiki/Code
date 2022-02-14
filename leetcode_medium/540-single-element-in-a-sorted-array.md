## 540. 有序数组中的单一元素

2022-02-14 11:47:23

### 题目

给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 ``O(log n)`` 时间复杂度和 ``O(1)`` 空间复杂度。



**示例 1:**

```
输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2
```

**示例 2:**

```
输入: nums =  [3,3,7,7,10,11,11]
输出: 10
```


**提示:**


- ``1 <= nums.length <= 10<sup>5</sup>``
- ``0 <= nums[i] <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/single-element-in-a-sorted-array/)

### 思路及代码

看到题目的复杂度要求，基本可以确定要用二分查找在人群中找到自己。

观察数组可以发现，在单身狗出现之前，情侣的第一个索引为偶数，在其出现之后，情侣的第一个索引变为奇数，可以用这点判断二分查找中点所处位置。

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int length = nums.size();
        if(length == 1) return nums[0];
        if(nums[0] != nums[1])  return nums[0];
        if(nums[length-1] != nums[length-2])    return nums[length-1];


        int left = 1, right = length-2;
        while(left < right){
             int mid = (left + right) / 2;
             bool flag1 = nums[mid] == nums[mid+1];
             bool flag2 = nums[mid] == nums[mid-1];
             if(!(flag1 | flag2))   return nums[mid];
             if(flag1){
                 if(mid & 1){
                     right = mid - 1;
                 }
                 else{
                     left = mid + 2;
                 }
             }
             if(flag2){
                 if(mid & 1){
                     left = mid + 1;
                 }
                 else{
                     right = mid - 2;
                 }
             }
        }
        return nums[left];
    }
};
```

进一步观察，单身狗的索引一定为偶数，所以可以只针对偶数索引进行查找。

```cpp
class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int length = nums.size();
        if(length == 1) return nums[0];
        if(nums[0] != nums[1])  return nums[0];
        if(nums[length-1] != nums[length-2])    return nums[length-1];


        int left = 1, right = (length -2) / 2;
        while(left < right){
             int mid = (left + right) / 2 * 2;
             bool flag1 = nums[mid] == nums[mid+1];
             bool flag2 = nums[mid] == nums[mid-1];
             if(!(flag1 | flag2))   return nums[mid];
             if(flag1){
                 left = (mid + 2) / 2;
             }
             if(flag2){
                 right = (mid - 2) / 2;
             }
        }
        return nums[left * 2];
    }
};
```