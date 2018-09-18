# 303. Range Sum Query - Immutable

2018年9月18日

## 题目

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

```no
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

Note:

1. You may assume that the array does not change.
2. There are many calls to sumRange function.

## 分析

因为是要设计一个类，很容易想到直接在类内开一个数组，保存原数组的连加和，这样调用函数计算某个区间所有元素和的时候只要用简单的加法就可以了。

结合成员函数的调用方式，对于所有可能的区间只需要考虑i是否为零两种情况。前者直接返回内部数组索引为j的元素，后者需要返回索引为j和索引为i-1两个元素的差值。

尽管我个人觉得这种写法很简单很清楚，但实际上运行并不快。

## 示例代码

C++:

```cpp
class NumArray {
public:
    vector<int> sum;
    NumArray(vector<int> nums) {
        if(nums.size() == 0)
            return ;
        sum.push_back(nums[0]);
        for(int i = 1; i < nums.size(); i++)
           sum.push_back(sum[i - 1] + nums[i]);
    }
    
    int sumRange(int i, int j) {
        if(i == 0)
            return sum[j];
        else
            return sum[j] - sum[i - 1];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(i,j);
 */
```