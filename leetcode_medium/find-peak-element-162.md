## 162. Find Peak Element
##### 2018-05-15 18:41:08
##### 找到峰值元素 二分
***
## 题目
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

## 分析

根据峰值元素的判断条件，我们可以遍历整个数组，根据条件筛选。因为-1，n的值为无穷小，对于1，n-1这两个点我们还需要细节性的处理。

这时候，我们思考一下，既然可以遍历到一个元素，这就证明这个元素一定大于它的上一个元素，根据这点，我们还可以对代码进行优化，得到相对可以的解决方案。

上面已经有一个解法了，但复杂度为O(n)，而题目要求复杂度为O(logn)，刚学过数据结构，很容易就联想到了二分方法。同时这道题目的确是支持二分方法进行查找的。  
首先要注意到当存在多个峰值时只要求我们返回一个峰值，并且相邻元素都是不等的。在这个前提下再进行思考，不难发现的确存在这样的二分规律:

1. 当nums[mid] < nums[mid+1]时，mid元素的右侧一定存在一个峰值。
2. 反之，mid元素及其左侧一定存在一个峰值，因为这个峰值也有可能是mid本身。

根据上面这个规律我们便可以很简单的写出二分查找的方法了。（不过这个题目二分方法和遍历方法用时相差不大）


## 示例代码

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        for(int i=0;i<nums.size();i++){
            if(i+1<nums.size() && nums[i+1]>nums[i])
                continue;
            return i;
        }
        return 0;
    }
};
```

二分

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l = 0, r = nums.size() - 1, mid;
        while(l < r){
            mid = (l + r)/2;
            if(nums[mid] < nums[mid+1])
                l = mid + 1;
            else
                r = mid;    //注意两个不同的处理方法
        }
        return l;
    }
};
```
