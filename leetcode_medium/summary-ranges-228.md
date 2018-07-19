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

循环结束时如何处理也是一个重要的细节。
### 示例代码
C++:
```cpp
class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        if(nums.size() == 0)
            return res;
        int lack = nums[0];
        int left = 0;
        for(int i = 0 ; i < nums.size() + 1; i++){
            if(nums[i] != lack + i || i == nums.size()){
                if(i - left == 1){
                    res.push_back(to_string(nums[left]));
                }
                else{
                    res.push_back(to_string(nums[left]) + "->" + to_string(nums[i-1]));
                }
                lack = nums[i] - i;
                left = i;
            }
        }
        return res;
    }
};
```
