# 283. Move Zeroes

2018年8月19日

## 题目

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

```cpp
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

Note:

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

## 分析

用一个变量zero_num记录当前遇到的零的个数，接着遍历整个数组，将非零的索引为i的元素的值赋给索引为i-zero_num的元素，如果便利过程中遇到了0，则zero_num的值加一。

遍历结束之后，非零的元素都被移动到了前面，最后几个元素应该为零，所以还要再次处理一下。

## 示例代码

C++

```cpp
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int zero_num = 0, len = nums.size();
        for(int i = 0; i < len ; i++){
            if(nums[i] == 0)
                zero_num ++;
            else{
                nums[i-zero_num] = nums[i];
            }
        }
        for(int i = len - zero_num; i < len; i++)
            nums[i] = 0;
        return ;
    }
};
```