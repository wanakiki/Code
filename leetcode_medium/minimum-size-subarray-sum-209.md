## 209. Minimum Size Subarray Sum
##### 2018-05-19 09:53:05
##### 最小尺寸的子阵列和
***
## 题目
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
```
Input: [2,3,1,2,4,3], s = 7
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
```
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
## 分析
没有想到什么算法优化，直接全部遍历了一遍，结果没有超时，更有效的办法，以后再想吧。（现在有三道等着去优化的了）
## 示例代码
```cpp
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int maxlen=INT_MAX;
        int len=nums.size();
        bool flag=false;
        for(int i=0;i<len;i++){
            int temp=0;
            for(int j=i;j<len;j++){
                temp+=nums[j];
                if(temp>=s && j-i+1<maxlen){
                    maxlen=j-i+1;
                    flag=true;
                }
            }
        }
        if(flag)
            return maxlen;
        else
            return 0;
    }
};
```
