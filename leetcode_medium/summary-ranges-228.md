## 228. Summary Ranges
##### 2018年7月19日
***
### 题目
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
```
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
```
Example 2:
```
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
```
### 分析
标记一个区间开始的位置，然后判断是否连续，进行更新。因为数组是排好序的，为了提高运行速度，可以另外设置一个变量标记出该位置应该有的值。

循环结束时如何处理也是一个重要的细节，我的做法是可以遍历到数组结束后一个元素，并根据left和i的位置判断应该添加几个元素。
### 示例代码
C++:
```cpp
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
         if(nums.size() == 0)
            return res;
        int left = 0, lack = nums[0];
        int i = 0;
        for(i = 0; i <= nums.size(); i++){
            if(i == nums.size() || nums[i] != lack){
                if(i == left + 1)
                    res.push_back(to_string(nums[i - 1]));    
                else
                    res.push_back(to_string(nums[left]) + "->" + to_string(nums[i - 1]));
                left = i ;
                if(i != nums.size())
                    lack = nums[i];
            }
            lack ++;
        }
        return res;
    }
};
```
