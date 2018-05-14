## 179. Largest Number
##### 2018-05-14 21:25:47
##### 最大数字
***
## 题目
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
```
Input: [10,2]
Output: "210"
```
Example 2:
```
Input: [3,30,34,5,9]
Output: "9534330"
```
## 分析
首先要了解一下一个关键的函数：``to_string(i)``，其作用是将整数转化为字符串。其余的部分就相对简单了。

自定义排序：将两个整数转化为字符串病比较两种组合方式，给出返回值。  
开始我的做法是这样，但是如果提前把所有的整数转化为字符串再比较会快很多。

## 示例代码
```cpp
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        string res;
        //sort(nums.begin(),nums.end(),greater<int>());
        sort(nums.begin(),nums.end(),[](int a,int b){
            string c=to_string(a)+to_string(b),d=to_string(b)+to_string(a);
            return d<c;
        });
        for(int i=0;i<nums.size();i++){
            if(i==0 && nums[0]==0)
                return "0";	//避免多个零的情况
            res+=to_string(nums[i]);
        }
        return res;
    }
};
```
