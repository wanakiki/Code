##  217. Contains Duplicate
##### 2018-06-09 11:01:44
##### 判断是否含有相同元素
***
## 题目
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
```
Input: [1,2,3,1]
Output: true
```
Example 2:
```
Input: [1,2,3,4]
Output: false
```
Example 3:
```
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
```
## 分析
排列，遍历判断前后元素是否相同
## 示例代码
```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int len=nums.size();
        if(len<2)
            return false;
        sort(nums.begin(),nums.end());
        for(int i=0;i<len-1;i++){
            if(nums[i]==nums[i+1])
                return true;
        }
        return false;
    }
};
```
