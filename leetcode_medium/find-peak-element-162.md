## 162. Find Peak Element
##### 2018-05-15 18:41:08
##### 找到峰值元素
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
