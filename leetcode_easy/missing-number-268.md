# 268. Missing Number

2018年8月6日

## 题目

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

```no
Input: [3,0,1]
Output: 2
```

Example 2:

```no
Input: [9,6,4,2,3,5,7,0,1]
Output: 8
```

Note:

Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## 分析

先排序，再遍历数组找到缺失的元素。要注意当给出的数组连续的时候要返回下一个数。比如[1,0]需要返回2。

这是最容易想到的做法，提交之后看了看别人的解答，最快的方式是用数学知识来解决，应该的总数减去现有的总数就是缺少的那个数字。还有少数人用位运算。

## 代码

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int i = 0;
        for(i = 0; i < nums.size(); i++){
            if(nums[i] != i)
                return i;
        }
        return i;
    }
};
```

计算总数：

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int sm = 0;
        for(auto n: nums)
            sm += n;
        //int l = nums.size();
        return (nums.size()*(nums.size()+1)/2) - sm;
    }
};
```